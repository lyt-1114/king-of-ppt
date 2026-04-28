from __future__ import annotations

import argparse
from pathlib import Path

from .editable import EditableConfig, OcrConfig, create_editable_text_pptx, extract_ocr_json
from .exporter import ExportConfig, export_exact_deck
from .pipeline import ImageSvgEditableConfig, run_image_svg_editable_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="image2ppt-exact",
        description=(
            "Export full-slide images as pixel-identical SVG wrappers and an "
            "optional full-image PPTX."
        ),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    export = subparsers.add_parser("export", help="Export an exact image deck.")
    export.add_argument("src", type=Path, help="Folder containing slide images.")
    export.add_argument("--out", type=Path, required=True, help="Output folder.")
    export.add_argument(
        "--pattern",
        default="slide_*.png",
        help="Glob used to find slide images. Default: slide_*.png",
    )
    export.add_argument("--width", type=int, default=1920, help="Canvas width.")
    export.add_argument("--height", type=int, default=1080, help="Canvas height.")
    export.add_argument("--title", default="Exact Image2PPT Export")
    export.add_argument(
        "--pptx",
        type=Path,
        default=None,
        help="PPTX output path. Defaults to OUT/exact_image_deck.pptx.",
    )
    export.add_argument(
        "--no-pptx",
        action="store_true",
        help="Only generate SVG wrappers, preview, and run log.",
    )
    export.add_argument(
        "--force",
        action="store_true",
        help="Allow overwriting generated files in an existing output folder.",
    )

    ocr = subparsers.add_parser(
        "ocr",
        help="Extract editable text boxes into per-slide OCR JSON using PaddleOCR.",
    )
    ocr.add_argument("src", type=Path, help="Folder containing slide images.")
    ocr.add_argument("--out", type=Path, required=True, help="OCR JSON output folder.")
    ocr.add_argument(
        "--pattern",
        default="slide_*.png",
        help="Glob used to find slide images. Default: slide_*.png",
    )
    ocr.add_argument("--lang", default="ch", help="PaddleOCR language. Default: ch")

    editable = subparsers.add_parser(
        "editable",
        help="Create a PPTX with native editable text boxes from OCR JSON.",
    )
    editable.add_argument("src", type=Path, help="Folder containing slide images.")
    editable.add_argument("--ocr", type=Path, required=True, help="OCR JSON folder.")
    editable.add_argument("--pptx", type=Path, required=True, help="PPTX output path.")
    editable.add_argument(
        "--pattern",
        default="slide_*.png",
        help="Glob used to find slide images. Default: slide_*.png",
    )
    editable.add_argument("--width", type=int, default=1920, help="Canvas width.")
    editable.add_argument("--height", type=int, default=1080, help="Canvas height.")
    editable.add_argument(
        "--background",
        choices=["keep", "blank"],
        default="keep",
        help="Keep original slide image as background, or create text-only slides.",
    )
    editable.add_argument("--font", default="Microsoft YaHei")
    editable.add_argument("--color", default="#111827")

    pipeline = subparsers.add_parser(
        "image-svg-editable",
        help=(
            "Run image -> SVG exact proof -> OCR JSON -> editable PPTX with "
            "verification."
        ),
    )
    pipeline.add_argument("src", type=Path, help="Folder containing slide images.")
    pipeline.add_argument("--out", type=Path, required=True, help="Output folder.")
    pipeline.add_argument(
        "--pptx",
        type=Path,
        default=None,
        help="Editable PPTX path. Defaults to OUT/editable_text_layer.pptx.",
    )
    pipeline.add_argument(
        "--ocr",
        type=Path,
        default=None,
        help="Existing OCR JSON folder. If omitted, creates OUT/ocr_json.",
    )
    pipeline.add_argument(
        "--pattern",
        default="slide_*.png",
        help="Glob used to find slide images. Default: slide_*.png",
    )
    pipeline.add_argument("--width", type=int, default=1920, help="Canvas width.")
    pipeline.add_argument("--height", type=int, default=1080, help="Canvas height.")
    pipeline.add_argument("--lang", default="ch", help="PaddleOCR language.")
    pipeline.add_argument(
        "--background",
        choices=["keep", "blank"],
        default="keep",
        help="Keep original slide image as background, or create text-only slides.",
    )
    pipeline.add_argument("--font", default="Microsoft YaHei")
    pipeline.add_argument("--color", default="#111827")
    pipeline.add_argument("--force", action="store_true")
    pipeline.add_argument(
        "--allow-empty-text",
        action="store_true",
        help="Allow decks with zero OCR text blocks.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "export":
        result = export_exact_deck(
            ExportConfig(
                src=args.src,
                out=args.out,
                pattern=args.pattern,
                width=args.width,
                height=args.height,
                title=args.title,
                pptx_path=args.pptx,
                create_pptx=not args.no_pptx,
                force=args.force,
            )
        )
        print(f"slides={result.slide_count}")
        print(f"svg_dir={result.svg_dir}")
        print(f"preview={result.preview_path}")
        print(f"run_log={result.run_log_path}")
        if result.pptx_path is not None:
            print(f"pptx={result.pptx_path}")
        return 0

    if args.command == "ocr":
        out = extract_ocr_json(
            OcrConfig(
                src=args.src,
                out=args.out,
                pattern=args.pattern,
                lang=args.lang,
            )
        )
        print(f"ocr_json={out}")
        return 0

    if args.command == "editable":
        pptx_path = create_editable_text_pptx(
            EditableConfig(
                src=args.src,
                ocr_dir=args.ocr,
                pptx_path=args.pptx,
                pattern=args.pattern,
                width=args.width,
                height=args.height,
                background=args.background,
                default_font=args.font,
                default_color=args.color,
            )
        )
        print(f"editable_pptx={pptx_path}")
        return 0

    if args.command == "image-svg-editable":
        result = run_image_svg_editable_pipeline(
            ImageSvgEditableConfig(
                src=args.src,
                out=args.out,
                editable_pptx_path=args.pptx,
                ocr_dir=args.ocr,
                pattern=args.pattern,
                width=args.width,
                height=args.height,
                lang=args.lang,
                background=args.background,
                default_font=args.font,
                default_color=args.color,
                force=args.force,
                allow_empty_text=args.allow_empty_text,
            )
        )
        print(f"slides={result.slide_count}")
        print(f"svg_dir={result.svg_dir}")
        print(f"preview={result.preview_path}")
        print(f"exact_pptx={result.exact_pptx_path}")
        print(f"ocr_json={result.ocr_dir}")
        print(f"editable_pptx={result.editable_pptx_path}")
        print(f"pipeline_log={result.pipeline_log_path}")
        print(f"ocr_text_blocks={result.expected_text_blocks}")
        print(f"editable_text_boxes={result.actual_text_boxes}")
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
