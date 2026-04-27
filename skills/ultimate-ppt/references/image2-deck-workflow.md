# Image2 Deck Workflow

Use this when the user provides a reference image, screenshot, PDF page, website capture, old PPT page, product visual, brand asset, or rough mockup and expects a stronger deck from it.

## Core Promise

Image2PPT is not screenshot tracing. It is reference image to editable presentation system.

The output should preserve the reference's visual intelligence while rebuilding the deck as usable slides:

- images carry atmosphere, scene, product context, case memory, and premium first impression
- editable objects carry titles, claims, metrics, charts, labels, diagrams, and sources
- verification checks prove the deck is not only visually close, but also readable and editable

## Required Image2 Artifacts

For non-trivial image2 work, create or include these in the output folder:

```text
image2-brief.md
visual-grammar.md
strategy-lock.md
execution-lock.md
run-log.md
```

If the job is very small, merge them into `run-log.md`, but keep the same headings.

### `image2-brief.md`

```markdown
# Image2 Brief

Reference sources:
Source type: brand / website / PDF / screenshot / old PPT / product image / sketch
Audience:
Deck goal:
Output format:
Must stay editable:
Can become bitmap:
Brand/product assets available:
Missing assets:
Risks:
```

### `visual-grammar.md`

```markdown
# Visual Grammar

Reference read:
- palette:
- type hierarchy:
- composition:
- spacing:
- shape language:
- image treatment:
- chart/diagram language:
- footer/source behavior:

Transfer decision:
- faithful / inspired / upgraded / hybrid

Reusable slide archetypes:
- cover hero:
- dense proof page:
- case scene:
- comparison:
- architecture/workflow:
- close:

Forbidden moves:
```

## Source Type Diagnosis

| Source Type | Extract | Watch Out |
| --- | --- | --- |
| Website screenshot | palette, spacing, UI rhythm, brand assets, screenshot crop rules | copying webpage sections instead of making slides |
| PDF/report page | type hierarchy, grid, evidence density, citation behavior | making every slide too text-heavy |
| Old PPT | facts, slide order, required wording, reusable motifs | screenshot tracing ugly pages |
| Product screenshot | actual UI proof, feature flow, interface crop zones | fake UI or unreadable microtext |
| Brand/product image | logo, product hero, material, lighting, color grade | treating color alone as brand identity |
| Poster/key visual | mood, focal point, typography energy, safe zones | flattening every slide into a poster |
| Rough mockup/sketch | intent, hierarchy, missing content | copying rough proportions too literally |

## Brand And Asset Protocol

If a concrete brand, product, or company is involved, do not rely only on colors and fonts.

Look for the recognition assets in this order:

1. logo or wordmark
2. product image, official render, packaging, or hardware photo
3. UI screenshots or app-store/product screenshots for digital products
4. website or brand guideline palette
5. typography clues and motion/photography style

For hero or case visuals, prefer fewer better assets. Use this quality bar:

- search multiple channels when assets are missing: official website, press kit, product page, app store, official video, user-provided files
- gather candidates before choosing; do not use the first small image that appears
- keep only assets that are high resolution, relevant, legally reasonable to use, and visually compatible
- if assets are weak, say so in the run log and use honest placeholders or generated concept visuals instead of pretending they are proof

Logo exception: if a logo is required and available, use it even when it is visually imperfect. Recognition beats abstract brand-colored decoration.

## Transfer Ladder

Choose the transfer level before layout:

| Level | Use When | Rule |
| --- | --- | --- |
| Faithful | user wants close style matching | preserve composition logic, palette, type rhythm, and footer behavior |
| Inspired | reference is a mood board | borrow visual grammar, redesign slide structure for the deck goal |
| Upgraded | old PPT or rough screenshot is weak | preserve facts and intent, rebuild the system at a higher design level |
| Hybrid | PPTX editability and premium visuals both matter | bitmap atmosphere plus editable claims, numbers, labels, and diagrams |

## Two-Page Image2 Pass

Before producing a 5+ slide image2 deck, build two representative pages:

1. High-impact page: cover, thesis, divider, or product moment.
2. Dense page: case, architecture, comparison, data, or proof.

Evaluate them against:

- recognizable relation to the reference
- clear slide thesis
- readable typography at thumbnail scale
- editable title/claim/metric/source layer
- image safe zone
- no fake evidence in bitmap images
- enough style range to support 10+ slides

If the two pages do not feel like the same deck, fix the visual grammar before bulk production.

## Production Pattern

For each slide:

1. Write the slide thesis.
2. Pick the slide archetype.
3. Decide image role and safe zone.
4. Place the editable layer first: title, claim, data, source, labels.
5. Add the bitmap layer around or behind the editable layer.
6. Check thumbnail readability.
7. Check that repeated motifs carry the style while central compositions vary.

Avoid using image generation to hide weak slide thinking. If the thesis, proof, or audience action is unclear, fix content before visual polish.

## Image2 Acceptance Checks

- [ ] `image2-brief.md` or equivalent run-log section exists.
- [ ] `visual-grammar.md` records what was extracted from the reference.
- [ ] Transfer level is explicit: faithful, inspired, upgraded, or hybrid.
- [ ] Must-editable layer is listed and preserved.
- [ ] Bitmap layer does not contain long titles, key metrics, detailed chart labels, or factual proof that should be editable.
- [ ] A high-impact page and dense page were checked before bulk production for 5+ slide decks.
- [ ] No three consecutive slides repeat the same central layout with swapped content.
- [ ] Brand/product work includes recognition assets or explains why they were unavailable.
- [ ] Generated/conceptual images are not presented as factual screenshots or customer proof.
- [ ] Final audit was run with image2 checks when `scripts/audit_deck.py` is available.

## Failure Patterns

| Failure | Fix |
| --- | --- |
| Looks like a screenshot collection | rebuild editable text, metrics, labels, and diagrams |
| Matches color but not structure | extract grid, spacing, type hierarchy, and page rhythm |
| Premium cover, weak body pages | design the dense proof page before the rest |
| Beautiful but uneditable | switch to hybrid PPTX or explain HTML/PDF tradeoff |
| Reference copied too literally | move from faithful to inspired/upgraded transfer |
| Images imply fake proof | label conceptual visuals or replace with real screenshots |
