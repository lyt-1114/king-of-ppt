# Ultimate PPT

**Image2PPT-first agent skill for creating polished, editable, and verified presentations.**

Turn reference images, screenshots, websites, PDFs, notes, data, and rough ideas into presentation decks that look designed, stay editable, and pass layout checks before delivery.

`ultimate-ppt` is built for one hard problem: most AI-generated slides look generic. This skill starts from visual evidence and design intent, then rebuilds the deck as a real presentation system instead of flattening everything into screenshots.

```bash
npx skills add https://github.com/lyt-1114/king-of-ppt
```

## Why Image2PPT

Image2 is the core workflow.

Give the agent a reference image, PDF page, website screenshot, brand visual, product screenshot, poster, old PPT, or rough mockup. The skill will extract the visual grammar and use it to produce a deck with:

- editable titles, claims, metrics, charts, labels, and source notes
- image-driven covers, dividers, case scenes, and premium showcase pages
- a two-page visual grammar pass before bulk production
- an execution lock for colors, fonts, icons, image treatment, page rhythm, and forbidden moves
- HTML-first preview when visual quality matters
- PPTX/PDF/HTML outputs depending on the real delivery need
- audit checks for overlap, overflow, density, duplicated footers, and unreadable text

It is not "screenshot to PPT." It is **reference image to presentation system**.

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
3. Choose the deck route: consulting, pitch, launch, keynote, technical report, training, image-driven PPT, or browser-native.
4. Choose delivery architecture: editable PPTX, HTML-first, PDF, hybrid, or prompt board.
5. For image2 or premium work, extract visual grammar and run the two-page showcase pass.
6. Create an execution lock for serious, long, or multi-format decks.
7. Produce the deck using the right format.
8. Audit layout, readability, source coverage, and output files.
9. Report what was built, what was checked, and any limitations.

## Install

From this repository URL:

```bash
npx skills add https://github.com/lyt-1114/king-of-ppt
```

Or copy the folder manually:

```bash
mkdir -p ~/.codex/skills
cp -r skills/ultimate-ppt ~/.codex/skills/
```

## Capabilities

`ultimate-ppt` combines and extends the strongest patterns from multiple PPT-oriented skills:

- strategy-first deck planning from `ppt-master`
- template-driven HTML/PPT production from `html-ppt-skill`
- editorial/keynote storytelling from `guizang-ppt-skill`
- presentation-image prompt discipline from `PPT-Design-Prompt`
- browser-native viewport-safe slide craft from `frontend-slides`
- HTML-first visual production with PDF/PPTX derivatives
- two-page visual grammar passes before bulk slide production
- editable-PPTX constraint handling
- execution-lock discipline for production consistency
- presenter notes, motion recipes, viewport fitting, export discipline, and PPTX conversion intake
- fact-driven verification without coercive tone

## Repository Structure

```text
skills/ultimate-ppt/SKILL.md
skills/ultimate-ppt/assets/
skills/ultimate-ppt/assets/deck_index.html
skills/ultimate-ppt/assets/slide.css
skills/ultimate-ppt/references/
skills/ultimate-ppt/references/content-playbook.md
skills/ultimate-ppt/references/editable-pptx.md
skills/ultimate-ppt/references/execution-lock.md
skills/ultimate-ppt/references/html-first-deck.md
skills/ultimate-ppt/references/image-driven-ppt.md
skills/ultimate-ppt/references/layout-theme-system.md
skills/ultimate-ppt/references/presentation-image-system.md
skills/ultimate-ppt/references/presentation-readout.md
skills/ultimate-ppt/references/presenter-motion-export.md
skills/ultimate-ppt/references/quality-gates.md
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
```

## Update Log

### 2026-04-27

- Repositioned the project around Image2PPT / image-driven deck creation.
- Added HTML-first deck engine guidance: browser-playable `index.html` as visual source, isolated slide files, visual verification, and starter `assets/deck_index.html` / `assets/slide.css`.
- Added visual direction/showcase workflow: three distinct style directions and a two-page grammar pass for premium 5+ slide decks.
- Added editable PPTX guidance: early editability decision, HTML constraints, hybrid bitmap + editable object pattern, and fallback for visual HTML that later needs PPTX.
- Added execution-lock guidance: page rhythm, approved colors/fonts/icons/images, and forbidden moves.
- Added layout/theme system guidance: token-first themes, layout archetype catalog, preflight checks, image ratio rules, and presenter-note handling.
- Added presenter/motion/export guidance: hidden speaker notes, semantic animation recipes, viewport fitting, PPTX conversion intake, PDF/export/deploy discipline, and optional browser editing boundaries.
- Added presentation-image system guidance: slide images as arguments, role/thesis/safe-zone prompt skeletons, brand-inspired translation, and text-safe image rules.
- Added PPTX layout audit checks, density guardrails, image-driven PPT rules, and source-informed presentation principles.

## License

MIT
