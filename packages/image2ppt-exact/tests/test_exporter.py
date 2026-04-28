from __future__ import annotations

import base64
import tempfile
import unittest
from pathlib import Path

from image2ppt_exact import (
    EditableConfig,
    ExportConfig,
    create_editable_text_pptx,
    export_exact_deck,
)


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


if __name__ == "__main__":
    unittest.main()
