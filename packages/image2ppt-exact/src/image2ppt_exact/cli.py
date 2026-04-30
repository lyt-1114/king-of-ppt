from __future__ import annotations

import argparse
from pathlib import Path

from .blueprint import BlueprintRebuildConfig, rebuild_from_blueprint
from .editable import EditableConfig, OcrConfig, create_editable_text_pptx, extract_ocr_json
from .exporter import ExportConfig, export_exact_deck
from .full_rebuild import FullRebuildConfig, run_full_rebuild_pipeline
from .native_svg import SvgNativeRebuildConfig, rebuild_from_svg_native
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
        default="blank",
        help=(
            "Create text-only slides by default. Use keep only when the source "
            "images are text-free or when making a debug overlay."
        ),
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
        default="blank",
        help=(
            "Create text-only slides by default. Use keep only when the source "
            "images are text-free or when making a debug overlay."
        ),
    )
    pipeline.add_argument("--font", default="Microsoft YaHei")
    pipeline.add_argument("--color", default="#111827")
    pipeline.add_argument("--force", action="store_true")
    pipeline.add_argument(
        "--allow-empty-text",
        action="store_true",
        help="Allow decks with zero OCR text blocks.",
    )

    blueprint = subparsers.add_parser(
        "blueprint-rebuild",
        help=(
            "Rebuild a high-fidelity editable PPTX from a blueprint JSON using "
            "native text boxes, shapes, lines, pictures, and components."
        ),
    )
    blueprint.add_argument("blueprint", type=Path, help="Blueprint JSON path.")
    blueprint.add_argument("--pptx", type=Path, required=True, help="PPTX output path.")
    blueprint.add_argument(
        "--assets-root",
        type=Path,
        default=None,
        help="Folder used to resolve relative image asset paths.",
    )

    svg_native = subparsers.add_parser(
        "svg-native-rebuild",
        help=(
            "Convert structured SVG slides into native editable PowerPoint "
            "objects."
        ),
    )
    svg_native.add_argument("src", type=Path, help="Folder containing SVG slides.")
    svg_native.add_argument("--pptx", type=Path, required=True, help="PPTX output path.")
    svg_native.add_argument(
        "--pattern",
        default="slide_*.svg",
        help="Glob used to find SVG slides. Default: slide_*.svg",
    )
    svg_native.add_argument("--width", type=int, default=None, help="Canvas width override.")
    svg_native.add_argument("--height", type=int, default=None, help="Canvas height override.")
    svg_native.add_argument("--font", default="Microsoft YaHei")
    svg_native.add_argument("--color", default="#111827")

    full = subparsers.add_parser(
        "full-rebuild",
        help=(
            "Run exact proof, OCR editable text, optional blueprint rebuild, "
            "and a unified verification log."
        ),
    )
    full.add_argument("src", type=Path, help="Folder containing slide images.")
    full.add_argument("--out", type=Path, required=True, help="Output folder.")
    full.add_argument(
        "--blueprint",
        type=Path,
        default=None,
        help="Optional blueprint JSON for high-fidelity native-object rebuild.",
    )
    full.add_argument(
        "--blueprint-pptx",
        type=Path,
        default=None,
        help="High-fidelity PPTX path. Defaults to OUT/high_fidelity_editable.pptx.",
    )
    full.add_argument(
        "--assets-root",
        type=Path,
        default=None,
        help="Folder used to resolve relative blueprint image asset paths.",
    )
    full.add_argument(
        "--pptx",
        type=Path,
        default=None,
        help="Editable text PPTX path. Defaults to OUT/editable_text_layer.pptx.",
    )
    full.add_argument(
        "--ocr",
        type=Path,
        default=None,
        help="Existing OCR JSON folder. If omitted, creates OUT/ocr_json.",
    )
    full.add_argument(
        "--pattern",
        default="slide_*.png",
        help="Glob used to find slide images. Default: slide_*.png",
    )
    full.add_argument("--width", type=int, default=1920, help="Canvas width.")
    full.add_argument("--height", type=int, default=1080, help="Canvas height.")
    full.add_argument("--lang", default="ch", help="PaddleOCR language.")
    full.add_argument(
        "--background",
        choices=["keep", "blank"],
        default="blank",
        help=(
            "Create text-only slides by default. Use keep only when the source "
            "images are text-free or when making a debug overlay."
        ),
    )
    full.add_argument("--font", default="Microsoft YaHei")
    full.add_argument("--color", default="#111827")
    full.add_argument("--force", action="store_true")
    full.add_argument(
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

    if args.command == "blueprint-rebuild":
        result = rebuild_from_blueprint(
            BlueprintRebuildConfig(
                blueprint_path=args.blueprint,
                pptx_path=args.pptx,
                assets_root=args.assets_root,
            )
        )
        print(f"pptx={result.pptx_path}")
        print(f"blueprint_log={result.log_path}")
        print(f"slides={result.slide_count}")
        print(f"text_objects={result.text_count}")
        print(f"shape_objects={result.shape_count}")
        print(f"picture_objects={result.picture_count}")
        print(f"line_objects={result.line_count}")
        return 0

    if args.command == "svg-native-rebuild":
        result = rebuild_from_svg_native(
            SvgNativeRebuildConfig(
                src=args.src,
                pptx_path=args.pptx,
                pattern=args.pattern,
                width=args.width,
                height=args.height,
                default_font=args.font,
                default_color=args.color,
            )
        )
        print(f"pptx={result.pptx_path}")
        print(f"svg_native_log={result.log_path}")
        print(f"slides={result.slide_count}")
        print(f"text_objects={result.text_count}")
        print(f"shape_objects={result.shape_count}")
        print(f"picture_objects={result.picture_count}")
        print(f"line_objects={result.line_count}")
        print(f"group_objects={result.group_count}")
        print(f"skipped_objects={result.skipped_count}")
        return 0

    if args.command == "full-rebuild":
        result = run_full_rebuild_pipeline(
            FullRebuildConfig(
                src=args.src,
                out=args.out,
                blueprint_path=args.blueprint,
                blueprint_pptx_path=args.blueprint_pptx,
                assets_root=args.assets_root,
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
        print(f"blueprint_pptx={result.blueprint_pptx_path}")
        print(f"full_rebuild_log={result.full_rebuild_log_path}")
        print(f"ocr_text_blocks={result.expected_text_blocks}")
        print(f"editable_text_boxes={result.actual_text_boxes}")
        print(f"blueprint_text_objects={result.blueprint_text_objects}")
        print(f"blueprint_shape_objects={result.blueprint_shape_objects}")
        print(f"blueprint_picture_objects={result.blueprint_picture_objects}")
        print(f"blueprint_line_objects={result.blueprint_line_objects}")
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
