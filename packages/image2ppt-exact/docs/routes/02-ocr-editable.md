# Route 2: OCR Editable Text

Use this route when you already have slide images and want editable PowerPoint text boxes.

## Flow

1. Extract OCR JSON from slide images
2. Optionally apply spec correction
3. Build an editable PPTX from the OCR JSON

## Commands

```bash
image2ppt-exact ocr path/to/slides \
  --out path/to/ocr_json \
  --lang ch

image2ppt-exact editable path/to/slides \
  --ocr path/to/ocr_json \
  --pptx path/to/editable_text_layer.pptx \
  --background blank
```

## What This Route Gives You

- editable text boxes
- optional background redaction for duplicate-text avoidance
- OCR JSON you can manually fix and rerun

## Spec Correction

If you already know the intended text, pass a spec file:

```bash
image2ppt-exact editable path/to/slides \
  --ocr path/to/ocr_json \
  --pptx path/to/editable_text_layer.pptx \
  --spec-file path/to/expected_text.txt
```

This helps when OCR is close but not exact.

## Manual Rerun Loop

1. Generate OCR JSON once
2. Edit `slide_XX.json` by hand if needed
3. Rerun `editable` with the same OCR folder

If you changed `bbox` and use `--background redact`, rerun the rebuild so the cleaned background matches the corrected boxes.

## Limitation

This route restores text, not full layout intelligence. For polished native-object reconstruction, use the blueprint route.

