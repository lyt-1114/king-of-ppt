---
name: ultimate-ppt
description: Use when creating, improving, converting, or evaluating presentations, PPT/PPTX decks, HTML slides, pitch decks, keynote-style talks, sales decks, reports, launch decks, training decks, or visual slide systems from documents, websites, notes, data, or rough ideas.
---

# Ultimate PPT

Create the strongest possible presentation from source material by combining strategy-first PPT planning, template-driven HTML/PPT execution, magazine-grade storytelling, browser-native slide craft, visual prompt systems, and verification discipline.

## Core Rule

Do not start by writing slides. Start by reading sources and deciding what kind of deck will best win the audience.

Every serious deck must have:
- a clear audience and decision goal
- a narrative spine
- a visual system
- a density budget before layout
- source-backed claims
- speaker/readout notes when useful
- verification before delivery

## Workflow

### 1. Intake and Source Reading

Read all supplied materials before outlining:
- documents: DOCX, PDF, PPTX, Markdown, text files
- URLs and websites
- images, logos, screenshots, charts, tables
- user instructions in the conversation

Create a short source brief with:
- audience
- goal
- required facts
- strongest proof points
- risks, gaps, and assumptions
- required footer/source/brand constraints

If the user gives enough information, proceed with reasonable defaults. Ask only when a missing choice would materially change the deck.

### 2. Route the Deck Type

Choose one primary mode and optionally one secondary mode:

| Mode | Use For | Inherits From |
| --- | --- | --- |
| Executive consulting | board, enterprise sales, strategy, procurement | ppt-master |
| Pitch / product launch | fundraising, sales, product story, demo day | html-ppt |
| Editorial keynote | memorable talks, founder vision, thought leadership | guizang |
| Browser-native interactive | animated single-file HTML, modern demos | frontend-slides |
| Visual system / prompt board | art direction, image generation, brand slide assets | PPT-Design-Prompt |
| Training / course | teaching, workshops, internal enablement | html-ppt + frontend-slides |

Use the route to shape content, not just visual style. Two different modes should not produce the same outline.

### 3. Strategy Lock

Before slide production, write a compact strategy lock:
- canvas and output format: PPTX, HTML, PDF, or mixed
- page count range
- audience and desired action
- narrative spine
- slide archetypes
- visual style
- color and typography plan
- image/diagram plan
- evidence and citation plan
- acceptance checks

For high-stakes decks, save this as `design_spec.md` or `strategy-lock.md` beside the output.

### 4. Build the Content Architecture

Use a deck-specific outline. Avoid generic repeated structures.

Recommended spines:
- Consulting: Problem -> Diagnosis -> Solution architecture -> Proof -> Rollout -> Decision
- Pitch: Problem -> Why now -> Product -> Use cases -> Proof -> Offer -> CTA
- Launch: New reality -> Product moment -> Benefits -> Demo flow -> Proof -> Adoption
- Editorial: Hook -> Context -> Core idea -> Field scenes -> Shift -> Takeaway
- Training: Learning goal -> Concept -> Worked example -> Practice -> Recap
- Visual system: Principles -> Prompt boards -> Asset recipes -> Guardrails -> Handoff

Each slide must have one job. If a slide has two jobs, split it.

### 5. Visual System

Create a visual system before making pages:
- palette with 2-3 dominant colors and 1 accent
- heading/body/metadata typography roles
- recurring components: cards, metrics, diagrams, timelines, quotes, callouts
- image style or prompt language
- spacing and density rules

Create an elegance lock before production:
- one job per slide, one dominant message, one visual rhythm
- no nested cards; use fewer, larger objects with visible whitespace
- prefer 2-4 large units over 6-10 small cards
- keep body copy short enough to read at presentation distance
- reserve screenshot/detail pages for pages where inspection matters
- choose fewer colors and repeat them consistently

Avoid generic AI slide aesthetics:
- purple-blue gradients by default
- empty bento grids
- decorative blobs
- stock-looking abstract people
- robotic handshake imagery
- crowded text walls

Use visual assets when the subject benefits from them: logos, website captures, product screenshots, generated imagery, diagrams, charts, and icons.

### 6. Execute in the Best Format

Choose the production path that best matches the goal:

- PPTX: use for editable business deliverables.
- HTML: use for polished browser presentation, animation, keyboard navigation, or single-file sharing.
- Both: use when the user needs a business file plus a visual preview.
- Visual prompt board: use when the task is really about image direction rather than full deck generation.

For HTML decks:
- keep every slide within `100vh`
- avoid scrolling inside slides
- use responsive constraints and `clamp()`
- include keyboard navigation
- include notes/presenter script when useful

For PPTX decks:
- use real slide dimensions
- keep text inside shapes
- use reusable layouts
- set stable x/y/w/h bounds for every recurring text box
- avoid manual footer duplication; use one footer helper or one master pattern
- after generation, run a layout audit for text overlap and off-slide text
- keep footer/source requirements on the specified pages
- generate speaker notes separately if the library cannot write notes reliably

### 7. Quality Gates

Before delivery, verify:
- source requirements are represented
- page count and output files exist
- first-slide required footers are present
- every claim with a number has a source or note
- text does not overflow
- each slide has one clear job
- deck mode shaped the content, not only the colors
- exported/openable files exist
- notes or run log explain key choices

For PPTX outputs, also verify:
- no non-empty text boxes overlap except intentional labels inside their own shape
- no text box extends outside the slide canvas
- no slide exceeds the density budget for its archetype
- no page has duplicate footers, duplicate page numbers, or repeated source lines
- the deck still reads clearly when slide thumbnails are viewed at small size

If any gate fails, revise the deck. Do not claim completion without evidence.

## Required References

Load these only when needed:
- `references/workflow.md` for the full end-to-end process
- `references/modes.md` for deck-type routing and outline patterns
- `references/visual-system.md` for style selection and image prompt rules
- `references/quality-gates.md` for verification checklist

Use `scripts/audit_deck.py` when checking generated PPTX/HTML outputs. For PPTX files, treat layout warnings about overlap, off-slide text, duplicate footers, or high density as fix-before-delivery issues unless the user explicitly wants a rough draft.

## Common Mistakes

| Mistake | Correction |
| --- | --- |
| Reusing one outline for every style | Change the content strategy per deck mode |
| Starting from page design before source reading | Build a source brief first |
| Treating visual prompts as a full deck | Use prompt boards as upstream art direction |
| Cramming too much into one slide | Split by job |
| Making a deck "complete" by adding more text | Cut to the decision message, move detail to notes or appendix |
| Using many small cards to look polished | Use fewer large units, clear hierarchy, and whitespace |
| Trusting visual judgment without inspection | Run the PPTX audit and fix overlap/off-slide warnings |
| Saying "done" without checking outputs | Run quality gates and report evidence |

## Completion Standard

A presentation is complete only when it is audience-ready, source-grounded, visually coherent, and verified. The deliverable should include the deck files and a short run log explaining the sources read, route chosen, design decisions, and checks performed.
