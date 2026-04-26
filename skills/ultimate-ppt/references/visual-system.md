# Visual System Guide

## Build the System First

Before making slides, define:

- palette: background, text, muted text, accent, card, line
- type roles: display, title, body, metadata, numeric
- components: metric card, quote page, timeline, comparison, diagram, CTA
- imagery: screenshot, generated visual, diagram, logo, icon set
- density: sparse keynote, medium pitch, dense consulting
- whitespace budget: outer margins, gutters, and maximum number of blocks
- text budget: maximum lines per title, subtitle, body block, and card

## Elegance Rules

Elegant decks usually come from restraint, not decoration.

- Start with the sentence the slide must prove; delete anything that does not support it.
- Use one visual hierarchy per slide: title, one main visual, one short support line.
- Favor 2-4 large objects over many small cards.
- Keep title blocks away from charts and screenshots; never let body text touch media.
- Use generous gutters. If a layout needs tiny gutters to fit, split the slide.
- Avoid nested cards and card-heavy pages unless comparing repeated items.
- Do not use a screenshot as a background for text unless the screenshot is muted and the text has a dedicated clear area.
- Keep page numbers, sources, logos, and footers in one consistent zone.
- Make title, subtitle, body, and footer zones non-overlapping by construction; do not rely on visual alignment if the actual text boxes intersect.
- Avoid abrupt size jumps. If a headline is 32 pt, nearby body text should usually sit around 18-22 pt rather than collapsing to 10-12 pt.
- Use atmosphere at the edges and meaning in the center: backgrounds can set tone, but the central content must stay clean and readable.

## Style Routes

| Route | Visual Direction |
| --- | --- |
| Consulting | white or quiet neutral background, sharp hierarchy, restrained accent |
| Pitch | clean cards, bold section titles, strong CTA blocks |
| Launch | warmer contrast, product moments, benefit blocks |
| Editorial | serif display, large quotes, chapter rhythm, image spreads |
| Technical report | paper background, technical diagrams, scorecards, case pages, section rhythm |
| Chinese ink-tech | soft paper, teal ink accents, ghosted characters, restrained technical grids |
| Browser-native | high-contrast interface, motion layers, geometric atmosphere |
| Prompt board | dark or neutral boards, prompt cards, asset recipes |

## Mixing Styles Without Losing Coherence

Use multiple page treatments, not multiple unrelated decks.

- Keep one palette, one footer system, and one type scale.
- Vary page archetypes: thesis, divider, comparison, architecture, case, evaluation, roadmap.
- Let decorative motifs appear at low opacity and outside text-critical zones.
- Use recurring symbols or small labels to connect sections.
- Avoid changing corner radius, shadow style, and line weight from page to page.
- Vary composition, not quality: alternate claim pages, comparison pages, case spreads, architecture diagrams, and decision pages while preserving the same margins, typography, and footer logic.
- When a case needs more substance, use a two-slide spread instead of a dense bento grid: narrative first, evidence second.

## Chinese Ink-Tech Motif

For elegant technology decks with Chinese cultural tone:

- Use a warm paper background instead of pure white.
- Use teal/emerald as the main accent, charcoal as text, and one warm accent for emphasis.
- Add a subtle oversized character, brush texture, mountain line, or wave footer as atmosphere.
- Keep content grids modern and precise so the deck feels technical, not antique.
- Use the motif mainly on cover, divider, summary, and transition pages; keep dense evidence pages cleaner.

## Image Prompt Pattern

Use this structure for generated images:

```text
[subject and scene], [business context], [composition], [brand tone],
[lighting/color], [presentation image quality], avoid [negative clichés]
```

Example:

```text
Premium enterprise AI operations control room where data streams, workflow nodes,
human review gates and agent tasks converge into one calm execution map,
Chinese B2B technology brand, clean consulting presentation image,
teal-blue accents, no robot handshake, no purple sci-fi brain.
```

## Avoid

- default purple gradients
- decorative blobs with no semantic meaning
- stock people pointing at transparent screens
- robot handshake imagery
- dense walls of text
- repeated bento grids without narrative purpose
- tiny unreadable screenshots

## Slide Density

- Title: 1 headline, 1 subtitle, optional proof/CTA
- Content: 1 main idea, 3-4 bullets or cards
- Metric: 1-3 large metrics with context
- Diagram: 1 flow or model, not multiple competing charts
- Quote: 1 quote, 1 source/context line
- CTA: one action

## Live Presentation Typography

When the deck is meant to be presented directly:

- Prefer title sizes around 28-36 pt and body text around 18-24 pt.
- Keep card body text at 15 pt or larger.
- Keep labels at 12 pt or larger when they carry meaning.
- Use footer/source text at 8-10 pt, but never rely on footer text for the story.
- If a layout needs smaller text, split the slide or move detail to backup.
- Keep line length comfortable. For Chinese body copy, aim for 18-32 characters per line in cards; for wider statement boxes, use one or two short lines.
- Do not make important text compete with large decorative characters, watermarks, charts, or screenshots.

## PPTX Layout Guardrails

When creating PPTX programmatically:

- Define reusable helpers for header, footer, cards, metrics, and diagrams.
- Keep footer generation centralized. Do not add a default footer and then add a second page-specific footer.
- Use stable dimensions rather than content-driven resizing for repeated components.
- After writing the deck, run `scripts/audit_deck.py <output-folder>`.
- If the audit flags overlap, off-slide text, duplicate footers, or high density, revise the layout before delivery.
