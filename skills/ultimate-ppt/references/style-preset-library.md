# Style Preset Library

Use this when the user wants a beautiful deck but has not supplied a clear design system, or when image2 work needs a named visual direction before production.

## Core Rule

Choose a style by audience, evidence type, and reference image behavior. Do not choose by color alone.

For image2 decks, use the reference image to select or adapt one preset, then record the result in `visual-grammar.md`.

## Presets

| Preset | Best For | Visual Signals | Avoid |
| --- | --- | --- | --- |
| Executive Editorial | board decks, founder vision, strategy keynote | large claims, restrained palette, serif/sans contrast, sparse proof | tiny consulting grids on every page |
| Consulting Precision | enterprise sales, procurement, operating model | tight grid, clean tables, sober accents, source discipline | decorative image-heavy pages without evidence |
| Product Cinema | launches, product stories, demos | hero image, feature flow, large screenshots, dramatic dividers | fake UI, stock device mockups |
| Technical Atlas | AI systems, architecture, research, platform reports | diagrams, maps, scorecards, mono metadata, traceable logic | unreadable micro labels |
| Magazine Casebook | case studies, customer stories, industry examples | image spreads, captions, story/proof pairs, editorial rhythm | repeated card grids |
| Paper Ink Tech | Chinese reports, cultural tech, education, policy | warm paper, ink-dark typography, calm charts, subtle lines | beige monotony or faux-traditional decoration |
| Interface Native | SaaS, workflow, dashboards, internal tools | real screenshots, browser frames, UI rhythm, component annotation | copying website layout as slides |
| Data Command | KPI reviews, analytics, ops, finance | bold metrics, high-contrast charts, evidence strips, alert accent | too many dashboards per slide |
| Premium Minimal | investor summaries, high-end brand decks | wide whitespace, product closeups, restrained typography | empty luxury decoration |
| Bold Signal | campaign, announcement, call-to-action | high contrast, one accent, oversized message, poster moments | making every slide a poster |
| Workshop Clarity | training, courses, enablement | clear modules, examples, practice pages, friendly diagrams | over-designed pages that slow learning |
| Dark Systems | technical talks, cybersecurity, AI infrastructure | dark canvas, luminous linework, structured motion, code/graph accents | default purple-blue AI glow |

## Selection Heuristic

1. Identify the audience: executives, buyers, engineers, students, public audience, or internal team.
2. Identify the proof type: numbers, cases, screenshots, architecture, product visuals, process, or narrative.
3. Identify the reference behavior: editorial, UI-native, cinematic, report-like, poster-like, or diagrammatic.
4. Pick one preset as the base and one as a modifier.
5. Write the merged style in one sentence:

```text
Base preset: Technical Atlas.
Modifier: Magazine Casebook.
Result: a structured AI architecture deck with editorial case spreads and traceable proof pages.
```

## Preset-To-Layout Mapping

| Preset | High-Impact Page | Dense Page | Proof Page |
| --- | --- | --- | --- |
| Executive Editorial | editorial claim | statement plus evidence | decision summary |
| Consulting Precision | board thesis | option matrix | KPI table |
| Product Cinema | product hero | feature flow | user proof |
| Technical Atlas | system map | architecture diagram | scorecard |
| Magazine Casebook | photo spread | case storyboard | metrics follow-up |
| Paper Ink Tech | chapter poster | report grid | evaluation page |
| Interface Native | screenshot hero | annotated workflow | before/after UI |
| Data Command | metric wall | operations map | KPI strip |
| Premium Minimal | product closeup | two-column proof | concise metric page |
| Bold Signal | campaign poster | comparison | CTA page |
| Workshop Clarity | learning promise | worked example | recap |
| Dark Systems | network hero | layered system | incident/proof log |

## Image2 Adaptation

When the reference image conflicts with the chosen preset:

- preserve the reference's strongest recognition cue
- keep the preset's layout and readability discipline
- record what changed in `visual-grammar.md`
- do not force the whole deck to mimic one screenshot if the deck needs varied slide jobs

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Picking a preset because the colors look close | Match composition, density, typography, and proof type |
| Applying one preset to every slide identically | Repeat motifs and vary central composition |
| Mixing three presets equally | Pick one base, one modifier |
| Choosing cinematic style for dense reports | Use cinematic moments only for covers/dividers/case scenes |
| Choosing consulting precision for keynote moments | Add editorial or product-cinema pages for rhythm |
