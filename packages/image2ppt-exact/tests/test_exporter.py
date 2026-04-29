from __future__ import annotations

import base64
import json
import tempfile
import unittest
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

from image2ppt_exact import (
    BlueprintRebuildConfig,
    EditableConfig,
    ExportConfig,
    FullRebuildConfig,
    ImageSvgEditableConfig,
    create_editable_text_pptx,
    export_exact_deck,
    rebuild_from_blueprint,
    run_full_rebuild_pipeline,
    run_image_svg_editable_pipeline,
)
from image2ppt_exact.cli import build_parser
from image2ppt_exact.editable import rapid_result_to_blocks


TINY_PNG = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8"
    "/x8AAwMCAO+/p9sAAAAASUVORK5CYII="
)


class ExporterTests(unittest.TestCase):
    def test_exports_svg_preview_and_log(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "slides"
            out = root / "out"
            src.mkdir()
            (src / "slide_01.png").write_bytes(base64.b64decode(TINY_PNG))

            result = export_exact_deck(
                ExportConfig(src=src, out=out, create_pptx=False)
            )

            self.assertEqual(result.slide_count, 1)
            self.assertTrue((out / "slides_svg" / "slide_01.svg").exists())
            self.assertTrue((out / "index.html").exists())
            self.assertTrue((out / "run-log.md").exists())
            svg = (out / "slides_svg" / "slide_01.svg").read_text(
                encoding="utf-8"
            )
            self.assertIn("data:image/png;base64", svg)

    def test_creates_editable_text_pptx_from_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "slides"
            ocr = root / "ocr"
            src.mkdir()
            ocr.mkdir()
            (src / "slide_01.png").write_bytes(base64.b64decode(TINY_PNG))
            (ocr / "slide_01.json").write_text(
                '{"blocks":[{"text":"Hello","bbox":[0,0,100,40]}]}',
                encoding="utf-8",
            )
            pptx = root / "editable.pptx"

            create_editable_text_pptx(
                EditableConfig(
                    src=src,
                    ocr_dir=ocr,
                    pptx_path=pptx,
                    width=1920,
                    height=1080,
                    background="blank",
                )
            )

            self.assertTrue(pptx.exists())

    def test_editable_routes_default_to_blank_background(self) -> None:
        parser = build_parser()

        editable_args = parser.parse_args(
            [
                "editable",
                "slides",
                "--ocr",
                "ocr",
                "--pptx",
                "editable.pptx",
            ]
        )
        pipeline_args = parser.parse_args(
            ["image-svg-editable", "slides", "--out", "out"]
        )
        full_args = parser.parse_args(["full-rebuild", "slides", "--out", "out"])

        self.assertEqual(EditableConfig(Path("s"), Path("o"), Path("p")).background, "blank")
        self.assertEqual(ImageSvgEditableConfig(Path("s"), Path("out")).background, "blank")
        self.assertEqual(FullRebuildConfig(Path("s"), Path("out")).background, "blank")
        self.assertEqual(editable_args.background, "blank")
        self.assertEqual(pipeline_args.background, "blank")
        self.assertEqual(full_args.background, "blank")

    def test_rapidocr_result_to_blocks(self) -> None:
        blocks = rapid_result_to_blocks(
            [
                (
                    [[1, 2], [11, 2], [11, 8], [1, 8]],
                    "Hello",
                    "0.91",
                )
            ]
        )

        self.assertEqual(blocks[0]["text"], "Hello")
        self.assertEqual(blocks[0]["bbox"], [1.0, 2.0, 10.0, 6.0])
        self.assertAlmostEqual(blocks[0]["confidence"], 0.91)

    def test_default_editable_output_does_not_keep_text_bearing_image_background(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "slides"
            ocr = root / "ocr"
            src.mkdir()
            ocr.mkdir()
            (src / "slide_01.png").write_bytes(base64.b64decode(TINY_PNG))
            (ocr / "slide_01.json").write_text(
                '{"blocks":[{"text":"Hello","bbox":[0,0,100,40]}]}',
                encoding="utf-8",
            )
            pptx = root / "editable.pptx"

            create_editable_text_pptx(
                EditableConfig(src=src, ocr_dir=ocr, pptx_path=pptx)
            )

            prs = Presentation(str(pptx))
            pictures = [
                shape
                for slide in prs.slides
                for shape in slide.shapes
                if shape.shape_type == MSO_SHAPE_TYPE.PICTURE
            ]
            text_boxes = [
                shape
                for slide in prs.slides
                for shape in slide.shapes
                if getattr(shape, "has_text_frame", False) and shape.text.strip()
            ]
            self.assertEqual(len(pictures), 0)
            self.assertEqual(len(text_boxes), 1)

    def test_image_svg_editable_pipeline_with_existing_ocr(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "slides"
            ocr = root / "ocr"
            out = root / "out"
            src.mkdir()
            ocr.mkdir()
            (src / "slide_01.png").write_bytes(base64.b64decode(TINY_PNG))
            (ocr / "slide_01.json").write_text(
                '{"blocks":[{"text":"Hello","bbox":[0,0,100,40]}]}',
                encoding="utf-8",
            )

            result = run_image_svg_editable_pipeline(
                ImageSvgEditableConfig(
                    src=src,
                    out=out,
                    ocr_dir=ocr,
                    width=1920,
                    height=1080,
                    background="blank",
                    force=True,
                )
            )

            self.assertEqual(result.slide_count, 1)
            self.assertEqual(result.expected_text_blocks, 1)
            self.assertEqual(result.actual_text_boxes, 1)
            self.assertTrue((out / "slides_svg" / "slide_01.svg").exists())
            self.assertTrue((out / "editable_text_layer.pptx").exists())
            log = (out / "pipeline-execution-log.md").read_text(encoding="utf-8")
            self.assertIn("SVG output is a pixel-faithful wrapper", log)
            self.assertIn("Editable output is a separate PPTX", log)

    def test_blueprint_rebuild_creates_native_objects(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            blueprint = root / "deck.json"
            pptx = root / "blueprint.pptx"
            blueprint.write_text(
                json.dumps(
                    {
                        "canvas": {"width": 1920, "height": 1080},
                        "theme": {
                            "font": "Microsoft YaHei",
                            "accent": "#01e1d9",
                            "panel_fill": "#163f45",
                        },
                        "slides": [
                            {
                                "background": {"color": "#04191c"},
                                "elements": [
                                    {
                                        "type": "text",
                                        "x": 120,
                                        "y": 100,
                                        "w": 900,
                                        "h": 90,
                                        "text": "High fidelity title",
                                        "font_size": 28,
                                        "bold": True,
                                    },
                                    {
                                        "type": "component",
                                        "name": "panel",
                                        "x": 120,
                                        "y": 260,
                                        "w": 560,
                                        "h": 260,
                                        "title": "Native panel",
                                        "body": "Text, shape, and accent bar are editable.",
                                    },
                                    {
                                        "type": "component",
                                        "name": "chip",
                                        "x": 760,
                                        "y": 260,
                                        "w": 240,
                                        "h": 64,
                                        "text": "Editable chip",
                                    },
                                    {
                                        "type": "line",
                                        "x1": 760,
                                        "y1": 390,
                                        "x2": 1100,
                                        "y2": 390,
                                    },
                                    {
                                        "type": "component",
                                        "name": "footer",
                                        "page": "01",
                                        "label": "Blueprint",
                                    },
                                ],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            result = rebuild_from_blueprint(
                BlueprintRebuildConfig(blueprint_path=blueprint, pptx_path=pptx)
            )

            self.assertTrue(pptx.exists())
            self.assertTrue(result.log_path.exists())
            self.assertEqual(result.slide_count, 1)
            self.assertGreaterEqual(result.text_count, 5)
            self.assertGreaterEqual(result.shape_count, 3)
            self.assertEqual(result.line_count, 1)

    def test_full_rebuild_pipeline_combines_exact_editable_and_blueprint_routes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "slides"
            ocr = root / "ocr"
            out = root / "out"
            src.mkdir()
            ocr.mkdir()
            (src / "slide_01.png").write_bytes(base64.b64decode(TINY_PNG))
            (ocr / "slide_01.json").write_text(
                '{"blocks":[{"text":"Hello","bbox":[0,0,100,40]}]}',
                encoding="utf-8",
            )
            blueprint = root / "deck.blueprint.json"
            blueprint.write_text(
                json.dumps(
                    {
                        "canvas": {"width": 1920, "height": 1080},
                        "slides": [
                            {
                                "background": {"color": "#ffffff"},
                                "elements": [
                                    {
                                        "type": "text",
                                        "x": 120,
                                        "y": 100,
                                        "w": 900,
                                        "h": 90,
                                        "text": "Native rebuild",
                                        "font_size": 28,
                                    }
                                ],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            result = run_full_rebuild_pipeline(
                FullRebuildConfig(
                    src=src,
                    out=out,
                    ocr_dir=ocr,
                    blueprint_path=blueprint,
                    background="blank",
                    force=True,
                )
            )

            self.assertEqual(result.slide_count, 1)
            self.assertTrue((out / "exact_image_deck.pptx").exists())
            self.assertTrue((out / "editable_text_layer.pptx").exists())
            self.assertTrue((out / "high_fidelity_editable.pptx").exists())
            self.assertTrue((out / "full-rebuild-log.md").exists())
            self.assertIsNotNone(result.blueprint_pptx_path)
            self.assertEqual(result.expected_text_blocks, 1)
            self.assertEqual(result.actual_text_boxes, 1)
            log = (out / "full-rebuild-log.md").read_text(encoding="utf-8")
            self.assertIn("Exact proof route", log)
            self.assertIn("Editable text route", log)
            self.assertIn("High-fidelity blueprint route", log)


if __name__ == "__main__":
    unittest.main()
