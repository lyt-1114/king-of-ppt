# Route 1: Exact Export

Use this route when the approved deck already exists as full-slide images and
the priority is pixel-level reproduction.

```bash
image2ppt-exact export path/to/slides \
  --out path/to/exact_export \
  --pptx path/to/exact_export/exact_image_deck.pptx \
  --force
```

## What It Does

```text
slide_XX.png -> slide_XX.svg -> HTML preview -> exact image PPTX
```

Each SVG embeds one full-slide bitmap as a base64 data URI. This is useful for
archival, preview, and exact proof assets.

## Outputs

- `slides_svg/slide_XX.svg`
- `index.html`
- `run-log.md`
- `exact_image_deck.pptx`

## Limitation

This route does not recover native PowerPoint text boxes, shapes, charts, or
tables. If the SVG wraps a PNG, PowerPoint can only edit it as an image layer.
