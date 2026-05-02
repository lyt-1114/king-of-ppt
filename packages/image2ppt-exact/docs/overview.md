# image2ppt-exact Overview

`image2ppt-exact` turns slide images into deliverable PPTX files.

Default path:

```bash
image2ppt-exact full-rebuild path/to/slides --out path/to/rebuild --force
```

## What You Get

- `exact`: pixel-faithful proof output
- `editable`: OCR-backed editable text layer
- `blueprint`: native-object rebuild when you need higher fidelity

## Common Options

- `--background redact`: remove text regions from the background before overlaying editable text
- `--spec-file`: correct OCR text from an expected-text list
- `--blueprint`: enable high-fidelity native-object rebuild

## Output

```text
rebuild/
  exact_image_deck.pptx
  ocr_json/
  editable_text_layer.pptx
  full-rebuild-log.md
```

If `--blueprint` is provided:

```text
rebuild/
  high_fidelity_editable.pptx
  high_fidelity_editable.blueprint-log.md
```

## When To Look Deeper

- OCR text recovery and manual rerun: use `full-rebuild` or `ocr` plus `editable`
- Native object rebuild: use `blueprint-rebuild`
- Exact proof export: use `export`
- Verified image -> SVG -> editable flow: use `image-svg-editable`

## Install

```bash
cd packages/image2ppt-exact
pip install -e .
pip install -e .[ocr]
```

## Related Reference

- Blueprint schema: [docs/blueprint-schema.md](docs/blueprint-schema.md)

