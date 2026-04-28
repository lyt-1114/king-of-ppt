# Blueprint Schema

Blueprint files are JSON documents for building native PowerPoint objects.
Coordinates are measured in the source canvas coordinate system, typically
`1920 x 1080`.

## Top Level

```json
{
  "canvas": { "width": 1920, "height": 1080 },
  "theme": {},
  "slides": []
}
```

## Canvas

```json
{
  "width": 1920,
  "height": 1080,
  "slide_width_in": 13.333,
  "slide_height_in": 7.5
}
```

`slide_width_in` and `slide_height_in` are optional. If omitted, the package uses
`width / 144` and `height / 144`.

## Theme

```json
{
  "font": "Microsoft YaHei",
  "font_size": 12,
  "text": "#f4f8f7",
  "accent": "#01e1d9",
  "panel_fill": "#163f45",
  "muted": "#8ea6a8"
}
```

## Slide

```json
{
  "background": { "color": "#04191c" },
  "elements": []
}
```

`background` can be a color object or an image path:

```json
{ "background": { "image": "background.png" } }
```

## Text Element

```json
{
  "type": "text",
  "x": 120,
  "y": 100,
  "w": 900,
  "h": 90,
  "text": "Title",
  "font_size": 28,
  "bold": true,
  "color": "#f4f8f7",
  "align": "left"
}
```

## Shape Element

```json
{
  "type": "shape",
  "shape": "roundRect",
  "x": 120,
  "y": 260,
  "w": 560,
  "h": 260,
  "fill": "#163f45",
  "line": { "color": "#01e1d9", "width": 1 }
}
```

Supported shapes:

- `rect`
- `roundRect`
- `oval`

## Picture Element

```json
{
  "type": "picture",
  "path": "paper_crop.png",
  "x": 720,
  "y": 80,
  "w": 620,
  "h": 880
}
```

Relative paths are resolved from `--assets-root`, or from the blueprint folder
when `--assets-root` is omitted.

## Line Element

```json
{
  "type": "line",
  "x1": 760,
  "y1": 390,
  "x2": 1100,
  "y2": 390,
  "color": "#99efe9",
  "width": 1.2
}
```

## Component: Panel

```json
{
  "type": "component",
  "name": "panel",
  "x": 120,
  "y": 260,
  "w": 560,
  "h": 260,
  "title": "Native panel",
  "body": "Text, shape, and accent bar are editable."
}
```

## Component: Chip

```json
{
  "type": "component",
  "name": "chip",
  "x": 760,
  "y": 260,
  "w": 240,
  "h": 64,
  "text": "Editable chip"
}
```

## Component: Footer

```json
{
  "type": "component",
  "name": "footer",
  "page": "01",
  "label": "Blueprint",
  "source": "Source: internal materials"
}
```
