# Editable PPTX Path

Use this when the user needs text and shapes editable inside PowerPoint or Keynote.

## Core Principle

Editable PPTX and maximum HTML visual freedom are different production paths. Decide early.

If editability matters, write the source in a PPTX-safe way from the first slide. If visual fidelity matters more, deliver HTML/PDF and keep PPTX as an optional simplified business version.

## Decision Table

| User Need | Recommended Output |
| --- | --- |
| Stakeholders will edit text, numbers, labels | Editable PPTX |
| Presenter only needs to show/share | HTML + PDF |
| Wants premium visuals and some editable text | Hybrid PPTX: bitmap atmosphere + editable claims/metrics |
| Wants animation/interactivity | HTML, plus PDF/video snapshot if needed |
| Wants both rich HTML effects and fully editable PPTX | Ask for a tradeoff; do not promise both |

## Editable-Safe HTML Rules

When using HTML as an upstream format for editable PPTX, keep it close to PowerPoint's object model:

- Use a 16:9 physical canvas such as `960pt x 540pt` or a known PPTX layout.
- Put meaningful text in `h1`-`h6`, `p`, `li`, or table cells.
- Do not put primary text directly in bare `div` or `span`.
- Let wrapper `div` elements carry fills, borders, and shadows.
- Keep text elements responsible for text only.
- Use solid fills by default; avoid CSS gradients when editability is required.
- Use real `img` tags for pictures rather than CSS `background-image`.
- Avoid pseudo-element text because it will not become editable text.
- Avoid complex SVG as editable structure; use it as an image or redraw with simple shapes.
- Keep every repeated object inside fixed x/y/w/h bounds.

## Hybrid PPTX Pattern

For polished business decks, use layers:

- bitmap layer: hero scene, product render, case atmosphere, texture, screenshot frame
- editable layer: title, claim, metric, source, label, callout, chart axis
- validation layer: overlap check, font-size check, source check

This preserves the "designed" feeling without turning the whole deck into uneditable posters.

## Fallback For Existing Visual HTML

If a free-form HTML deck already exists and the user later asks for editable PPTX:

1. Explain the tradeoff clearly.
2. Offer PDF as the faithful version.
3. Offer an editable rewrite as a simplified version.
4. Preserve the layout intent, palette, hierarchy, and copy.
5. Simplify gradients, filters, web components, and complex SVG.
6. Deliver both versions when useful: faithful PDF plus editable PPTX.

## Verification

After creating editable PPTX:

- open the file
- edit several titles/body blocks manually
- confirm text did not overflow after font fallback
- run `scripts/audit_deck.py` when available
- inspect thumbnail readability

Never claim "editable" if the slide is just a full-slide screenshot.
