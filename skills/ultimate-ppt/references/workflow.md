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
Slide count:
Audience:
Desired action:
Narrative spine:
Visual style:
Typography:
Color system:
Image / diagram plan:
Slide list:
Acceptance checks:
```

## 3. Production

Build slides in the chosen format:

- PPTX for editable business files
- HTML for web-native presentations
- both when comparison or sharing matters
- prompt board when the task is visual direction

Keep output folders self-contained. Include `run-log.md` with sources, choices, and verification.

## 4. Verification

Run quality gates before final response. If using the bundled script:

```bash
python scripts/audit_deck.py path/to/output
```

Report the result and any limitations.
