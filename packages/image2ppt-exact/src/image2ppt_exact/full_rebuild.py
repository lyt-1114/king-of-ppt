from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .blueprint import BlueprintRebuildConfig, rebuild_from_blueprint
from .pipeline import (
    ImageSvgEditableConfig,
    ImageSvgEditableResult,
    run_image_svg_editable_pipeline,
)


@dataclass(frozen=True)
class FullRebuildConfig:
    src: Path
    out: Path
    blueprint_path: Path | None = None
    blueprint_pptx_path: Path | None = None
    assets_root: Path | None = None
    editable_pptx_path: Path | None = None
    ocr_dir: Path | None = None
    pattern: str = "slide_*.png"
    width: int = 1920
    height: int = 1080
    lang: str = "ch"
    background: str = "blank"
    default_font: str = "Microsoft YaHei"
    default_color: str = "#111827"
    min_text_height: float | None = None
    min_text_area: float | None = None
    lock_file: Path | None = None
    spec_file: Path | None = None
    force: bool = False
    allow_empty_text: bool = False


@dataclass(frozen=True)
class FullRebuildResult:
    slide_count: int
    svg_dir: Path
    preview_path: Path
    exact_pptx_path: Path | None
    ocr_dir: Path
    editable_pptx_path: Path
    pipeline_log_path: Path
    full_rebuild_log_path: Path
    expected_text_blocks: int
    actual_text_boxes: int
    skipped_by_height: int = 0
    skipped_by_area: int = 0
    skipped_by_lock: int = 0
    blueprint_pptx_path: Path | None = None
    blueprint_log_path: Path | None = None
    blueprint_text_objects: int = 0
    blueprint_shape_objects: int = 0
    blueprint_picture_objects: int = 0
    blueprint_line_objects: int = 0


def run_full_rebuild_pipeline(config: FullRebuildConfig) -> FullRebuildResult:
    out = config.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    image_result = run_image_svg_editable_pipeline(
        ImageSvgEditableConfig(
            src=config.src,
            out=out,
            editable_pptx_path=config.editable_pptx_path,
            ocr_dir=config.ocr_dir,
            pattern=config.pattern,
            width=config.width,
            height=config.height,
            lang=config.lang,
            background=config.background,
            default_font=config.default_font,
            default_color=config.default_color,
            min_text_height=config.min_text_height,
            min_text_area=config.min_text_area,
            lock_file=config.lock_file,
            spec_file=config.spec_file,
            force=config.force,
            allow_empty_text=config.allow_empty_text,
        )
    )

    blueprint_pptx_path: Path | None = None
    blueprint_log_path: Path | None = None
    blueprint_text_objects = 0
    blueprint_shape_objects = 0
    blueprint_picture_objects = 0
    blueprint_line_objects = 0

    if config.blueprint_path is not None:
        blueprint_pptx_path = (
            config.blueprint_pptx_path or out / "high_fidelity_editable.pptx"
        ).resolve()
        blueprint_result = rebuild_from_blueprint(
            BlueprintRebuildConfig(
                blueprint_path=config.blueprint_path,
                pptx_path=blueprint_pptx_path,
                assets_root=config.assets_root,
            )
        )
        blueprint_pptx_path = blueprint_result.pptx_path
        blueprint_log_path = blueprint_result.log_path
        blueprint_text_objects = blueprint_result.text_count
        blueprint_shape_objects = blueprint_result.shape_count
        blueprint_picture_objects = blueprint_result.picture_count
        blueprint_line_objects = blueprint_result.line_count

    full_log_path = out / "full-rebuild-log.md"
    full_log_path.write_text(
        build_full_rebuild_log(
            config=config,
            image_result=image_result,
            full_log_path=full_log_path,
            blueprint_pptx_path=blueprint_pptx_path,
            blueprint_log_path=blueprint_log_path,
            blueprint_text_objects=blueprint_text_objects,
            blueprint_shape_objects=blueprint_shape_objects,
            blueprint_picture_objects=blueprint_picture_objects,
            blueprint_line_objects=blueprint_line_objects,
        ),
        encoding="utf-8",
    )

    return FullRebuildResult(
        slide_count=image_result.slide_count,
        svg_dir=image_result.svg_dir,
        preview_path=image_result.preview_path,
        exact_pptx_path=image_result.exact_pptx_path,
        ocr_dir=image_result.ocr_dir,
        editable_pptx_path=image_result.editable_pptx_path,
        pipeline_log_path=image_result.pipeline_log_path,
        full_rebuild_log_path=full_log_path,
        expected_text_blocks=image_result.expected_text_blocks,
        actual_text_boxes=image_result.actual_text_boxes,
        skipped_by_height=image_result.skipped_by_height,
        skipped_by_area=image_result.skipped_by_area,
        skipped_by_lock=image_result.skipped_by_lock,
        blueprint_pptx_path=blueprint_pptx_path,
        blueprint_log_path=blueprint_log_path,
        blueprint_text_objects=blueprint_text_objects,
        blueprint_shape_objects=blueprint_shape_objects,
        blueprint_picture_objects=blueprint_picture_objects,
        blueprint_line_objects=blueprint_line_objects,
    )


def build_full_rebuild_log(
    *,
    config: FullRebuildConfig,
    image_result: ImageSvgEditableResult,
    full_log_path: Path,
    blueprint_pptx_path: Path | None,
    blueprint_log_path: Path | None,
    blueprint_text_objects: int,
    blueprint_shape_objects: int,
    blueprint_picture_objects: int,
    blueprint_line_objects: int,
) -> str:
    lines = [
        "# Full Rebuild Execution Log",
        "",
        "## Route",
        "",
        "- Exact proof route: preserve a pixel-faithful baseline with SVG wrappers, HTML preview, and an exact image PPTX.",
        "- Editable text route: rebuild OCR text as native PowerPoint text boxes.",
        "- High-fidelity blueprint route: optionally rebuild native PowerPoint objects from a blueprint JSON.",
        "- Verification route: record slide counts, text counts, object counts, and output paths in one handoff log.",
        "",
        "## Inputs",
        "",
        f"- Source slide images: `{config.src.resolve()}`",
        f"- Pattern: `{config.pattern}`",
        f"- Canvas: `{config.width} x {config.height}`",
        f"- Editable text background mode: `{config.background}`",
        f"- OCR JSON: `{image_result.ocr_dir}`",
        f"- Minimum editable text height: `{config.min_text_height if config.min_text_height is not None else 'disabled'}`",
        f"- Minimum editable text area: `{config.min_text_area if config.min_text_area is not None else 'disabled'}`",
        f"- OCR lock file: `{config.lock_file.resolve() if config.lock_file else 'not provided'}`",
        f"- Spec correction file: `{config.spec_file.resolve() if config.spec_file else 'not provided'}`",
        f"- Blueprint JSON: `{config.blueprint_path.resolve() if config.blueprint_path else 'not provided'}`",
        "",
        "## Outputs",
        "",
        f"- Full rebuild log: `{full_log_path}`",
        f"- SVG wrappers: `{image_result.svg_dir}`",
        f"- SVG preview: `{image_result.preview_path}`",
        f"- Exact image PPTX: `{image_result.exact_pptx_path}`",
        f"- Editable text PPTX: `{image_result.editable_pptx_path}`",
    ]
    if blueprint_pptx_path is not None:
        lines.extend(
            [
                f"- High-fidelity editable PPTX: `{blueprint_pptx_path}`",
                f"- Blueprint log: `{blueprint_log_path}`",
            ]
        )
    else:
        lines.append(
            "- High-fidelity editable PPTX: `not generated because no blueprint JSON was provided`"
        )

    lines.extend(
        [
            "",
            "## Verification",
            "",
            f"- Slides: `{image_result.slide_count}`",
            f"- OCR text blocks: `{image_result.expected_text_blocks}`",
            f"- Editable PPT text boxes: `{image_result.actual_text_boxes}`",
            f"- OCR blocks skipped by height: `{image_result.skipped_by_height}`",
            f"- OCR blocks skipped by area: `{image_result.skipped_by_area}`",
            f"- OCR blocks skipped by lock regions: `{image_result.skipped_by_lock}`",
            f"- Blueprint text objects: `{blueprint_text_objects}`",
            f"- Blueprint shape objects: `{blueprint_shape_objects}`",
            f"- Blueprint picture objects: `{blueprint_picture_objects}`",
            f"- Blueprint line objects: `{blueprint_line_objects}`",
            "",
            "## Boundary",
            "",
            "- The exact image PPTX is the visual baseline and should be used for pixel comparison.",
            "- The editable text PPTX proves the recoverable text layer.",
            "- The high-fidelity editable PPTX is the native-object rebuild and depends on blueprint quality.",
            "- A flattened bitmap can be pixel-identical, while native PowerPoint objects require reconstruction.",
            "",
        ]
    )
    return "\n".join(lines)
