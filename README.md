# Ultimate PPT Skill

`ultimate-ppt` is a Codex/agent skill for creating best-in-class presentations from documents, websites, notes, data, and rough ideas.

It combines the strongest patterns from several PPT-oriented skills:

- strategy-first production discipline from `ppt-master`
- template-driven HTML/PPT thinking from `html-ppt-skill`
- editorial/keynote storytelling from `guizang-ppt-skill`
- visual prompt system thinking from `PPT-Design-Prompt`
- browser-native, viewport-safe slide craft from `frontend-slides`
- fact-driven owner/verification discipline inspired by the useful parts of the referenced PUA skill, without adopting coercive tone

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

## Usage

Ask Codex for a presentation:

```text
Use ultimate-ppt to turn this Word document and website into a polished enterprise sales deck.
```

The skill will guide the agent to:

1. read the source materials
2. create a source brief
3. choose the right deck mode
4. lock strategy and visual direction
5. produce PPTX, HTML, or prompt-board outputs
6. verify the deck before delivery

## Update Log

### 2026-04-27

- Added image-driven PPT guidance: reference-image style transfer, generated hero/case visuals, hybrid bitmap + editable PPT layouts, and safeguards against fake screenshot proof.
- Added anti-repetition rules for image-driven decks: repeat motifs rather than full page skeletons, and redesign runs of near-identical pages.
- Added stage-ready polish rules for direct reporting decks: 3-second glance test, 18 pt body-copy floor, non-overlapping header/footer zones, and no density fixes by shrinking type.
- Added case-spread guidance: split substantial examples into a narrative page and an evidence page so decks can feel fuller without becoming crowded.
- Added source-informed presentation principles from Microsoft PowerPoint accessibility guidance, Duarte audience/message discipline, and Presentation Zen restraint/simplicity guidance.
- Added visual-system guidance for more elegant page variety: claim, comparison, architecture, case story, case proof, scorecard, roadmap, and decision pages.

### 2026-04-26

- Added PPTX layout audit checks for overlapping text boxes, off-slide text, repeated source/footer lines, and high density.
- Added elegance guardrails: density budgets, stable text bounds, centralized footers, and whitespace-first layouts.
- Added richer content guidance for complete decks: background, pain analysis, solution comparison, architecture, core modules, cases, evaluation, roadmap, and future outlook.
- Added multi-style guidance including technical-report pages and Chinese ink-tech presentation direction.
- Added Chinese slide-writing guidance: thesis sentences, fuller case copy, elegant report language, metric explanations, and core-value lines.
- Added live-presentation/readout guidance: larger typography, fewer support blocks per slide, anti-tiny-font checks, and direct-presenting page patterns.

## Repository Structure

```text
skills/ultimate-ppt/SKILL.md
skills/ultimate-ppt/references/
skills/ultimate-ppt/references/content-playbook.md
skills/ultimate-ppt/references/image-driven-ppt.md
skills/ultimate-ppt/references/presentation-readout.md
skills/ultimate-ppt/references/writing-style.md
skills/ultimate-ppt/scripts/audit_deck.py
```

## Validate

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/ultimate-ppt
python skills/ultimate-ppt/scripts/audit_deck.py path/to/output-folder
```

## License

MIT
