# Execution Lock

Use this for serious decks, long decks, multi-format delivery, or any deck where repeated visual decisions must stay consistent.

## Core Principle

After strategy and visual direction are chosen, write a compact machine-readable contract. The deck executor should check it before creating every page.

This prevents drift: random colors, mixed icon styles, inconsistent page rhythm, off-brand fonts, and repeated layout accidents.

## Lock Template

Create `execution-lock.md` beside the deck output:

```markdown
# Execution Lock

## canvas
- format:
- width:
- height:
- output:

## colors
- background:
- surface:
- text:
- muted:
- primary:
- accent:
- line:

## typography
- display:
- title:
- body:
- mono:
- title_size:
- body_size:
- note_size:

## layout
- outer_margin:
- gutter:
- footer_zone:
- max_blocks_per_slide:
- dense_slide_rule:

## icons
- library:
- stroke_or_fill:
- approved_icons:

## images
- logo:
- product:
- screenshots:
- hero_images:
- texture_or_background:

## page_rhythm
- P01:
- P02:
- P03:

## forbidden
- 
```

Delete unused rows rather than leaving placeholders.

## Page Rhythm Vocabulary

Use a small rhythm vocabulary. Do not invent a unique rhythm for every slide.

| Rhythm | Use For | Layout Discipline |
| --- | --- | --- |
| `anchor` | cover, divider, TOC, ending | strong identity, low detail |
| `breathing` | single idea, quote, transition, big number | no multi-card grid as primary structure |
| `dense` | evidence, data, case proof, architecture | structured grid allowed, but one main object |
| `visual` | image-led hero/case scene | text-safe zone first |
| `decision` | roadmap, options, CTA | clear next action |

Every slide in the outline should receive one rhythm tag before layout starts.

## Icon Discipline

Choose one icon language:

- Lucide outline
- filled geometric
- duotone
- brand marks only
- no icons

Do not mix outline, filled, emoji, and brand icons as if they are one system. If brand marks are used, keep them in brand/logo contexts rather than general-purpose bullets.

## Font Discipline

Write role-based font stacks, not one generic font:

- display for covers, chapter titles, editorial claims
- title for normal page headings
- body for paragraphs and cards
- mono for metadata, source tags, code, coordinates

If the final output is PPTX, prefer fonts likely to exist on the recipient machine or include a clear font requirement in `run-log.md`.

## Forbidden Moves

List the deck-specific things the executor must not do:

- use arbitrary colors not in the lock
- add a second footer system
- mix icon libraries
- repeat the same bento page three times in a row
- bake long text into generated images
- shrink dense slides below readability thresholds
- add emoji icons
- use screenshots as text backgrounds without safe zones

## When To Update

Change the lock only when the strategy changes. Do not silently mutate colors, fonts, or page rhythm while producing slides. If a slide cannot work under the lock, revise the lock explicitly and record why in `run-log.md`.
