"""Pixel-exact Image2PPT export helpers."""

from .blueprint import BlueprintRebuildConfig, BlueprintRebuildResult, rebuild_from_blueprint
from .exporter import ExportConfig, ExportResult, export_exact_deck
from .editable import (
    EditableBuildResult,
    EditableConfig,
    EditableFilterStats,
    OcrConfig,
    collect_editable_blocks,
    create_editable_text_pptx,
    create_editable_text_pptx_with_stats,
    extract_ocr_json,
    load_ocr_locks,
)
from .pipeline import (
    ImageSvgEditableConfig,
    ImageSvgEditableResult,
    run_image_svg_editable_pipeline,
)
from .full_rebuild import (
    FullRebuildConfig,
    FullRebuildResult,
    run_full_rebuild_pipeline,
)
from .native_svg import (
    SvgNativeRebuildConfig,
    SvgNativeRebuildResult,
    rebuild_from_svg_native,
)

__all__ = [
    "BlueprintRebuildConfig",
    "BlueprintRebuildResult",
    "EditableBuildResult",
    "EditableConfig",
    "EditableFilterStats",
    "ExportConfig",
    "ExportResult",
    "FullRebuildConfig",
    "FullRebuildResult",
    "ImageSvgEditableConfig",
    "ImageSvgEditableResult",
    "OcrConfig",
    "SvgNativeRebuildConfig",
    "SvgNativeRebuildResult",
    "collect_editable_blocks",
    "create_editable_text_pptx",
    "create_editable_text_pptx_with_stats",
    "export_exact_deck",
    "extract_ocr_json",
    "load_ocr_locks",
    "rebuild_from_blueprint",
    "rebuild_from_svg_native",
    "run_full_rebuild_pipeline",
    "run_image_svg_editable_pipeline",
]
