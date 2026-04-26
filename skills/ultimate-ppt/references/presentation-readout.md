# Presentation Readout Guide

Use this when the user needs a deck that can be presented directly, projected, or read comfortably without zooming.

## Live Presentation Mode

Live presentation decks are not documents. The audience must understand the point while listening to the speaker.
Run a stage-readability pass before layout: if the slide only works when zoomed in, it is not a presentation slide yet.

Use this hierarchy as a default:

- Cover title: 34-44 pt
- Slide title / claim headline: 28-36 pt
- Section label: 10-13 pt
- Main body: 18-24 pt
- Card body: 15-18 pt
- Diagram label: 12-16 pt
- Footer/source: 8-10 pt

Avoid any meaningful content below 12 pt. If content cannot fit above that size, split the slide.
For normal projected decks, treat 18 pt as the practical floor for body copy. Microsoft presentation guidance recommends avoiding sizes below 18 pt for distance reading; use 12-16 pt only for diagram labels, source notes, and metadata that is not needed to follow the story.

## Stage-Ready Craft Rules

Use these rules when the user says the deck is ugly, too small, abrupt, crowded, or not ready for live reporting:

- Pass the 3-second glance test: the audience should know the slide's main point before reading the body.
- Put one idea on one slide. If the content has two claims, create two slides instead of shrinking type.
- Design is not decoration: every icon, line, chip, and background mark must clarify hierarchy or meaning.
- Keep the speaker in control. Slides should support the oral story, not force the audience to read paragraphs.
- Use short, complete Chinese sentences with a point of view; avoid noun-only labels unless they are small section markers.
- Prefer 2-3 large evidence blocks over 4-6 small cards. Use one large metric instead of a row of tiny numbers.
- Split cases into story and proof when needed: one slide for situation/intervention/result, one slide for metrics/assets/replication.
- Keep all decorative motifs outside the title, body, chart, and footer zones.
- If the audit reports high density, fix it by cutting, splitting, or moving detail to notes/appendix. Do not lower font size.

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
- **Elegant case spread**: first page uses a large scenario statement and one workflow visual; second page uses 1 big result, 2 supporting metrics, and a reusable asset line.

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
- Review slide sorter thumbnails. If multiple slides look like the same grid, vary the page treatment while keeping the same palette and type scale.

## Source-Informed Principles

- Microsoft PowerPoint support: use readable sans serif fonts, strong contrast, accessible templates, and avoid small font sizes for distant audiences.
- Duarte: keep one idea per slide, make design serve the message, and build from the audience's needs.
- Presentation Zen / Garr Reynolds: use restraint, simplicity, and emphasis; remove noise so the core message has room to breathe.
