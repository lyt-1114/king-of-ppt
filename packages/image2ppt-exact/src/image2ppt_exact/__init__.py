"""Pixel-exact Image2PPT export helpers."""

from .exporter import ExportConfig, ExportResult, export_exact_deck
from .editable import EditableConfig, OcrConfig, create_editable_text_pptx, extract_ocr_json
from .pipeline import (
    ImageSvgEditableConfig,
    ImageSvgEditableResult,
    run_image_svg_editable_pipeline,
)

__all__ = [
    "EditableConfig",
    "ExportConfig",
    "ExportResult",
    "ImageSvgEditableConfig",
    "ImageSvgEditableResult",
    "OcrConfig",
    "create_editable_text_pptx",
    "export_exact_deck",
    "extract_ocr_json",
    "run_image_svg_editable_pipeline",
]
