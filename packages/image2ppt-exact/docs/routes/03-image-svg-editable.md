# Route 3: Verified Image SVG Editable Pipeline

Use this route when you want the historical image -> SVG -> editable PPTX flow
as a single reproducible command with verification.

```bash
image2ppt-exact image-svg-editable path/to/slides \
  --out path/to/rebuild \
  --pptx path/to/rebuild/editable_text_layer.pptx \
  --background keep \
  --force
```

## What It Does

```text
slide images
  -> SVG wrappers and exact preview
  -> OCR JSON
  -> editable text PPTX
  -> slide-count and editable-text checks
```

## Safety Checks

The command refuses to report success when:

- OCR JSON files are missing
- OCR JSON contains zero text blocks
- editable PPTX slide count does not match the source images
- editable PPTX contains no editable text boxes

## Execution Log

The route writes:

```text
pipeline-execution-log.md
```

That log records the key boundary:

- SVG is a bitmap wrapper
- editability requires a separate native PPTX reconstruction
- source image deck is not overwritten
- exact pixel reproduction and full native editability are different goals

## Limitation

This route verifies that the editable text layer exists. It does not make a
polished high-fidelity business deck by itself. For that, use
`blueprint-rebuild`.
