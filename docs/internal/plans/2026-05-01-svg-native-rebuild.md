# SVG Native Rebuild Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `svg-native-rebuild` command that converts structured SVG slides into a native editable PowerPoint deck.

**Architecture:** Keep the route inside `packages/image2ppt-exact` as a focused module named `native_svg.py`. The module parses SVG with the standard library, creates PPT objects with `python-pptx`, and reports object counts in a markdown log.

**Tech Stack:** Python 3.10+, `python-pptx`, `xml.etree.ElementTree`, standard-library path and base64 helpers.

---

## File Map

- Create `packages/image2ppt-exact/src/image2ppt_exact/native_svg.py`: SVG collection, parsing, PPT object creation, log writing.
- Modify `packages/image2ppt-exact/src/image2ppt_exact/cli.py`: add `svg-native-rebuild` subcommand.
- Modify `packages/image2ppt-exact/src/image2ppt_exact/__init__.py`: export config, result, and runner.
- Modify `packages/image2ppt-exact/tests/test_exporter.py`: add route tests.
- Modify `packages/image2ppt-exact/README.md`: document the new route.
- Modify `skills/image2ppt-exact/SKILL.md`: add route selection guidance and command.

## Tasks

### Task 1: Add Failing Tests

**Files:**
- Modify: `packages/image2ppt-exact/tests/test_exporter.py`

- [x] **Step 1: Add tests for SVG native rebuild**

Add tests that expect:

- a simple structured SVG produces native text and shapes
- data URI images become PowerPoint pictures
- CLI parser recognizes `svg-native-rebuild`

- [x] **Step 2: Run tests to verify failure**

Run:

```bash
cd packages/image2ppt-exact
python -m unittest discover -s tests
```

Expected before implementation: import failure or missing CLI command.

### Task 2: Implement Native SVG Route

**Files:**
- Create: `packages/image2ppt-exact/src/image2ppt_exact/native_svg.py`
- Modify: `packages/image2ppt-exact/src/image2ppt_exact/__init__.py`

- [x] **Step 1: Implement config/result dataclasses and SVG collection**

Create `SvgNativeRebuildConfig`, `SvgNativeRebuildResult`, and `collect_svg_files`.

- [x] **Step 2: Implement SVG parsing and PPT object conversion**

Support first-pass native objects:

- text
- rect
- circle/ellipse
- line
- polyline/polygon
- simple path
- image
- recursive group

- [x] **Step 3: Implement object-count log**

Write `*.svg-native-log.md` beside the generated PPTX.

- [x] **Step 4: Export route from package init**

Expose the public API.

### Task 3: Add CLI Support

**Files:**
- Modify: `packages/image2ppt-exact/src/image2ppt_exact/cli.py`

- [x] **Step 1: Add parser subcommand**

Command:

```bash
image2ppt-exact svg-native-rebuild path/to/svg_slides --pptx path/to/native_editable.pptx
```

- [x] **Step 2: Call route and print result paths/counts**

Print PPTX path, log path, slide count, and native object counts.

### Task 4: Documentation

**Files:**
- Modify: `packages/image2ppt-exact/README.md`
- Modify: `skills/image2ppt-exact/SKILL.md`

- [x] **Step 1: Document route table entry**

Add `svg-native-rebuild` between OCR editable text and blueprint rebuild.

- [x] **Step 2: Document boundary**

Explain that structured SVG converts to native PPT objects, while a one-image SVG wrapper remains a bitmap.

### Task 5: Verification and Commit

**Files:**
- All changed files

- [x] **Step 1: Run unit tests**

Run:

```bash
cd packages/image2ppt-exact
python -m unittest discover -s tests
```

- [x] **Step 2: Run CLI help**

Run:

```bash
cd packages/image2ppt-exact
python -m image2ppt_exact.cli --help
```

- [x] **Step 3: Commit and push**

Run:

```bash
git add .
git commit -m "feat: add svg native rebuild route"
git push origin main
```
