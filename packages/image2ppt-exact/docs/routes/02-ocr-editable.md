# Route 2: OCR Editable Text

Use this route when you have slide images and want a PPTX containing editable
PowerPoint text boxes.

## Step 1: Extract OCR JSON

```bash
image2ppt-exact ocr path/to/slides \
  --out path/to/ocr_json \
  --lang ch
```

This writes one JSON file per slide:

```text
ocr_json/slide_01.json
ocr_json/slide_02.json
...
```

## Step 2: Build Editable PPTX

```bash
image2ppt-exact editable path/to/slides \
  --ocr path/to/ocr_json \
  --pptx path/to/editable_text_layer.pptx \
  --background blank
```

`--background blank` creates a text-only PPTX and is the safe default.
`--background keep` keeps the slide image under the editable text boxes. Use it
only for visual debugging or when the slide images are already text-free;
otherwise duplicate text is expected.

## OCR JSON Shape

```json
{
  "blocks": [
    {
      "text": "Editable text",
      "bbox": [120, 90, 420, 48],
      "font_size": 22,
      "color": "#111827",
      "bold": false,
      "align": "left"
    }
  ]
}
```

OCR JSON is intentionally editable by hand. This makes it possible to correct
recognition errors or tune positions before generating the PPTX.

## Limitation

OCR can recover text and approximate boxes. It does not understand card layout,
connectors, section dividers, icon logic, fonts, colors, or visual hierarchy.
For a polished editable deck, use the blueprint rebuild route.
