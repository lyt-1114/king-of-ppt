# image2ppt-exact

`image2ppt-exact` makes the historical Image2PPT handoff reproducible:

```text
full-slide images -> pixel-identical SVG wrappers -> HTML preview + run log -> PPTX
full-slide images -> OCR JSON -> native editable PPT text boxes
```

This package is intentionally honest about the tradeoff. It preserves the approved
render exactly by wrapping each slide image inside an SVG and placing the slide
image full-canvas in the PPTX. It does **not** recover editable text boxes, vector
shapes, or chart objects from a flattened image unless you run the OCR/editable
step and accept that the editable layer is a reconstruction.

## Install

From this package folder:

```bash
pip install -e .
```

For OCR extraction:

```bash
pip install -e .[ocr]
```

## Usage

```bash
image2ppt-exact export path/to/image2_assets/slides --out path/to/svg_exact --force
```

With an explicit PPTX path:

```bash
image2ppt-exact export path/to/slides \
  --out path/to/svg_exact \
  --pptx path/to/final_exact.pptx \
  --title "Approved Image2PPT Deck" \
  --force
```

The output folder contains:

- `slides_svg/slide_XX.svg`: each SVG embeds the matching source image as a
  full-canvas base64 image.
- `index.html`: browser preview for checking the generated SVG deck.
- `run-log.md`: source, output, page count, and limitations.
- `exact_image_deck.pptx`: full-slide image PPTX unless `--no-pptx` is used.

## Editable Text Step

For the exact route you care about, use the verified one-command pipeline:

```bash
image2ppt-exact image-svg-editable path/to/slides \
  --out path/to/rebuild \
  --pptx path/to/rebuild/editable_text_layer.pptx \
  --background keep \
  --force
```

This always performs the same sequence:

```text
slide images -> SVG exact wrappers + preview -> OCR JSON -> native editable PPTX -> verification
```

The command refuses to report success when OCR JSON is missing, contains zero
text blocks, the editable PPTX slide count is wrong, or the generated PPTX has
no editable text boxes. It also writes `pipeline-execution-log.md`, which records
the same decision boundary used in the earlier successful run: SVG is only a
PNG wrapper, editability requires a separate native PPTX reconstruction, the
source image deck is not overwritten, and pixel-identical output cannot be fully
editable at the same time.

## High-Fidelity Blueprint Rebuild

OCR alone is not enough to reproduce a polished editable deck. The successful
high-fidelity Cargill rebuild used native PowerPoint text boxes, shapes, cards,
connectors, footers, and a few image assets. Use `blueprint-rebuild` for that
route:

```bash
image2ppt-exact blueprint-rebuild path/to/deck.blueprint.json \
  --pptx path/to/high_fidelity_editable.pptx \
  --assets-root path/to/assets
```

Blueprint elements are native PPT objects:

```json
{
  "canvas": { "width": 1920, "height": 1080 },
  "theme": {
    "font": "Microsoft YaHei",
    "accent": "#01e1d9",
    "panel_fill": "#163f45"
  },
  "slides": [
    {
      "background": { "color": "#04191c" },
      "elements": [
        {
          "type": "text",
          "x": 120,
          "y": 100,
          "w": 900,
          "h": 90,
          "text": "High fidelity title",
          "font_size": 28,
          "bold": true
        },
        {
          "type": "component",
          "name": "panel",
          "x": 120,
          "y": 260,
          "w": 560,
          "h": 260,
          "title": "Native panel",
          "body": "Text, shape, and accent bar are editable."
        },
        {
          "type": "component",
          "name": "chip",
          "x": 760,
          "y": 260,
          "w": 240,
          "h": 64,
          "text": "Editable chip"
        },
        { "type": "line", "x1": 760, "y1": 390, "x2": 1100, "y2": 390 },
        { "type": "component", "name": "footer", "page": "01", "label": "Blueprint" }
      ]
    }
  ]
}
```

The command also writes `*.blueprint-log.md` with counts for native text,
shape, picture, and line objects. This is the route to use when the target is
close to the earlier `可编辑高还原版.pptx`, not merely an OCR text overlay.

The editable route is split into two reproducible commands.

First, extract one OCR JSON file per slide:

```bash
image2ppt-exact ocr path/to/slides --out path/to/ocr_json --lang ch
```

Then rebuild a PPTX with native PowerPoint text boxes:

```bash
image2ppt-exact editable path/to/slides \
  --ocr path/to/ocr_json \
  --pptx path/to/editable_text_layer.pptx \
  --background keep \
  --font "Microsoft YaHei"
```

`--background keep` preserves the original slide render below the editable text
boxes. `--background blank` creates text-only slides from OCR boxes, which is
useful when you want to manually rebuild the visual layer without duplicated
flattened text.

OCR JSON can also be edited by hand. Each `slide_XX.json` file uses:

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

## Reproduce The Earlier Cargill Flow

From the original working folder, the historical command maps to:

```bash
image2ppt-exact export cargill_wanflow_ppt_output/image2_assets/slides \
  --out cargill_wanflow_ppt_svg_exact_rebuild \
  --pptx cargill_wanflow_ppt_svg_exact_rebuild/exact_image_deck.pptx \
  --title "Cargill Wanflow Image2PPT Exact Export" \
  --force

image2ppt-exact ocr cargill_wanflow_ppt_output/image2_assets/slides \
  --out cargill_wanflow_ppt_svg_exact_rebuild/ocr_json \
  --lang ch

image2ppt-exact editable cargill_wanflow_ppt_output/image2_assets/slides \
  --ocr cargill_wanflow_ppt_svg_exact_rebuild/ocr_json \
  --pptx cargill_wanflow_ppt_svg_exact_rebuild/editable_text_layer.pptx \
  --background keep

image2ppt-exact image-svg-editable cargill_wanflow_ppt_output/image2_assets/slides \
  --out cargill_wanflow_ppt_svg_exact_rebuild \
  --pptx cargill_wanflow_ppt_svg_exact_rebuild/editable_text_layer.pptx \
  --background keep \
  --force
```

## Important Limitation

Putting an SVG into PPT is not the same thing as making the PPT editable. If the
SVG contains a single embedded PNG, PowerPoint can only edit it as an image layer.
For editable decks, rebuild the slide with native PPT text boxes, shapes, lines,
tables, charts, and replaceable images.
