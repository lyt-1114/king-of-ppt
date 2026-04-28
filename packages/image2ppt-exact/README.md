# image2ppt-exact

Reproducible routes for the historical Image2PPT handoff:

```text
approved slide images
  -> exact SVG wrappers / exact image PPTX
  -> OCR JSON / editable text PPTX
  -> optional high-fidelity blueprint rebuild
```

The package is intentionally split into routes because these goals are different:

| Route | Command | Best For | Output |
| --- | --- | --- | --- |
| Exact export | `export` | Pixel-faithful proof of an approved image deck | SVG wrappers, HTML preview, exact image PPTX |
| OCR editable text | `ocr` + `editable` | Recovering editable text boxes from slide images | OCR JSON, native PPT text boxes |
| Verified image route | `image-svg-editable` | Running the approved image -> SVG -> editable text flow in one command | Exact assets, editable PPTX, execution log |
| High-fidelity rebuild | `blueprint-rebuild` | Rebuilding polished editable decks with native layout objects | PPT text, shapes, lines, pictures, panels, chips, footers |
| Full rebuild | `full-rebuild` | Running exact proof, editable text, optional blueprint rebuild, and verification together | Exact PPTX, editable text PPTX, optional high-fidelity PPTX, unified log |

Important boundary:

```text
SVG containing one embedded PNG is still an image.
It is pixel-faithful, but it is not editable as native PowerPoint text/shapes.
```

For a deck like the earlier high-fidelity editable Cargill version, use
`blueprint-rebuild`, not OCR alone.

## Install

From this package folder:

```bash
pip install -e .
```

For OCR extraction:

```bash
pip install -e .[ocr]
```

## Quick Start

Exact proof route:

```bash
image2ppt-exact export path/to/slides --out path/to/exact_export --force
```

Verified image -> SVG -> editable text route:

```bash
image2ppt-exact image-svg-editable path/to/slides \
  --out path/to/rebuild \
  --pptx path/to/rebuild/editable_text_layer.pptx \
  --background keep \
  --force
```

High-fidelity blueprint route:

```bash
image2ppt-exact blueprint-rebuild examples/blueprint.sample.json \
  --pptx path/to/high_fidelity_editable.pptx \
  --assets-root examples
```

Full rebuild route:

```bash
image2ppt-exact full-rebuild path/to/slides \
  --out path/to/rebuild \
  --blueprint examples/blueprint.sample.json \
  --assets-root examples \
  --force
```

If `--blueprint` is omitted, `full-rebuild` still creates the exact proof deck
and editable text layer, then records that the high-fidelity native-object PPTX
was skipped because no blueprint was provided.

## Documentation

- [Exact export](docs/routes/01-exact-export.md)
- [OCR editable text](docs/routes/02-ocr-editable.md)
- [Verified image SVG editable pipeline](docs/routes/03-image-svg-editable.md)
- [High-fidelity blueprint rebuild](docs/routes/04-blueprint-rebuild.md)
- [Blueprint schema](docs/blueprint-schema.md)

## Outputs

Depending on the route, the package writes:

- `slides_svg/slide_XX.svg`
- `index.html`
- `run-log.md`
- `exact_image_deck.pptx`
- `ocr_json/slide_XX.json`
- `editable_text_layer.pptx`
- `pipeline-execution-log.md`
- `high_fidelity_editable.pptx`
- `full-rebuild-log.md`
- `*.blueprint-log.md`

## Validate

```bash
python -m unittest discover -s tests
image2ppt-exact --help
image2ppt-exact full-rebuild --help
image2ppt-exact blueprint-rebuild --help
```

## Source Layout

```text
src/image2ppt_exact/exporter.py    # exact image/SVG/PPTX export
src/image2ppt_exact/editable.py    # OCR JSON and editable text PPTX
src/image2ppt_exact/pipeline.py    # verified image-svg-editable route
src/image2ppt_exact/blueprint.py   # high-fidelity native object rebuild
src/image2ppt_exact/cli.py         # command-line entry point
tests/                             # route smoke tests
docs/routes/                       # per-route docs
examples/                          # sample JSON inputs
```
