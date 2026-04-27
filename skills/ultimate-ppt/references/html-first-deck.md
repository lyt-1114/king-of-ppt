# HTML-First Deck Engine

Use this when the deck needs stronger visual quality, browser presentation, PDF export, or a visual preview beside a PPTX.

## Core Principle

Treat HTML as the visual source of truth and PPTX/PDF as delivery derivatives.

The strongest workflow is:

1. Build a browser-playable HTML deck.
2. Verify the deck visually in the browser.
3. Export or rebuild to PPTX/PDF only after the visual system works.

This does not mean every deliverable must be a website. It means the deck is designed with a real canvas, isolated pages, CSS typography, screenshots, and browser inspection before it becomes a business file.

## Architecture Choice

| Situation | Use |
| --- | --- |
| 5+ slides, reports, lectures, sales decks, case-heavy decks | Multi-file HTML deck |
| 1-4 slides, quick concept, animated keynote moment | Single HTML file |
| Final must be editable PPTX | Editable-safe HTML from the first line, then export/rebuild |
| Final must be visually faithful | HTML + PDF, optionally plus PPTX summary |

Default to a multi-file deck for serious work:

```text
deck/
  index.html
  shared/
    slide.css
  slides/
    01-cover.html
    02-context.html
    03-proof.html
```

Use `assets/deck_index.html` as the starter for `index.html` and `assets/slide.css` as the shared baseline.

## Two-Page Grammar Pass

For any deck with 5 or more slides, do not produce all pages in one pass.

First create two showcase pages:

- one high-impact page: cover, divider, thesis, or keynote claim
- one content-heavy page: case, architecture, data, comparison, or evidence

Use these two pages to lock:

- masthead or footer system
- outer margins and grid
- title/body/metadata type scale
- color rhythm
- image treatment
- chart/table treatment
- density limits
- recurring motifs

If the two pages look like different decks, fix the system before making more slides.

## Visual Grammar Checklist

Before bulk production, write a short visual grammar:

```markdown
# Visual Grammar

Canvas:
Grid and margins:
Type roles:
Color system:
Page rhythm:
Image treatment:
Diagram/chart rules:
Footer/source zone:
Reusable motifs:
Forbidden moves:
```

## Page Rhythm

A polished deck should not feel like a template with different titles.

Alternate page treatments while keeping the same type, margins, and footer:

- thesis page: large claim, minimal support
- section divider: strong rhythm reset
- comparison page: before/after or options
- architecture page: one model, not many models
- case story page: situation, move, result
- case proof page: metrics, artifact, evidence
- scorecard page: evaluation criteria
- roadmap page: phases and decision points
- closing page: one action

Avoid three consecutive pages with the same central grid.

## Browser Verification

For HTML decks:

- open `index.html`
- use keyboard navigation through every page
- inspect at full screen and at thumbnail size
- screenshot at least the two grammar pages and any dense evidence page
- check that no page scrolls and no text is clipped

For serious decks, keep a `run-log.md` with:

- source files read
- route chosen
- visual grammar
- two-page pass outcome
- checks run
- known limitations

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Building 20 pages before testing the visual direction | Make two grammar pages first |
| Letting each page invent its own style | Define shared tokens and footer/masthead zones |
| Using HTML only as a screenshot generator | Make it playable and inspectable |
| Designing a beautiful HTML deck, then promising editable PPTX | Decide editable constraints before layout |
| Repeating the same bento grid | Vary page archetypes, repeat motifs only |
