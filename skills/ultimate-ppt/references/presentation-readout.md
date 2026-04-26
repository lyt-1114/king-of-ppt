# Presentation Readout Guide

Use this when the user needs a deck that can be presented directly, projected, or read comfortably without zooming.

## Live Presentation Mode

Live presentation decks are not documents. The audience must understand the point while listening to the speaker.

Use this hierarchy as a default:

- Cover title: 34-44 pt
- Slide title / claim headline: 28-36 pt
- Section label: 10-13 pt
- Main body: 18-24 pt
- Card body: 15-18 pt
- Diagram label: 12-16 pt
- Footer/source: 8-10 pt

Avoid any meaningful content below 12 pt. If content cannot fit above that size, split the slide.

## Readability Rules

- One slide should have one claim the speaker can say out loud in one sentence.
- Use 1-3 support blocks on normal slides; use 4 only for comparisons or portfolios.
- Prefer large callouts, simple diagrams, and fewer rows over dense tables.
- If a case needs five facts, use two slides: story first, evidence second.
- Keep decorative motifs away from text-critical zones.
- Do not rely on the audience reading paragraphs while the presenter speaks.
- Use consistent slide regions: title top, evidence center, takeaway bottom.

## Direct-Report Page Patterns

Use these page patterns for presentable decks:

- **Claim page**: one sentence headline, one explanatory sentence, one visual proof.
- **Comparison page**: two columns, 4 rows max, decisive takeaway.
- **Architecture page**: 4-5 layers max, labels large enough to read from the back of a room.
- **Case story page**: situation, intervention, result; one big metric.
- **Case proof page**: 2-3 metrics with captions; reusable assets and replication path.
- **Roadmap page**: 3-4 phases with deliverables and decision gates.

## Fixing Small or Abrupt Slides

If a slide feels small, noisy, or abrupt:

1. Rewrite the title as a claim, not a topic.
2. Choose the one thing the audience must remember.
3. Keep only the evidence needed to support that claim.
4. Move the rest to a follow-up slide, notes, or appendix.
5. Increase font size before adding decoration.

## Quality Check

Before delivery:

- Scan the deck in slide sorter or thumbnails. Each slide should still have an obvious message.
- Check that meaningful text is not under 12 pt.
- Check that live body text is generally 18 pt or larger.
- Confirm no slide depends on reading more than one dense paragraph.
- Run `scripts/audit_deck.py` and fix font-size, overlap, and off-slide warnings.
