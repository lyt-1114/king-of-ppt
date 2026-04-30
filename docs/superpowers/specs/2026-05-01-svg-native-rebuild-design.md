# SVG Native Rebuild Design

## Goal

Add a native editable SVG rebuild route to `packages/image2ppt-exact` so a structured SVG deck can be converted into a PowerPoint deck made of editable text boxes, shapes, lines, pictures, and groups.

## Context

`image2ppt-exact` already has a reliable image-first baseline:

- exact image export for pixel-faithful proof decks
- OCR extraction and editable text boxes
- blueprint rebuild for manually described native objects
- full rebuild logs that report object counts

The current gap is between OCR text recovery and high-fidelity native object recovery. OCR alone cannot recover panels, lines, diagrams, shapes, visual hierarchy, or reusable layout structure. The blueprint route can recover those objects, but it requires a JSON object model to be written first.

`ppt-master` solves a related problem by treating SVG as the semantic layout layer and converting SVG primitives into PowerPoint DrawingML. That is the part worth borrowing: if a slide is represented as structured SVG, the SVG can be rebuilt as editable PPT objects instead of being inserted as one flat image.

## Proposed Route

Add a new route:

```text
structured SVG folder -> native DrawingML PPTX -> rebuild log
```

Command:

```bash
image2ppt-exact svg-native-rebuild path/to/svg_slides --pptx path/to/native_editable.pptx
```

Default source pattern:

```text
slide_*.svg
```

The route does not replace existing image routes. It becomes the high-fidelity native object route when the system can produce or receive structured SVG.

## Architecture

Create a focused module, `native_svg.py`, inside `src/image2ppt_exact`.

Responsibilities:

- collect SVG files in natural order
- parse SVG XML
- read canvas size from `viewBox`, `width`, and `height`
- convert core SVG elements into native PowerPoint objects using `python-pptx`
- write a log with slide count and native object counts

Supported first-pass SVG features:

- `rect`
- `circle`
- `ellipse`
- `line`
- `polyline`
- `polygon`
- `path` as a freeform object for simple `M/L/H/V/Z` paths
- `text` and direct `tspan` text
- `image` for external files and base64 data URIs
- `g` groups as recursive containers
- inline style and direct attributes for fill, stroke, stroke width, opacity, font, alignment, and rotation

Deliberately out of scope for the first pass:

- automatic image-to-SVG vision extraction
- full SVG CSS cascade
- complex Bezier path reconstruction
- gradients and filters
- charts
- animation
- exact pixel comparison

These can be added later without changing the route boundary.

## Data Flow

1. User supplies a folder of structured SVG slides.
2. CLI resolves the files with natural sort.
3. The first SVG determines the PowerPoint canvas.
4. Each SVG becomes one slide.
5. Each supported SVG element becomes a native PPT object.
6. Unsupported visual elements are skipped and counted in the log.
7. The route saves the PPTX and a `*.svg-native-log.md` file.

## Verification

Tests should prove:

- SVG files are discovered in natural order.
- A simple SVG creates editable PPT text and native shape objects.
- Inline data URI images are extracted and inserted as pictures.
- The CLI exposes `svg-native-rebuild`.
- A log records slide count and native object counts.

## User-Facing Boundary

This route only makes SVG decks editable when the SVG itself is structured. An SVG that embeds one full-slide PNG remains an image wrapper and cannot magically become native editable objects. For image-only sources, the existing exact proof and OCR text routes remain necessary.
