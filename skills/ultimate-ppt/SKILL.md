---
name: ultimate-ppt
description: Use when creating, improving, converting, or evaluating presentations, PPT/PPTX decks, HTML slides, image2PPT/image-to-PPT decks, reference-image style matching, screenshot/PDF/website/old-PPT to deck workflows, pitch decks, keynote-style talks, sales decks, reports, launch decks, training decks, or visual slide systems from documents, images, websites, notes, data, or rough ideas.
---

# Ultimate PPT

Create the strongest possible presentation from source material by combining strategy-first PPT planning, template-driven HTML/PPT execution, magazine-grade storytelling, browser-native slide craft, visual prompt systems, and verification discipline.

Image2PPT is the flagship route: convert reference images into a presentation system, not a stack of screenshots.

## Core Rule

Do not start by writing slides. Start by reading sources and deciding what kind of deck will best win the audience.

Every serious deck must have:
- a clear audience and decision goal
- a delivery context: live presentation, readout document, sales conversation, classroom, or appendix
- an output architecture chosen before layout: editable PPTX, HTML-first, PDF, or hybrid
- an execution lock for serious or multi-format decks: canvas, color, typography, icon, image, rhythm, and forbidden moves
- a narrative spine
- enough context, cases, and proof for the audience to trust the story
- polished slide copy with a clear point of view, not just labels
- a visual system
- a visual grammar proven on representative pages before bulk production
- for image2 work, an image2 brief and visual grammar that explain what was extracted from the reference
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
- tone and writing style: executive, technical, editorial, sales, training, or cultural/ink-tech
- readability target: live-presentation, readout, or appendix
- required footer/source/brand constraints

If the user gives enough information, proceed with reasonable defaults. Ask only when a missing choice would materially change the deck.

### 2. Route the Deck Type

Choose one primary mode and optionally one secondary mode:

| Mode | Use For | Inherits From |
| --- | --- | --- |
| Executive consulting | board, enterprise sales, strategy, procurement | ppt-master |
| Pitch / product launch | fundraising, sales, product story, demo day | html-ppt |
| Editorial keynote | memorable talks, founder vision, thought leadership | guizang |
| Technical report | AI platforms, product systems, research portfolios, architecture reports | ppt-master + guizang |
| Browser-native interactive | animated single-file HTML, modern demos | frontend-slides |
| Visual system / prompt board | art direction, image generation, brand slide assets | PPT-Design-Prompt |
| Image-driven PPT | reference-image style transfer, generated hero/case visuals, premium case showcases | image-driven-ppt + PPT-Design-Prompt |
| Training / course | teaching, workshops, internal enablement | html-ppt + frontend-slides |

If the user provides a reference image, screenshot, PDF page, website capture, old PPT page, product image, brand visual, or rough mockup, route through Image-driven PPT unless the user explicitly wants a plain content deck.

Use the route to shape content, not just visual style. Two different modes should not produce the same outline.

### 3. Strategy Lock

Before slide production, write a compact strategy lock:
- canvas and output format: PPTX, HTML, PDF, or mixed
- delivery architecture: direct PPTX, HTML-first deck, editable-safe HTML, or hybrid image/editable PPTX
- page count range
- audience and desired action
- narrative spine
- slide archetypes
- visual style
- whether a two-page visual grammar pass is required
- color and typography plan
- image/diagram plan
- evidence and citation plan
- presenter notes, motion, export, or conversion needs
- acceptance checks

For image2 work, also create an image2 lock:
- source type and reference sources
- visual grammar extracted from the reference
- transfer level: faithful, inspired, upgraded, or hybrid
- must-editable layer: titles, claims, metrics, charts, labels, diagrams, sources
- bitmap layer: atmosphere, case scene, product context, screenshot frame, texture
- recognition assets: logo, product image, UI screenshot, brand color, typography clues
- image safe-zone strategy
- similarity targets and anti-screenshot-tracing checks

For high-stakes, long, or multi-format decks, save this as `design_spec.md` or `strategy-lock.md` beside the output, then create an `execution-lock.md` with the concrete canvas, colors, fonts, icon language, image inventory, page rhythm, and forbidden moves.

### 4. Build the Content Architecture

Use a deck-specific outline. Avoid generic repeated structures.

Recommended spines:
- Consulting: Problem -> Diagnosis -> Solution architecture -> Proof -> Rollout -> Decision
- Pitch: Problem -> Why now -> Product -> Use cases -> Proof -> Offer -> CTA
- Launch: New reality -> Product moment -> Benefits -> Demo flow -> Proof -> Adoption
- Editorial: Hook -> Context -> Core idea -> Field scenes -> Shift -> Takeaway
- Training: Learning goal -> Concept -> Worked example -> Practice -> Recap
- Visual system: Principles -> Prompt boards -> Asset recipes -> Guardrails -> Handoff
- Technical report: Background -> Gap -> Comparison -> Architecture -> Modules -> Cases -> Evaluation -> Roadmap

For decks that need to feel complete, include a case-and-proof layer:
- one context page that explains why the topic matters now
- one before/after or current-vs-new comparison
- one architecture or operating model diagram
- 2-4 concrete scenario or case pages with situation, intervention, result, reusable asset
- one evaluation or KPI page that explains how success is measured
- one roadmap, handoff, or next-step page

Each slide must have one job. If a slide has two jobs, split it.

Before layout, write a copy layer:
- a slide thesis: the sentence the page must make the audience believe
- 2-4 supporting content blocks with complete, useful wording
- one short core-value line for report-style decks
- speaker/readout notes when nuance would overcrowd the slide

Do not ship pages that only contain headings and tags. If a slide feels thin, enrich the idea with context, mechanism, evidence, implication, or a concrete case detail before decorating it.

For live presentation decks, prioritize stage readability over page density:
- split dense ideas into more slides instead of shrinking text
- use a large claim headline and 1-3 support blocks
- keep normal body copy at presentation scale, typically 18 pt or larger
- pass the 3-second glance test in slide sorter before delivery
- keep detailed evidence in speaker notes, backup, or appendix pages
- avoid tiny labels that only work when zoomed in
- make every slide understandable from thumbnail view
- split substantial cases into a story slide and a proof slide instead of forcing all details into one bento layout

### 5. Visual System

Create a visual system before making pages:
- palette with 2-3 dominant colors and 1 accent
- heading/body/metadata typography roles
- recurring components: cards, metrics, diagrams, timelines, quotes, callouts
- image style or prompt language
- spacing and density rules
- layout/theme tokens and a small layout catalog matched to slide jobs
- style range: choose 2-4 compatible page treatments, not one repeated card layout

If the user asks for a beautiful, premium, high-end, designed, less generic, style-matched, or more impressive deck, or if the visual direction is vague, run a visual direction sprint before making final pages:
- propose 3 distinct visual directions that differ in composition, typography, image treatment, and density, not only color
- recommend one direction based on audience and delivery context
- when the deck has 5+ slides, create or describe a two-page showcase: one high-impact page and one dense content page
- lock the visual grammar before bulk production

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
If visual polish is the main complaint, vary page treatments deliberately: claim, comparison, architecture, case story, case proof, scorecard, roadmap, and decision pages should not all look like the same grid.

For presentation images, treat each image as a slide argument:
- choose the image role: cover hero, divider, concept visual, comparison plate, data backdrop, system plate, case scene, or closing poster
- write the slide thesis before prompting or selecting the image
- reserve 25-35% clean text-safe space when overlay text is expected
- keep titles, metrics, body copy, sources, and proof labels editable unless the user requests flattened poster slides
- avoid stock office scenes, generic AI glow, fake dashboards, and unreadable microtext

For image-driven PPT work, keep the deck hybrid by default:
- images carry atmosphere, product/case context, scene memory, and visual polish
- titles, claims, metrics, diagrams, and sources remain editable PPT objects
- generated images should avoid fake logos, fake UI proof, unreadable in-image text, and cluttered sci-fi AI cliches
- substantial case pages can use a scene image plus editable situation/intervention/result blocks, followed by a proof page with large metrics
- repeat visual motifs, not whole layouts; if pages feel batch-generated, redesign the central composition instead of swapping only titles and icons
- leave an evidence trail: `image2-brief.md`, `visual-grammar.md`, and `run-log.md` or equivalent sections explaining the reference extraction, transfer level, editable layer, bitmap layer, and checks

### 6. Execute in the Best Format

Choose the production path that best matches the goal:

- PPTX: use for editable business deliverables.
- HTML: use for polished browser presentation, animation, keyboard navigation, or single-file sharing.
- Both: use when the user needs a business file plus a visual preview.
- Visual prompt board: use when the task is really about image direction rather than full deck generation.
- Image-driven PPTX: use when the user wants the final deliverable to remain a single editable PPTX but needs stronger hero images, case scenes, or reference-image style matching.

For premium visual decks, prefer an HTML-first source unless the user explicitly needs a directly editable PPTX. Use the HTML deck to establish visual quality, inspect pages in a browser, and then produce PDF/PPTX derivatives as needed.

When editability is required, decide before layout. Do not build a free-form HTML deck with gradients, complex SVG, pseudo-element text, and web components and then promise a fully editable PPTX. Use the editable PPTX path from the beginning or deliver a faithful PDF plus a simplified editable PPTX.

For HTML decks:
- keep every slide within `100vh`
- avoid scrolling inside slides
- use responsive constraints and `clamp()`
- include keyboard navigation
- include notes/presenter script when useful
- for serious decks, use a browser-playable `index.html` with isolated slide files when possible
- for 5+ slides, verify the two-page grammar pass before producing all pages
- use shared theme tokens and known layout archetypes before inventing new classes
- if the deck is a live talk, include hidden speaker notes and verify they are not visible to the audience
- if motion is used, animate semantic blocks and keep static fallback readable

For PPTX decks:
- use real slide dimensions
- keep text inside shapes
- use reusable layouts
- set stable x/y/w/h bounds for every recurring text box
- avoid manual footer duplication; use one footer helper or one master pattern
- after generation, run a layout audit for text overlap and off-slide text
- keep footer/source requirements on the specified pages
- generate speaker notes separately if the library cannot write notes reliably

For PPT conversion or enhancement:
- extract and summarize existing titles, text, notes, images, and slide order before redesign
- decide whether the goal is faithful remake, visual upgrade, or narrative rewrite
- preserve required facts and wording unless the user asks for rewriting
- rebuild the visual system instead of screenshot-tracing by default

### 7. Quality Gates

Before delivery, verify:
- source requirements are represented
- page count and output files exist
- first-slide required footers are present
- every claim with a number has a source or note
- text does not overflow
- visual grammar was tested on representative pages for serious or premium decks
- execution lock was followed for colors, fonts, icons, images, and rhythm where required
- each slide has one clear job
- deck mode shaped the content, not only the colors
- exported/openable files exist
- notes or run log explain key choices

For HTML-first outputs, also verify:
- `index.html` opens and keyboard navigation works
- every slide fits the viewport without internal scrolling
- the two-page showcase and at least one dense page were inspected
- no three consecutive slides look like the same template with swapped text
- presenter notes are hidden from audience slides when present
- export or deployment limitations are reported honestly

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
- `references/execution-lock.md` for serious, long, multi-format, template-based, or consistency-sensitive decks
- `references/layout-theme-system.md` when choosing themes, page archetypes, layout catalogs, presenter notes, image ratios, or reusable HTML deck systems
- `references/style-preset-library.md` when choosing a named visual direction, adapting a reference image into a style preset, or avoiding generic theme choices
- `references/presenter-motion-export.md` when the deck needs live speaker notes, presenter mode, animation, viewport fitting, PPTX conversion intake, PDF export, deployment, or browser editing
- `references/presentation-image-system.md` when generating/selecting cover images, divider images, concept visuals, data backdrops, brand-inspired slide images, or any image intended to carry slide meaning
- `references/visual-direction-showcase.md` when the user asks for a beautiful, premium, polished, designed, high-end, less generic, style-matched, or more impressive deck
- `references/html-first-deck.md` when building HTML decks, visual previews, browser-presentable decks, PDF-ready decks, or decks where first-impression design quality matters
- `references/editable-pptx.md` when the final output must be editable in PowerPoint/Keynote or when converting HTML to editable PPTX
- `references/image2-deck-workflow.md` when the user provides a reference image, screenshot, PDF page, website capture, old PPT page, product image, brand visual, or rough mockup
- `references/image-driven-ppt.md` when the user asks for image-to-PPT, image2PPT, reference-image/PDF style matching, generated presentation images, stronger case visuals, or a deck that feels more like a designed showcase
- `references/presentation-readout.md` when the user needs a PPT that can be presented directly, projected, or read comfortably without zooming
- `references/writing-style.md` when the deck needs richer Chinese copy, elegant wording, fuller slide content, or report-style readout language
- `references/content-playbook.md` when a deck needs richer introductions, more cases, comparisons, evaluation pages, or a technical/report-style structure
- `references/quality-gates.md` for verification checklist

Use `assets/deck_index.html` and `assets/slide.css` as starter files for HTML-first decks when the codebase does not already provide a better presentation shell.

Use `scripts/audit_deck.py` when checking generated PPTX/HTML outputs. Add `--image2` for image-driven decks so the audit also checks the expected image2 evidence files. For PPTX files, treat layout warnings about overlap, off-slide text, duplicate footers, or high density as fix-before-delivery issues unless the user explicitly wants a rough draft.

## Common Mistakes

| Mistake | Correction |
| --- | --- |
| Reusing one outline for every style | Change the content strategy per deck mode |
| Starting from page design before source reading | Build a source brief first |
| Treating visual prompts as a full deck | Use prompt boards as upstream art direction |
| Cramming too much into one slide | Split by job |
| Making a deck "complete" by adding more text | Cut to the decision message, move detail to notes or appendix |
| Making pages too thin with only labels | Add a thesis sentence, mechanism, evidence, implication, or case detail |
| Making pages "complete" by using tiny fonts | Split the story across more slides or move detail to notes/appendix |
| Producing all slides before testing the visual direction | Build a two-page grammar pass first for 5+ slide premium decks |
| Treating HTML and editable PPTX as the same path | Decide editability before layout and load `editable-pptx.md` |
| Making every page the same grid | Repeat motifs, not whole layouts |
| Letting colors/fonts/icons drift page by page | Create and follow `execution-lock.md` |
| Baking long text or metrics into generated images | Keep claims and proof editable; use images for scene and memory |
| Adding motion or presenter text visibly on slides | Use hidden notes and animate semantic blocks only |
| Converting PPTX by tracing screenshots | Extract content, decide remake vs upgrade, then rebuild |
| Using many small cards to look polished | Use fewer large units, clear hierarchy, and whitespace |
| Trusting visual judgment without inspection | Run the PPTX audit and fix overlap/off-slide warnings |
| Saying "done" without checking outputs | Run quality gates and report evidence |

## Completion Standard

A presentation is complete only when it is audience-ready, source-grounded, visually coherent, and verified. The deliverable should include the deck files and a short run log explaining the sources read, route chosen, design decisions, and checks performed.
