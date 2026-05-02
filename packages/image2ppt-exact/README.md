# image2ppt-exact

`image2ppt-exact` 是一个把幻灯片图片转成可交付 PPTX 的工具包。

默认只记住这一条主线就够了：

```bash
image2ppt-exact full-rebuild path/to/slides --out path/to/rebuild --force
```

它会尽量把结果分成三层：

- `exact`：先保留原图外观
- `editable`：再恢复可编辑文字
- `blueprint`：有需要时再做高保真原生对象重建

## 你最常用的结果

- 想要能交付、能编辑的 PPTX，就跑 `full-rebuild`
- 想保留背景但避免文字重复，就加 `--background redact`
- 已经有 blueprint 时，再加 `--blueprint`

## 生成内容

```text
rebuild/
  exact_image_deck.pptx
  ocr_json/
  editable_text_layer.pptx
  full-rebuild-log.md
```

## 安装

```bash
cd packages/image2ppt-exact
pip install -e .
```

OCR 额外依赖：

```bash
pip install -e .[ocr]
```

## 需要细看时

- OCR 可编辑路线: [docs/routes/02-ocr-editable.md](docs/routes/02-ocr-editable.md)
- Blueprint schema: [docs/blueprint-schema.md](docs/blueprint-schema.md)
