# Ultimate PPT

<p align="center">
  <img src="docs/readme/hero.svg" alt="Ultimate PPT: Not another PPT skill. Image2PPT-first, multi-engine, editable, verified." width="100%">
</p>

**Ultimate PPT is an Image2PPT-first agent skill for creating polished, editable, multi-format, and verified presentations.**

Most PPT skills stop at "generate slides from text." Ultimate PPT goes further: it reads visual references, extracts design grammar, plans the story, locks execution rules, builds a two-page visual proof, chooses the right output engine, and audits the result before delivery.

It is built for one hard problem: AI slides often look generic. Ultimate PPT starts from **visual evidence and design intent**, then rebuilds the deck as a real presentation system instead of flattening everything into screenshots.

```bash
npx skills add https://github.com/lyt-1114/king-of-ppt
```

## The Claim

This is not a simple PPT generator.

Ultimate PPT is a **multi-engine presentation system** centered on Image2PPT:

- **Image2PPT core**: reference image, screenshot, PDF page, website, poster, old PPT, product visual, or rough mockup becomes a reusable deck grammar.
- **Strategy engine**: audience, decision goal, narrative spine, proof layer, and deck route are chosen before slides are drawn.
- **Visual system engine**: palette, typography, grid, image role, page rhythm, and forbidden moves are locked before bulk production.
- **HTML-first engine**: browser-native decks can be used as the visual source of truth for premium previews and exports.
- **Editable PPTX engine**: business-critical text, claims, numbers, diagrams, and sources remain editable when the user needs PowerPoint.
- **Presenter engine**: live-talk decks can include hidden notes, pacing, motion, and stage-readable typography.
- **Audit engine**: generated outputs are checked for overlap, overflow, density, duplicate footers, source coverage, and image2 evidence.

<p align="center">
  <img src="docs/readme/engine-map.svg" alt="Ultimate PPT engine map" width="100%">
</p>

## Why Image2PPT

Image2 is the flagship workflow.

Give the agent a reference image, PDF page, website screenshot, brand visual, product screenshot, poster, old PPT, or rough mockup. The skill extracts the visual grammar and uses it to produce a deck with:

- editable titles, claims, metrics, charts, labels, and source notes
- image-driven covers, dividers, case scenes, and premium showcase pages
- a two-page visual grammar pass before bulk production
- an execution lock for colors, fonts, icons, image treatment, page rhythm, and forbidden moves
- HTML-first preview when visual quality matters
- PPTX/PDF/HTML outputs depending on the real delivery need
- audit checks for overlap, overflow, density, duplicate footers, unreadable text, and missing image2 evidence

It is not "screenshot to PPT." It is **reference image to presentation system**.

<p align="center">
  <img src="docs/readme/workflow.svg" alt="Image2PPT workflow" width="100%">
</p>

## Built To Beat Thin PPT Skills

<p align="center">
  <img src="docs/readme/comparison.svg" alt="Typical PPT skill versus Ultimate PPT" width="100%">
</p>

| Thin PPT Skill | Ultimate PPT |
| --- | --- |
| Starts from a prompt | Starts from sources, references, audience, and goal |
| Applies a template | Extracts visual grammar and creates a deck system |
| Often flattens design into images | Keeps claims, metrics, labels, charts, diagrams, and sources editable |
| Makes all slides at once | Runs a two-page showcase before bulk production |
| One output path | Routes to PPTX, HTML, PDF, hybrid, prompt board, or speaker-ready deck |
| Visual quality judged by vibe | Runs quality gates and layout audits |
| Easy to drift after slide 3 | Uses strategy lock and execution lock for consistency |

## What Makes It Different

### 1. Image2 Is First-Class

Images are treated as slide arguments, not decoration. Each generated or selected image must have a role, thesis, safe zone, and thumbnail-readable focal point.

The deck stays hybrid by default:

- bitmap layer: atmosphere, product/case scene, cover visual, texture, screenshot frame
- editable layer: slide title, claim, numbers, diagrams, labels, source notes
- validation layer: overlap checks, font-size checks, density checks, factual-source checks

### 2. Visual Grammar Before Bulk Production

For serious or premium decks, the agent does not produce 30 slides and hope the style works. It first creates or describes two representative pages:

- one high-impact page such as cover, thesis, or divider
- one dense page such as case, architecture, data, or comparison

Those two pages lock the grammar: margins, typography, color rhythm, footer logic, image treatment, chart style, and density budget.

### 3. Strategy + Execution Lock

The skill separates thinking from production:

- `source-brief.md`: audience, goal, proof, constraints
- `image2-brief.md`: reference source, editable layer, bitmap layer, transfer level, risks
- `visual-grammar.md`: palette, type hierarchy, composition, spacing, image treatment
- `strategy-lock.md`: narrative spine, deck route, output architecture
- `execution-lock.md`: canvas, colors, fonts, icons, images, rhythm, forbidden moves

That makes long decks more consistent and keeps the agent from drifting into random colors, repeated grids, tiny text, or mixed icon styles.

### 4. Editable When It Matters

Editable PPTX and maximum visual freedom are different paths. The skill forces that choice early.

If the user needs PPTX editing, the deck follows editable-safe constraints from the beginning. If visual fidelity matters more, the skill can deliver HTML/PDF plus a simplified editable PPTX when useful.

### 5. Verification Is Built In

Before claiming completion, the skill checks:

- text overflow and off-slide text
- overlapping non-empty text boxes
- duplicate footers or source lines
- high slide density
- thumbnail readability
- source-backed numeric claims
- hidden speaker notes for live-talk decks
- browser navigation for HTML-first decks
- image2 evidence files and visual grammar notes

## Use Cases

| Use Case | What Ultimate PPT Does |
| --- | --- |
| Reference image to PPT | Extracts visual grammar, rebuilds editable presentation pages |
| Screenshot/PDF style matching | Matches composition, rhythm, palette, and type hierarchy |
| Brand visual deck | Turns brand cues into presentation images and editable layouts |
| Product launch | Creates hero moments, feature flow, proof, and CTA |
| Enterprise sales deck | Builds problem, diagnosis, solution, cases, proof, rollout, decision |
| Technical report | Structures background, comparison, architecture, modules, cases, evaluation, roadmap |
| Keynote / live talk | Adds presenter notes, stage-readable typography, HTML preview |
| PPT cleanup | Preserves facts while rebuilding the narrative and visual system |

## Workflow

1. Read source material: documents, screenshots, URLs, images, data, old PPTs.
2. Create a source brief: audience, goal, proof, assumptions, risks.
3. For image2 work, extract visual grammar and record the editable/bitmap layer split.
4. Choose the deck route: consulting, pitch, launch, keynote, technical report, training, image-driven PPT, or browser-native.
5. Choose delivery architecture: editable PPTX, HTML-first, PDF, hybrid, or prompt board.
6. For image2 or premium work, run the two-page showcase pass.
7. Create an execution lock for serious, long, or multi-format decks.
8. Produce the deck using the right format.
9. Audit layout, readability, source coverage, output files, and image2 evidence.
10. Report what was built, what was checked, and any limitations.

## Capabilities

`ultimate-ppt` helps the agent make better deck decisions before it starts drawing slides:

- **Image2PPT style extraction**: turn a reference image, website screenshot, old PPT page, or PDF spread into a reusable visual grammar.
- **Image2 evidence trail**: record the reference read, transfer level, editable layer, bitmap layer, and visual grammar so the result is explainable, repeatable, and auditable.
- **Premium first impression**: create stronger covers, chapter dividers, case scenes, and product moments instead of plain title-card decks.
- **Editable business delivery**: keep claims, numbers, labels, charts, and source notes editable instead of flattening every slide into a picture.
- **Two-page showcase before bulk work**: test one high-impact page and one dense page first, so a 20-slide deck does not drift after page 3.
- **Execution lock for consistency**: fix canvas, colors, typography, icons, image treatment, page rhythm, and forbidden moves before production.
- **HTML-first visual preview**: use a browser-playable deck to inspect design quality before exporting PPTX or PDF.
- **Speaker-ready output**: add hidden presenter notes, stage-readable typography, and cleaner live-talk pacing.
- **PPT cleanup and rebuild**: preserve facts from an ugly or old PPT, then rebuild the story and visual system.
- **Verification before delivery**: audit overlap, overflow, density, duplicate footers, missing sources, and unreadable thumbnail pages.

## Install

From this repository URL:

```bash
npx skills add https://github.com/lyt-1114/king-of-ppt
```

## Repository Structure

```text
skills/ultimate-ppt/SKILL.md
skills/ultimate-ppt/agents/openai.yaml
skills/ultimate-ppt/assets/
skills/ultimate-ppt/assets/deck_index.html
skills/ultimate-ppt/assets/slide.css
skills/ultimate-ppt/references/
skills/ultimate-ppt/references/content-playbook.md
skills/ultimate-ppt/references/editable-pptx.md
skills/ultimate-ppt/references/execution-lock.md
skills/ultimate-ppt/references/html-first-deck.md
skills/ultimate-ppt/references/image2-deck-workflow.md
skills/ultimate-ppt/references/image-driven-ppt.md
skills/ultimate-ppt/references/layout-theme-system.md
skills/ultimate-ppt/references/presentation-image-system.md
skills/ultimate-ppt/references/presentation-readout.md
skills/ultimate-ppt/references/presenter-motion-export.md
skills/ultimate-ppt/references/quality-gates.md
skills/ultimate-ppt/references/style-preset-library.md
skills/ultimate-ppt/references/visual-direction-showcase.md
skills/ultimate-ppt/references/visual-system.md
skills/ultimate-ppt/references/workflow.md
skills/ultimate-ppt/references/writing-style.md
skills/ultimate-ppt/scripts/audit_deck.py
```

## Validate

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/ultimate-ppt
python skills/ultimate-ppt/scripts/audit_deck.py path/to/output-folder
python skills/ultimate-ppt/scripts/audit_deck.py path/to/output-folder --image2
```

## Try It

```text
Use ultimate-ppt to turn this reference image and product notes into a premium sales deck.
Keep the final PPTX editable, but match the image's visual mood.
```

```text
Use ultimate-ppt to convert this website screenshot into a 12-slide product launch deck.
Extract the visual grammar first, then create a two-page showcase before the full deck.
```

```text
Use ultimate-ppt to improve this ugly PPT.
Preserve the facts, rebuild the visual system, add stronger case pages, and audit the final PPTX.
```

```text
Use ultimate-ppt to make a speaker-ready keynote from this document.
Create hidden presenter notes and an HTML preview, then export a PPTX.
```

## Update Log

See [CHANGELOG.md](CHANGELOG.md) for the full history.

## License

MIT
