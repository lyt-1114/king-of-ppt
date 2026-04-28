"""Pixel-exact Image2PPT export helpers."""

from .exporter import ExportConfig, ExportResult, export_exact_deck
from .editable import EditableConfig, OcrConfig, create_editable_text_pptx, extract_ocr_json

__all__ = [
    "EditableConfig",
    "ExportConfig",
    "ExportResult",
    "OcrConfig",
    "create_editable_text_pptx",
    "export_exact_deck",
    "extract_ocr_json",
]
