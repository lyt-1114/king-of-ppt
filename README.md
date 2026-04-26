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
npx skills add https://github.com/YOUR_NAME/ultimate-ppt-skill
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

## Repository Structure

```text
skills/ultimate-ppt/SKILL.md
skills/ultimate-ppt/references/
skills/ultimate-ppt/scripts/audit_deck.py
```

## Validate

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/ultimate-ppt
python skills/ultimate-ppt/scripts/audit_deck.py path/to/output-folder
```

## License

MIT
