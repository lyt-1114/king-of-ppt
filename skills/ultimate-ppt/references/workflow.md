# Ultimate PPT Workflow

## 1. Source Brief

Create `source-brief.md` for non-trivial decks:

```markdown
# Source Brief

Audience:
Decision / action wanted:
Source files and URLs:
Must-include facts:
Strongest proof:
Open gaps:
Footer / citation / brand requirements:
Recommended deck route:
```

Do not invent missing proof. Mark uncertain claims as assumptions or omit them.

## 2. Strategy Lock

Create `strategy-lock.md` before production:

```markdown
# Strategy Lock

Output format:
Delivery architecture:
Slide count:
Audience:
Desired action:
Narrative spine:
Two-page visual grammar pass:
Visual style:
Typography:
Color system:
Image / diagram plan:
Presenter / motion / export needs:
Slide list:
Acceptance checks:
```

For premium, visual, or ambiguous decks, load `visual-direction-showcase.md` before locking the style. For HTML-first work, load `html-first-deck.md`. For editable PPTX, load `editable-pptx.md` before writing layout code.

For image2, reference-image, screenshot, PDF-page, website-capture, old-PPT, product-image, brand-visual, or rough-mockup work, load `image2-deck-workflow.md` and create:

- `image2-brief.md` or an equivalent run-log section
- `visual-grammar.md`
- a transfer decision: faithful, inspired, upgraded, or hybrid
- an editable-layer / bitmap-layer split
- image safe-zone and recognition-asset notes

For serious, long, template-based, or multi-format decks, create `execution-lock.md` after the strategy lock. It should specify canvas, colors, typography, icons, image inventory, page rhythm, and forbidden moves. Treat it as the production contract.

## 3. Production

Build slides in the chosen format:

- PPTX for editable business files
- HTML-first for polished browser-native presentations, visual previews, and PDF-ready decks
- both when comparison or sharing matters
- prompt board when the task is visual direction

For decks with 5 or more slides, build two representative pages first:

- a high-impact page such as cover, thesis, or divider
- a dense page such as case, architecture, data, or comparison

Use them to confirm typography, margins, image treatment, density, and footer logic before producing the rest.

For image2 decks, the two-page pass must also confirm that the style relation to the reference is visible without flattening the deck into screenshots.

If the deck is a live talk, write hidden presenter notes during production rather than after the deck is finished. Notes should support oral delivery and transitions, not duplicate slide text.

If the task is PPTX conversion or enhancement, extract and summarize the old deck first, then choose faithful remake, visual upgrade, or narrative rewrite. Do not default to screenshot tracing.

Keep output folders self-contained. Include `run-log.md` with sources, choices, and verification.

## 4. Verification

Run quality gates before final response. If using the bundled script:

```bash
python scripts/audit_deck.py path/to/output
```

For image2 decks:

```bash
python scripts/audit_deck.py path/to/output --image2
```

Report the result and any limitations.
