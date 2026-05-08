# king-of-ppt

This repository is not a thin PPT prompt wrapper.

It is a two-route presentation system that can do what most PPT skills still cannot do well:

- create premium presentation images and deck systems with real visual judgment
- carry that image-driven quality into editable PowerPoint delivery
- rebuild approved slide images into exact proof output and separate editable PPT results

In practice, this means the repo covers the whole serious workflow from presentation image generation to editable PPT reconstruction. That is the gap most market alternatives never truly close.

## 1. Make PPT with `ultimate-ppt`

<p align="center">
  <img src="docs/readme/hero.svg" alt="Ultimate PPT: Image2PPT-first presentation system" width="94%">
</p>

This hero image summarizes the front half of the system: the repo is designed to turn rough source material into premium presentation output, not just to autocomplete slides.

`ultimate-ppt` is built for users who need decks that look designed, not merely generated.

It does not just fill a template or decorate bullets. It can read references, understand visual grammar, build stronger covers and dense business pages, route the deck toward editable delivery, and keep the output usable for real review, revision, and handoff. Compared with typical PPT skills on the market, this is a much stronger production path: image-driven, strategy-aware, and built for decks that actually need to win.

If you want to call the skill, copy this command into Codex first:

```bash
npx skills add https://github.com/lyt-1114/king-of-ppt
```

Then copy this command into Codex:

```text
Use $ultimate-ppt to create or improve a premium PPT from my notes, screenshots, reference images, or old deck, and keep the final PPTX editable when possible.
```

<p align="center">
  <img src="docs/readme/engine-map.svg" alt="Ultimate PPT engine map" width="92%">
</p>

This map explains why the output quality is stronger than a normal one-shot skill. `ultimate-ppt` works like a system: source reading, visual grammar extraction, route selection, preview logic, and delivery planning all support the final deck instead of leaving the result to prompt luck.

<p align="center">
  <img src="docs/readme/comparison.svg" alt="Typical PPT skill versus Ultimate PPT" width="92%">
</p>

This comparison image is the positioning in one glance: most alternatives stop at "generate pages," while this repo is built to create presentation images, keep business content editable when needed, and survive real delivery and revision.

## How The Full System Works

```mermaid
flowchart TD
    A[Raw inputs<br/>notes, PDFs, screenshots, old decks, reference images] --> B[ultimate-ppt<br/>read source and choose deck route]
    B --> C[Visual grammar extraction<br/>palette, typography, spacing, composition]
    C --> D[Presentation image generation<br/>covers, sections, dense business pages]
    D --> E[Delivery decision<br/>premium visual output plus editable PPT plan]
    E --> F[Approved slide images or image-render deck]
    F --> G[image2ppt-exact full-rebuild]
    G --> H[Exact proof assets<br/>SVG wrappers, exact image deck]
    G --> I[Editable recovery<br/>OCR text layer and editable PPTX]
    G --> J[Optional high-fidelity rebuild<br/>blueprint/native-object reconstruction]
    H --> K[Serious handoff package]
    I --> K
    J --> K
```

This diagram is the core thesis of the repo. Most products can help with one isolated step, but `king-of-ppt` covers the whole path: generate stronger presentation imagery first, then carry that quality forward into exact proof output and editable PowerPoint reconstruction.

## 2. Convert to Editable PPT with `image2ppt-exact`

<p align="center">
  <img src="docs/readme/workflow.svg" alt="Image2PPT workflow" width="92%">
</p>

This workflow image explains the back half of the system: once a slide image set is approved, `image2ppt-exact` can preserve the exact visual result, recover editable layers, and move toward high-fidelity rebuild instead of collapsing everything into a flat screenshot deck.

`image2ppt-exact` is the route that makes this repository unusually powerful.

Most tools that claim image-to-PPT conversion stop at screenshots on slides, rough OCR overlays, or vague promises of editability. This package goes much further: it can preserve approved slide images as exact proof output, recover editable text layers, and drive toward high-fidelity editable rebuilds. That means it is not just "image import" and not just "OCR extraction" either. It is a serious bridge from approved presentation imagery to usable editable PowerPoint output, which is exactly where most competing skills fail.

If you want to call the skill, copy this command into Codex first:

```bash
npx skills add https://github.com/lyt-1114/king-of-ppt
```

Then copy this command into Codex:

```text
Use $image2ppt-exact full-rebuild to turn my approved slide-image folder into exact proof assets and an editable PPTX rebuild.
```
