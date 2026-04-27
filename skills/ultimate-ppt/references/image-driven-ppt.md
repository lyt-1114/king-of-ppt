# Image-Driven PPT Guide

Use this when a deck needs richer visual scenes, image-to-PPT style transfer, generated hero images, reference-PDF look matching, or case pages that feel more designed than text cards.

## Core Principle

Use images to carry atmosphere, scene, and memory; keep claims, metrics, charts, and key labels as editable PPT objects.

Do not turn a serious business deck into a stack of flattened posters unless the user explicitly asks for non-editable image slides. The best default is hybrid:

- bitmap image layer: cover scene, chapter atmosphere, product/case scene, screenshot frame, paper texture
- editable PPT layer: title, subtitle, claim, metrics, evidence blocks, diagrams, sources
- validation layer: overlap audit, font-size audit, contrast/readability check, asset relevance check

For end-to-end image2 work, load `image2-deck-workflow.md` and leave a traceable image2 brief, visual grammar, transfer level, and editable/bitmap layer split.

Every image should be assigned a role before generation or selection:

- cover hero
- section divider
- concept visualization
- comparison plate
- data backdrop
- system/workflow plate
- case scene
- closing poster

If the role is unclear, the image is probably decoration.

## When To Use Image-Driven Layouts

Choose this route when:

- the user says the deck is ugly, plain, abrupt, not premium, or lacks case-showcase quality
- the user provides a PDF, screenshot, poster, website, or PPT as a style reference
- the topic benefits from visual storytelling: product vision, industry cases, architecture scenes, customer journeys
- the deck needs cover, divider, case, or keynote pages with stronger emotional memory

Avoid this route when:

- the user needs dense editable tables or legal/financial documentation
- exact brand/product screenshots are required but unavailable
- image generation would create misleading evidence or fake UI/product claims

## Image-To-PPT Style Transfer Workflow

1. Inspect the reference image/PDF/PPT:
   - palette and contrast
   - type hierarchy
   - page composition
   - motif and texture
   - card/grid rhythm
   - image-to-text ratio
   - what must stay editable
   - which pages are intentionally similar and which pages vary
   - recognition assets: logo, product image, UI screenshot, brand colors, typography clues
2. Extract a design recipe:
   - 2-3 palette colors plus 1 accent
   - title/body/metadata sizes
   - 3-5 reusable page archetypes
   - image treatment: full-bleed, split image, framed screenshot, vignette, texture, or cutout
   - a repetition budget: which motif may repeat, and which layout must change
   - a transfer level: faithful, inspired, upgraded, or hybrid
3. Build a hybrid slide system:
   - reserve stable text zones before placing images
   - use images outside or behind non-critical zones
   - keep contrast panels subtle but real when text overlays imagery
   - add editable callouts and metrics on top of images
   - vary layout primitives across pages: hero, comparison, module map, process strip, case storyboard, scorecard, roadmap
4. Verify:
   - text remains readable in slide sorter
   - meaningful text remains editable
   - images do not imply unsupported facts
   - no text overlaps image-heavy decoration
   - slide sorter does not show a run of near-identical pages with only swapped titles
   - `image2-brief.md`, `visual-grammar.md`, and `run-log.md` or equivalent sections record what was extracted and why

## Image2 Artifact Checklist

For serious image2 decks, include:

- `image2-brief.md`: sources, source type, audience, goal, output, must-editable layer, bitmap layer, missing assets, risks
- `visual-grammar.md`: palette, type hierarchy, composition, spacing, image treatment, diagram/chart language, footer behavior
- `strategy-lock.md`: transfer level, slide list, output path, acceptance checks
- `execution-lock.md`: canvas, margins, colors, fonts, icons, image inventory, page rhythm, forbidden moves
- `run-log.md`: sources read, two-page pass result, audit command, limitations

Run `scripts/audit_deck.py <output> --image2` when available.

## Generated Image Prompt Pattern

Use one prompt per asset. Do not ask a single image to solve the whole deck.

```text
Create a [image role] for a presentation.
Slide thesis: [one sentence].
Audience/context: [who will see it and why].
Composition: one dominant focal point, one support layer, clean [left/right/top] text-safe zone.
Style direction: [deck visual grammar or brand-inspired cues].
Palette: [base, accent, neutral].
Texture/depth: [paper, metal, ink, glass, studio light, grain].
Text in image: none or only [short label / numeral / marker].
Avoid: stock office scenes, generic AI glow, unreadable labels, fake dashboards, clutter, watermark.
16:9 horizontal, presentation-first, strong thumbnail readability.
```

For WanFlow-style enterprise AI decks, useful image assets include:

- enterprise AI operations control room where data streams, workflow nodes, human review gates, and agent tasks converge
- finance review workflow scene with document intake, risk gate, evidence trail, and approval status
- manufacturing exception command view with inventory nodes, dispatch route, and escalation path
- retail operations review scene with campaign metrics, customer feedback, logistics status, and same-day recap
- abstract execution-chain visual: data, process, agent, human gate, evaluation loop

Default image spec:

- horizontal 16:9
- 3840x2160 preferred, 1920x1080 acceptable
- one dominant focal point
- 25-35% clean text-safe space
- meaningful content inside the central 80%
- minimal or no baked-in text

## Layout Patterns

### Cover Hero

- image occupies 45-60% of canvas
- title area is clean and editable
- one subtitle and one purpose line only
- no dense cards on cover

### Case Showcase

- top: claim headline
- center: one visual scene or workflow image
- side or bottom: situation, intervention, result
- proof goes on a second slide when metrics need room
- for image-to-PPT decks, use storyboard structure instead of repeated cards: scenario cue, process path, result proof, reusable asset

### Architecture Scene

- use a generated or drawn background to imply system depth
- keep the actual architecture labels editable
- avoid tiny layer names inside the bitmap

### Divider / Chapter

- use full-bleed or half-bleed visual atmosphere
- include one large chapter claim, not a list of contents

### Evidence Page

- image is secondary or absent
- use large metrics, clean cards, and source notes
- do not sacrifice readability for decoration

## Guardrails

- Never rely on generated in-image text for core content; it is often inaccurate and not editable.
- Do not use fake screenshots as proof. If it is conceptual, label it as conceptual or keep it abstract.
- Keep important text outside busy image areas.
- Do not use more than one dominant image treatment on the same slide.
- Use the same color grade across generated images so the deck feels like one system.
- Do not repeat the same generated panel, node chart, or card grid across multiple slides with only different headings. That reads as batch output, not design.
- If three consecutive slides share the same layout skeleton, redesign at least one as a visual spread, process strip, comparison, or scorecard.
- In reference-driven decks, repeat small motifs such as palette, page number chip, wave footer, ghost character, icon line, and value bar; vary the central composition.
- If file size matters, compress images after generation but before final PPTX delivery.
- Final output can still be a single PPTX; temporary image assets should be embedded and cleaned up unless the user asks to keep them.
