from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Pt

from .exporter import collect_slide_images


@dataclass(frozen=True)
class EditableConfig:
    src: Path
    ocr_dir: Path
    pptx_path: Path
    pattern: str = "slide_*.png"
    width: int = 1920
    height: int = 1080
    background: str = "blank"
    default_font: str = "Microsoft YaHei"
    default_color: str = "#111827"


@dataclass(frozen=True)
class OcrConfig:
    src: Path
    out: Path
    pattern: str = "slide_*.png"
    lang: str = "ch"


def create_editable_text_pptx(config: EditableConfig) -> Path:
    from pptx import Presentation
    from pptx.util import Inches

    images = collect_slide_images(config.src.resolve(), config.pattern)
    ocr_dir = config.ocr_dir.resolve()
    if not ocr_dir.exists():
        raise FileNotFoundError(f"OCR JSON folder not found: {ocr_dir}")

    prs = Presentation()
    prs.slide_width = Inches(config.width / 144)
    prs.slide_height = Inches(config.height / 144)
    blank_layout = prs.slide_layouts[6]
    default_color = parse_hex_color(config.default_color)

    for image_path in images:
        slide = prs.slides.add_slide(blank_layout)
        if config.background == "keep":
            slide.shapes.add_picture(
                str(image_path),
                0,
                0,
                width=prs.slide_width,
                height=prs.slide_height,
            )
        elif config.background != "blank":
            raise ValueError("background must be either 'keep' or 'blank'")

        blocks = load_slide_blocks(ocr_dir, image_path.stem)
        for block in blocks:
            x, y, w, h = normalize_bbox(block["bbox"], config.width, config.height)
            shape = slide.shapes.add_textbox(
                px_to_emu(x, config.width, prs.slide_width),
                px_to_emu(y, config.height, prs.slide_height),
                px_to_emu(w, config.width, prs.slide_width),
                px_to_emu(h, config.height, prs.slide_height),
            )
            text_frame = shape.text_frame
            text_frame.clear()
            text_frame.margin_left = 0
            text_frame.margin_right = 0
            text_frame.margin_top = 0
            text_frame.margin_bottom = 0
            text_frame.word_wrap = True

            paragraph = text_frame.paragraphs[0]
            paragraph.alignment = parse_alignment(block.get("align"))
            run = paragraph.add_run()
            run.text = str(block.get("text", ""))
            run.font.name = str(block.get("font", config.default_font))
            run.font.size = Pt(
                float(block.get("font_size") or estimate_font_size(h, config.height))
            )
            run.font.bold = bool(block.get("bold", False))
            run.font.italic = bool(block.get("italic", False))
            run.font.color.rgb = (
                parse_hex_color(block.get("color", config.default_color))
                or default_color
            )

    config.pptx_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(config.pptx_path)
    return config.pptx_path


def extract_ocr_json(config: OcrConfig) -> Path:
    rapid_ocr = None
    try:
        from paddleocr import PaddleOCR
    except ImportError:
        PaddleOCR = None  # type: ignore[assignment]

    if PaddleOCR is None:
        rapid_ocr = create_rapid_ocr()
        if rapid_ocr is None:
            raise RuntimeError(
                "No OCR engine is available. Install optional OCR dependencies "
                "with pip install -e .[ocr], or install rapidocr-onnxruntime, "
                "or provide OCR JSON manually."
            )

    ocr = None
    if PaddleOCR is not None:
        try:
            ocr = PaddleOCR(use_angle_cls=True, lang=config.lang)
        except Exception:
            rapid_ocr = create_rapid_ocr()
            if rapid_ocr is None:
                raise

    if ocr is None and rapid_ocr is None:
        raise RuntimeError(
            "No OCR engine is available. Provide OCR JSON manually."
        )

    images = collect_slide_images(config.src.resolve(), config.pattern)
    config.out.mkdir(parents=True, exist_ok=True)

    for image_path in images:
        if ocr is not None:
            try:
                raw_result = run_paddle_ocr(ocr, image_path)
                blocks = paddle_result_to_blocks(raw_result)
            except Exception:
                rapid_ocr = rapid_ocr or create_rapid_ocr()
                if rapid_ocr is None:
                    raise
                ocr = None
                raw_result = run_rapid_ocr(rapid_ocr, image_path)
                blocks = rapid_result_to_blocks(raw_result)
        else:
            raw_result = run_rapid_ocr(rapid_ocr, image_path)
            blocks = rapid_result_to_blocks(raw_result)
        (config.out / f"{image_path.stem}.json").write_text(
            json.dumps({"blocks": blocks}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    return config.out


def create_rapid_ocr() -> Any | None:
    try:
        from rapidocr_onnxruntime import RapidOCR
    except ImportError:
        return None
    return RapidOCR()


def run_paddle_ocr(ocr: Any, image_path: Path) -> Any:
    try:
        return ocr.ocr(str(image_path), cls=True)
    except TypeError:
        return ocr.predict(str(image_path))


def run_rapid_ocr(ocr: Any, image_path: Path) -> Any:
    result, _ = ocr(str(image_path))
    return result or []


def paddle_result_to_blocks(raw_result: Any) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    pages = raw_result if isinstance(raw_result, list) else [raw_result]
    if len(pages) == 1 and isinstance(pages[0], list):
        lines = pages[0]
    else:
        lines = []
        for page in pages:
            if isinstance(page, list):
                lines.extend(page)

    for line in lines:
        if not isinstance(line, (list, tuple)) or len(line) < 2:
            continue
        box = line[0]
        payload = line[1]
        if not isinstance(payload, (list, tuple)) or not payload:
            continue
        text = str(payload[0])
        confidence = float(payload[1]) if len(payload) > 1 else None
        blocks.append(
            {
                "text": text,
                "bbox": polygon_to_xywh(box),
                "confidence": confidence,
            }
        )
    return blocks


def rapid_result_to_blocks(raw_result: Any) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    for line in raw_result or []:
        if not isinstance(line, (list, tuple)) or len(line) < 2:
            continue
        box = line[0]
        text = str(line[1])
        confidence = float(line[2]) if len(line) > 2 else None
        blocks.append(
            {
                "text": text,
                "bbox": polygon_to_xywh(box),
                "confidence": confidence,
            }
        )
    return blocks


def polygon_to_xywh(points: Any) -> list[float]:
    xs = [float(point[0]) for point in points]
    ys = [float(point[1]) for point in points]
    return [min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)]


def load_slide_blocks(ocr_dir: Path, stem: str) -> list[dict[str, Any]]:
    path = ocr_dir / f"{stem}.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        blocks = data.get("blocks", [])
        if isinstance(blocks, list):
            return blocks
    raise ValueError(f"Unsupported OCR JSON schema: {path}")


def normalize_bbox(raw_bbox: Any, width: int, height: int) -> tuple[float, float, float, float]:
    if isinstance(raw_bbox, dict):
        x = float(raw_bbox.get("x", raw_bbox.get("left", 0)))
        y = float(raw_bbox.get("y", raw_bbox.get("top", 0)))
        w = float(raw_bbox.get("w", raw_bbox.get("width", 0)))
        h = float(raw_bbox.get("h", raw_bbox.get("height", 0)))
    elif isinstance(raw_bbox, list) and len(raw_bbox) == 4:
        x, y, w, h = [float(value) for value in raw_bbox]
        if w > x and h > y and (w > width * 0.5 or h > height * 0.5):
            w -= x
            h -= y
    else:
        raise ValueError(f"Unsupported bbox value: {raw_bbox!r}")

    return clamp_box(x, y, w, h, width, height)


def clamp_box(
    x: float,
    y: float,
    w: float,
    h: float,
    width: int,
    height: int,
) -> tuple[float, float, float, float]:
    x = max(0, min(x, width))
    y = max(0, min(y, height))
    w = max(1, min(w, width - x))
    h = max(1, min(h, height - y))
    return x, y, w, h


def px_to_emu(value: float, source_extent: int, slide_extent: int) -> int:
    return int(round((value / source_extent) * slide_extent))


def estimate_font_size(box_height_px: float, slide_height_px: int) -> float:
    slide_height_points = 7.5 * 72
    return max(6, min(44, box_height_px / slide_height_px * slide_height_points * 0.72))


def parse_hex_color(value: str | None) -> RGBColor | None:
    if not value:
        return None
    match = re.fullmatch(r"#?([0-9a-fA-F]{6})", str(value).strip())
    if not match:
        return None
    raw = match.group(1)
    return RGBColor(int(raw[0:2], 16), int(raw[2:4], 16), int(raw[4:6], 16))


def parse_alignment(value: Any) -> PP_ALIGN:
    normalized = str(value or "left").lower()
    if normalized == "center":
        return PP_ALIGN.CENTER
    if normalized == "right":
        return PP_ALIGN.RIGHT
    return PP_ALIGN.LEFT
