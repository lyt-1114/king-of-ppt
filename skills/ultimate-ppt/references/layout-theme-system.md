# Layout And Theme System

Use this when creating an HTML-first deck, choosing page archetypes, creating a reusable template, or avoiding a generic repeated layout.

## Core Principle

A deck should be built from a small system:

- one theme token set
- one runtime/chrome convention
- one layout catalog
- one page rhythm plan
- one set of forbidden moves

Do not design every slide from scratch, and do not paste the same grid everywhere.

## Theme Tokens

Define theme tokens before page production:

```css
:root {
  --paper: #fbfaf7;
  --ink: #171717;
  --muted: #68645f;
  --line: #ded9cf;
  --accent: #0f766e;
  --panel: #ffffff;
  --display-font: Georgia, "Times New Roman", serif;
  --body-font: system-ui, -apple-system, "Segoe UI", sans-serif;
}
```

Use variables in slide CSS. Avoid random one-off hex values.

## Layout Catalog

Pick a layout by slide job:

| Slide Job | Layout Pattern |
| --- | --- |
| open attention | cover hero, editorial claim, product moment |
| orient | TOC, agenda map, chapter divider |
| explain concept | two-column, statement plus evidence, annotated diagram |
| prove | KPI grid, table, chart, case proof |
| compare | before/after, option matrix, pros/cons |
| show system | architecture map, workflow, layered model |
| show time | timeline, roadmap, gantt, maturity ladder |
| teach | concept, worked example, practice, recap |
| persuade | problem, diagnosis, solution, proof, decision |
| close | one final judgment and action |

Use existing archetypes first. Create a new layout only when the slide job is genuinely different.

## Theme Rhythm

Plan rhythm before production:

- cover or section pages reset the deck visually
- dense pages should be followed by breathing or visual pages when possible
- case stories often work as a spread: story page then proof page
- dark/light, image/text, sparse/dense should alternate deliberately
- no three consecutive slides should share the same central layout

For editorial/keynote decks, use hero or chapter pages as breathing points. For consulting decks, use summary or decision pages as breathing points.

## Layout Preflight

Before using a starter or template:

- verify every class used by a slide exists in the shared CSS
- verify header/footer/source zones are already defined
- verify image containers have fixed crop rules
- verify the runtime supports keyboard navigation
- verify notes are hidden from audience view

If a slide looks unstyled, stop and fix the shared CSS. Do not patch every page with inline exceptions.

## Image Ratio Rules

Use standard ratios rather than the raw source image ratio:

| Use | Ratio / Sizing |
| --- | --- |
| full hero | 16:9, crop-safe |
| side image | 16:10, 4:3, or 3:2 |
| screenshot evidence | contain or framed crop, preserve meaningful UI |
| image grid | fixed height, consistent crop |
| portrait/person | 3:4 or 1:1 |
| logo | contain, never crop |

Prefer `object-position: top center` for screenshots so top navigation and titles survive cropping.

## Presenter Notes

If the deck is for a live talk, add speaker notes as a first-class layer.

Notes should:

- be hidden from audience slides
- be conversational, not essay-like
- contain transition lines between slides
- use bold keywords or short paragraphs when rendered in presenter mode
- avoid duplicating visible slide text verbatim

For a 30-minute talk, 8-12 slides with strong notes often beats 25 cramped slides.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Choosing a theme by color only | Choose by audience, page density, and evidence type |
| Inventing a new layout for every slide | Use a catalog and vary rhythm |
| Copying template demo content structure blindly | Map layout to slide job first |
| Using image ratios copied from original files | Use standard presentation ratios |
| Putting presenter script on visible slides | Put it in notes |
| Adding arbitrary local CSS per slide | Fix shared tokens/classes |
