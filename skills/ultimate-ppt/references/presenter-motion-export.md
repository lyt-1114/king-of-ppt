# Presenter, Motion, Viewport, And Export

Use this when the deck will be presented live, exported from HTML, converted from PPTX, or enhanced with animation.

## Core Principle

Motion and presenter tools should clarify the story, not decorate it. Viewport fitting and exportability are non-negotiable.

## Live Presenter Layer

If the user mentions any of these, plan presenter support:

- live talk, speech, keynote, conference, sharing session
- speaker notes, script, teleprompter, presenter view
- "怕忘词", "要讲顺", "逐字稿"

For each slide, write notes that support delivery:

- 150-300 Chinese characters or 90-180 English words for normal talk slides
- shorter notes for title/divider pages
- oral language, not report prose
- one transition sentence at the end
- bold or mark the words the presenter must catch quickly if the runtime supports it

Do not place presenter-only text visibly on the slide.

## Motion Recipes

Use a few named recipes:

| Recipe | Use For | Rule |
| --- | --- | --- |
| `subtle-fade` | business/report pages | 200-400ms, low distance |
| `editorial-cascade` | keynote/editorial pages | stagger title, image, support text |
| `quote-lines` | quote pages | reveal line by line |
| `compare-sides` | before/after or options | left and right enter separately |
| `step-through` | workflows/process | audience advances steps intentionally |
| `hero-reveal` | cover/divider/product moment | slower, more ceremonial |

Animate semantic blocks, not every tiny element. If animation failure would hide content, remove the animation or provide a static fallback.

## Viewport Fitting

For browser decks:

- every slide must fit within the viewport
- no scrolling inside a slide
- no content hidden behind browser chrome, footer, or navigation
- split dense content instead of shrinking type
- images need max-height rules
- test at 16:9 desktop and at a shorter 1280x720-like viewport

If a slide overflows, the fix order is:

1. split into two slides
2. move detail to notes or appendix
3. simplify layout
4. only then reduce secondary text

Do not solve overflow by making important text tiny.

## PPTX Conversion Intake

When converting or improving an existing PPTX:

1. Extract slide titles, text, notes, and media.
2. Summarize the existing deck structure.
3. Identify which slides are content keepers, which are redundant, and which need redesign.
4. Choose whether the output is faithful remake, visual upgrade, or narrative rewrite.
5. Preserve facts and required wording unless the user asks for rewriting.

Never treat PPTX conversion as screenshot tracing by default. The better upgrade often keeps the content and rebuilds the visual system.

## Export Discipline

For HTML -> PDF:

- use a browser renderer
- capture every slide at the intended canvas
- verify image loading via local server when relative assets are used
- open the resulting PDF or inspect page count
- report that animations become static snapshots

For HTML -> PNG:

- use a fixed viewport such as 1920x1080
- capture each slide by index or hash
- inspect at least cover, one dense page, and one image page

For deployment:

- prefer folder deployment when the deck has assets
- verify local images, fonts, and scripts load after deployment
- avoid absolute filesystem paths

## Inline Editing

Only include browser editing controls when the user asks for in-browser editing.

If enabled:

- keep editing UI out of exported/saved files
- avoid hover chains that disappear before click
- save clean HTML without active edit states
- make it obvious that this is not PowerPoint editability

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Adding motion to every object | Animate semantic blocks |
| Letting a browser slide scroll | Split the slide |
| Writing visible presenter instructions | Put them in notes |
| Promising PDF preserves animation | Explain it is static |
| Converting PPTX by screenshot tracing | Extract content and rebuild intentionally |
| Adding edit UI without cleanup | Strip edit state before saving |
