# Presentation Image System

Use this when generating or selecting images for covers, dividers, case pages, concept visuals, data backdrops, or brand-inspired slides.

## Core Principle

A presentation image is not decoration. It is a slide argument.

It should strengthen one slide thesis, leave room for editable text, and remain readable in live presentation, PDF export, and thumbnail view.

## Default Image Spec

Unless the user asks otherwise:

- aspect ratio: 16:9 horizontal
- target size: 3840x2160 or higher when possible
- one dominant focal point
- 25-35% clean text-safe space
- minimal or no baked-in text
- important content inside the central 80% of the frame
- no watermarks or fake UI proof

## Image Roles

| Role | Purpose | Density |
| --- | --- | --- |
| cover hero | establish the deck conflict or promise | strongest |
| section divider | reset rhythm | simpler than cover |
| concept visual | explain one abstract idea | medium |
| comparison plate | show tension/tradeoff/before-after | medium |
| data backdrop | support chart or metric | calm |
| system plate | show flow or architecture | structured |
| case scene | make a scenario memorable | medium |
| closing poster | resolve the deck emotionally | simple |

Choose role per slide. Do not use one image style for every page.

## Prompt Skeleton

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

## Brand-Inspired Translation

When a brand or style reference is involved, extract cues before prompting:

- recognition assets: logo, product image, UI screenshot, official render, or other real identity carrier
- mood: what the brand feels like
- palette: base, accent, neutral
- typography voice: geometric, serif, mono, editorial, humanist
- spacing: dense, spacious, cinematic, grid-heavy
- shape language: radius, lines, cards, pills, frames
- depth: flat, soft shadow, glass, product photography, paper texture
- signature restraint: what the brand refuses to do

Then translate those cues into slide images. Do not ask the image model to copy a website screenshot unless the slide is explicitly about the website.

Brand recognition depends on real assets before abstract style. If a concrete brand or product is central to the deck, look for official logos, product images, UI screenshots, or user-provided assets before generating generic brand-colored visuals. If they are unavailable, state that limitation and use conceptual visuals instead of fake proof.

## Safe Zones

Pick one safe-zone strategy:

- left-safe: subject on right, title/copy on left
- right-safe: subject on left, title/copy on right
- top-safe: scene below, title/chapter marker above
- center-safe: subject central, minimal overlay text

If the final layout is unknown, generate left-safe and right-safe variants.

## Do Not Bake Into Images

Keep these editable whenever possible:

- slide titles
- Chinese body text
- bullet lists
- metrics and percentages
- source notes
- detailed chart labels
- customer quotes
- UI proof that must be factual

Bitmap images carry atmosphere, scene, and memory. Editable slide objects carry claims, data, labels, and proof.

## Quality Check

Before using an image:

- Does it communicate the slide thesis in one second?
- Is there a real text-safe zone?
- Does it still work as a thumbnail?
- Are important details away from the outer 8%?
- Is it calmer than the text layer where text will sit?
- Does it belong to the same visual system as the rest of the deck?
- Could it be mistaken for factual evidence? If yes, label or replace it.
