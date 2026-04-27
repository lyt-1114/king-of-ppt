# Quality Gates

Run these checks before delivery.

## Source and Strategy

- [ ] All provided documents, URLs, images, and instructions were read or explicitly skipped with reason.
- [ ] Audience and desired action are clear.
- [ ] Deck route was chosen and shaped the outline.
- [ ] Delivery architecture was chosen before layout: direct PPTX, HTML-first, editable-safe HTML, PDF, or hybrid.
- [ ] Execution lock exists for serious/long/multi-format decks and lists canvas, colors, typography, icons, images, page rhythm, and forbidden moves.
- [ ] Required facts, footers, brand rules, and constraints are included.
- [ ] Numeric claims have source notes or are marked as assumptions.

## Content

- [ ] Every slide has one job.
- [ ] Every non-divider slide has a thesis or takeaway sentence, not only labels.
- [ ] Case slides include situation, intervention, result, and reusable asset.
- [ ] Metrics include context explaining what changed and why it matters.
- [ ] Outline follows a deliberate spine, not a generic repeated pattern.
- [ ] The opening earns attention.
- [ ] The middle builds proof or learning.
- [ ] The ending asks for a concrete action or leaves a clear takeaway.
- [ ] Repeated decks from the same source use different strategies when comparison is requested.

## Visual

- [ ] Palette and typography are consistent.
- [ ] For serious or premium 5+ slide decks, two representative grammar pages were created or inspected before bulk production.
- [ ] Colors, fonts, icons, and image treatment follow the execution lock when one exists.
- [ ] Text fits inside slide boundaries.
- [ ] Meaningful presentation text is not below 12 pt; live body text is generally 18 pt or larger.
- [ ] Non-empty text boxes do not overlap unintentionally.
- [ ] Footers, page numbers, logos, and source lines are not duplicated.
- [ ] Slide density matches the chosen archetype; dense detail is moved to notes or appendix.
- [ ] Each page has enough whitespace to read at thumbnail scale.
- [ ] Visual assets are relevant to the subject.
- [ ] Presentation images have a role, thesis, safe zone, and thumbnail-readable focal point.
- [ ] Image-heavy slides preserve editable titles, claims, metrics, and source notes unless the user requested flattened poster slides.
- [ ] Generated or conceptual images are not presented as factual screenshots or customer proof.
- [ ] Important text does not sit on busy image areas without a contrast panel or safe zone.
- [ ] Page rhythm varies: no three consecutive slides are the same central layout with swapped content.
- [ ] No decorative clutter.
- [ ] Charts/metrics are readable.
- [ ] Mobile/browser HTML slides fit 100vh with no internal scrolling.

## Output

- [ ] Required PPTX/HTML/PDF files exist.
- [ ] HTML-first decks open through `index.html` and keyboard navigation works.
- [ ] Live-talk decks keep speaker notes hidden from audience view.
- [ ] First-slide footer/source requirement is present when requested.
- [ ] Notes or run log are included for serious decks.
- [ ] Export/openability has been checked.
- [ ] Any limitations are reported honestly.

## Failure Response

If a check fails:

1. Identify the failed gate.
2. Fix the smallest necessary part.
3. Re-run the relevant check.
4. If the same gate fails twice, choose a different content or layout approach instead of tweaking the same solution.

For PPTX layout failures:

- Overlap usually means the slide is too dense; split the slide before shrinking fonts.
- Duplicate footer warnings usually mean footer logic is scattered; centralize it.
- High density means cut copy, convert detail to notes, or use an appendix.
- Off-slide text means the layout was not built from stable bounds; use fixed boxes and shorter text.
