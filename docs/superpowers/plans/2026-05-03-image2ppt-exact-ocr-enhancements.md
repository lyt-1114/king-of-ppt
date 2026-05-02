# image2ppt-exact OCR Enhancements Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Absorb the most practical OCR-editable capabilities into `image2ppt-exact`: spec-based OCR correction, OCR color/font-size recovery, and a clearly documented manual-correction rerun workflow.

**Architecture:** Keep `full-rebuild` as the single user-facing route, but strengthen the underlying OCR/editable layer. OCR extraction will emit richer block metadata, editable generation will optionally correct OCR text from a spec file before building text boxes, and docs/logs will explain how users can hand-edit OCR JSON and rerun without repeating OCR.

**Tech Stack:** Python, `python-pptx`, Pillow, existing OCR adapters, stdlib matching utilities, unittest.

---

### Task 1: Add regression tests for richer OCR/editable behavior

**Files:**
- Modify: `packages/image2ppt-exact/tests/test_exporter.py`

- [ ] Add failing tests for:
  - spec correction replacing OCR text from a provided spec file
  - OCR block extraction including `color` and `font_size`
  - pipeline logs/docs surfacing manual-correction rerun guidance

### Task 2: Implement OCR metadata enrichment and spec correction

**Files:**
- Modify: `packages/image2ppt-exact/src/image2ppt_exact/editable.py`
- Modify: `packages/image2ppt-exact/src/image2ppt_exact/cli.py`
- Modify: `packages/image2ppt-exact/src/image2ppt_exact/pipeline.py`
- Modify: `packages/image2ppt-exact/src/image2ppt_exact/full_rebuild.py`

- [ ] Add optional spec-file plumbing to `editable`, `image-svg-editable`, and `full-rebuild`
- [ ] Enrich OCR JSON blocks with sampled `color` and estimated `font_size`
- [ ] Apply spec correction before editable textbox generation and preserve existing OCR JSON reuse behavior

### Task 3: Explain the absorbed capabilities and rerun flow

**Files:**
- Modify: `packages/image2ppt-exact/README.md`
- Modify: `packages/image2ppt-exact/docs/routes/02-ocr-editable.md`

- [ ] Document the three absorbed capabilities
- [ ] Explain when users can rerun from existing OCR JSON and when they should regenerate/redact backgrounds

### Task 4: Verify behavior

**Files:**
- No code changes

- [ ] Run focused tests for the new OCR/editable cases
- [ ] Run the package test suite
