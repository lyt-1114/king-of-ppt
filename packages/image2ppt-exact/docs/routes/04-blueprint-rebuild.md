# Route 4: High-Fidelity Blueprint Rebuild

Use this route when OCR is not enough and the goal is a polished editable PPTX
with native PowerPoint layout objects.

```bash
image2ppt-exact blueprint-rebuild path/to/deck.blueprint.json \
  --pptx path/to/high_fidelity_editable.pptx \
  --assets-root path/to/assets
```

## What It Builds

Blueprint rebuild can create:

- native text boxes
- native rectangle / rounded rectangle / oval shapes
- native connector lines
- picture objects
- reusable `panel` components
- reusable `chip` components
- reusable `footer` components

This route matches the successful high-fidelity editable-deck pattern better
than OCR-only reconstruction because the layout intent is explicit.

## Outputs

- output PPTX
- `*.blueprint-log.md`

The log includes counts for native text, shape, picture, and line objects.

## Example

See:

```text
examples/blueprint.sample.json
```

## When To Use

Use this route when the deck needs cards, dividers, process maps, footer logic,
labels, or other structured design elements that OCR cannot infer reliably.
