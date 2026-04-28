---
name: image2ppt-exact
description: Use when converting approved full-slide images into exact SVG/PPTX proof assets, OCR-based editable text PPTX files, or high-fidelity editable PowerPoint rebuilds using blueprint JSON with native text boxes, shapes, lines, pictures, panels, chips, and footers.
---

# Image2PPT Exact

Use this skill for the reproducible handoff route:

```text
approved slide images -> exact SVG wrappers / exact image PPTX
approved slide images -> OCR JSON -> editable text PPTX
blueprint JSON -> high-fidelity editable PPTX
```

## Core Boundary

- SVG files produced by this route are usually PNG wrappers. They are pixel-faithful, but not editable as native PPT text or shapes.
- Editable PPTX output must be rebuilt as native PowerPoint objects.
- OCR-only output gives editable text boxes, not a polished high-fidelity deck.
- For decks similar to a successful high-fidelity editable rebuild, use `blueprint-rebuild` with explicit layout objects.

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

Choose exactly one primary route before running commands:

| Need | Route | Command |
| --- | --- | --- |
| Pixel-faithful proof of approved image deck | Exact export | `image2ppt-exact export` |
| Editable text boxes from slide images | OCR editable text | `image2ppt-exact ocr` then `image2ppt-exact editable` |
| One-command verified image -> SVG -> editable text flow | Verified pipeline | `image2ppt-exact image-svg-editable` |
| Polished high-fidelity editable deck | Blueprint rebuild | `image2ppt-exact blueprint-rebuild` |

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
  --background keep
```

Use `--background blank` when the deck should contain only reconstructed editable text.

## Route 3: Verified Image SVG Editable Pipeline

```bash
image2ppt-exact image-svg-editable path/to/slides \
  --out path/to/rebuild \
  --pptx path/to/rebuild/editable_text_layer.pptx \
  --background keep \
  --force
```

This writes `pipeline-execution-log.md` and refuses success when OCR JSON is missing, has zero text blocks, slide count mismatches, or the generated PPTX has no editable text boxes.

## Route 4: High-Fidelity Blueprint Rebuild

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
```

For a real output, inspect the generated log:

- `run-log.md` for exact export
- `pipeline-execution-log.md` for image-svg-editable
- `*.blueprint-log.md` for blueprint rebuild

Report the slide count and editable object counts when available.
