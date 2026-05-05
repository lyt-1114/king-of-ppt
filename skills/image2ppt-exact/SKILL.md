---
name: image2ppt-exact
description: Use when converting approved full-slide images into exact SVG/PPTX proof assets, OCR-based editable text PPTX files, full-rebuild pipelines, or high-fidelity editable PowerPoint rebuilds using blueprint JSON with native text boxes, shapes, lines, pictures, panels, chips, and footers.
---

# Image2PPT Exact

This directory is the skill entry point.

The runnable Python implementation lives in `packages/image2ppt-exact`.

Use this skill for the reproducible handoff route. Prefer the full rebuild route when the user wants the strongest end-to-end conversion:

```text
approved slide images
-> exact SVG wrappers / exact image PPTX
-> OCR JSON / editable text PPTX
-> optional structured SVG / native editable PPTX
-> optional blueprint JSON / high-fidelity editable PPTX
-> unified full-rebuild log
```

## Core Boundary

- SVG files produced by this route are usually PNG wrappers. They are pixel-faithful, but not editable as native PPT text or shapes.
- Structured SVG files can be rebuilt as native editable PPT objects with `svg-native-rebuild`.
- Editable PPTX output must be rebuilt as native PowerPoint objects.
- OCR-only output gives editable text boxes, not a polished high-fidelity deck.
- Use `--background redact` when keeping the visual background while overlaying OCR text. It clears OCR text regions from the background image before adding editable text boxes, preventing duplicate text.
- Use OCR filtering when slide images contain screenshots, charts, dashboard panels, or small labels that should stay in the bitmap background:
  - `--min-text-height 30` skips OCR blocks shorter than 30 source-image pixels.
  - `--min-text-area 900` skips OCR blocks whose bounding box is smaller than 900 source-image square pixels.
  - `--lock-file ocr-locks.json` skips OCR blocks intersecting user-defined locked regions.
  - Skipped blocks are not converted to editable text boxes and are not redacted from the background.
- Do not keep source images as editable backgrounds unless they are already text-free. Keeping text-bearing slide images under OCR text creates duplicate text.
- For decks similar to a successful high-fidelity editable rebuild, use `full-rebuild` with `--blueprint` so the exact proof, editable text layer, high-fidelity rebuild, and verification log are produced together.

## Package Setup

Prefer the local package when working inside this repository:

```bash
cd packages/image2ppt-exact
pip install -e .
```

For OCR extraction:

```bash
pip install -e .[ocr]
```

If the repository package is not local, install from GitHub:

```bash
pip install "git+https://github.com/lyt-1114/king-of-ppt.git#subdirectory=packages/image2ppt-exact"
```

## Route Selection

Use `full-rebuild` as the default route when the user asks for a complete conversion. Use the lower-level routes only when debugging or when the user explicitly wants one output layer.

| Need | Route | Command |
| --- | --- | --- |
| Complete exact proof + editable text + optional high-fidelity rebuild | Full rebuild | `image2ppt-exact full-rebuild` |
| Pixel-faithful proof of approved image deck | Exact export | `image2ppt-exact export` |
| Editable text boxes from slide images | OCR editable text | `image2ppt-exact ocr` then `image2ppt-exact editable` |
| One-command verified image -> SVG -> editable text flow | Verified pipeline | `image2ppt-exact image-svg-editable` |
| Structured SVG slides into editable objects | SVG native rebuild | `image2ppt-exact svg-native-rebuild` |
| Polished high-fidelity editable deck | Blueprint rebuild | `image2ppt-exact blueprint-rebuild` |

## Recommended Route: Full Rebuild

```bash
image2ppt-exact full-rebuild path/to/slides \
  --out path/to/rebuild \
  --blueprint path/to/deck.blueprint.json \
  --assets-root path/to/assets \
  --background redact \
  --min-text-height 30 \
  --min-text-area 900 \
  --lock-file path/to/ocr-locks.json \
  --force
```

This route runs the layers together:

- exact SVG wrappers, HTML preview, and exact image PPTX
- OCR JSON and editable text PPTX
- optional high-fidelity native-object PPTX when `--blueprint` is provided
- `full-rebuild-log.md` with the output paths, slide count, OCR text count, editable text box count, and blueprint object counts
- OCR filter counts showing how many blocks were skipped by height, area, or lock regions

If `--blueprint` is omitted, still run `full-rebuild` for the exact proof and editable text layer, but report that the high-fidelity native-object rebuild was skipped.

## Route 1: Exact Export

```bash
image2ppt-exact export path/to/slides \
  --out path/to/exact_export \
  --pptx path/to/exact_export/exact_image_deck.pptx \
  --force
```

Outputs include `slides_svg/`, `index.html`, `run-log.md`, and optionally an exact image PPTX.

## Route 2: OCR Editable Text

```bash
image2ppt-exact ocr path/to/slides \
  --out path/to/ocr_json \
  --lang ch

image2ppt-exact editable path/to/slides \
  --ocr path/to/ocr_json \
  --pptx path/to/editable_text_layer.pptx \
  --background blank \
  --min-text-height 30 \
  --min-text-area 900 \
  --lock-file path/to/ocr-locks.json
```

Use `--background keep` only for visual debugging or when the source images have already had text removed.

Lock file format:

```json
{
  "regions": [
    { "x": 40, "y": 820, "w": 1840, "h": 120 }
  ],
  "slides": {
    "slide_003": [
      { "x": 900, "y": 120, "w": 760, "h": 520 }
    ]
  }
}
```

`regions` applies to every slide. `slides` keys match the slide image stem, such as `slide_003` for `slide_003.png`. Coordinates use the source image pixel space.

## Route 3: Verified Image SVG Editable Pipeline

```bash
image2ppt-exact image-svg-editable path/to/slides \
  --out path/to/rebuild \
  --pptx path/to/rebuild/editable_text_layer.pptx \
  --background blank \
  --force
```

This writes `pipeline-execution-log.md` and refuses success when OCR JSON is missing, has zero text blocks, slide count mismatches, or the generated PPTX has no editable text boxes.

## Route 4: SVG Native Rebuild

```bash
image2ppt-exact svg-native-rebuild path/to/svg_slides \
  --pptx path/to/native_editable.pptx
```

Use this route when the input is structured SVG, not a one-image SVG wrapper.
It rebuilds supported SVG primitives as native PowerPoint objects:

- text
- rectangles, circles, ellipses
- lines, polylines, polygons, simple paths
- image elements
- recursive groups

The route writes `*.svg-native-log.md` with slide count and native object
counts. It is the closest package route to `ppt-master`'s SVG-to-DrawingML
idea, while staying inside this package's `python-pptx` architecture.

## Route 5: High-Fidelity Blueprint Rebuild

```bash
image2ppt-exact blueprint-rebuild path/to/deck.blueprint.json \
  --pptx path/to/high_fidelity_editable.pptx \
  --assets-root path/to/assets
```

Use this route for native PPT reconstruction with explicit objects:

- text boxes
- shapes
- connector lines
- pictures
- `panel`, `chip`, and `footer` components

This route is closest to a manually/rule-rebuilt high-fidelity editable PPTX. It writes `*.blueprint-log.md` with counts for native text, shape, picture, and line objects.

## Verification

Before reporting success, run at least one relevant check:

```bash
python -m unittest discover -s packages/image2ppt-exact/tests
image2ppt-exact --help
image2ppt-exact svg-native-rebuild --help
```

For a real output, inspect the generated log:

- `full-rebuild-log.md` for the recommended full rebuild route
- `run-log.md` for exact export
- `pipeline-execution-log.md` for image-svg-editable
- `*.svg-native-log.md` for SVG native rebuild
- `*.blueprint-log.md` for blueprint rebuild

Report the slide count and editable object counts when available.
