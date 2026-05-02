# image2ppt-exact

`image2ppt-exact` 是一个把整页幻灯片图片转换成可交付 PPTX 的工具包。

它的目标很简单：

- 先保留像素级外观
- 再恢复可编辑文本
- 需要时再做更高保真的原生对象重建

## 它能做什么

- `exact export`：导出像素一致的 proof 资产
- `ocr editable`：把图片里的文字恢复成可编辑文本框
- `image-svg-editable`：一条命令跑完 exact + OCR + editable 校验
- `svg-native-rebuild`：把结构化 SVG 重建为原生 PPT 对象
- `blueprint-rebuild`：按 blueprint 生成高保真可编辑 PPTX
- `full-rebuild`：推荐主路径，串起整条可追溯流程

## 推荐怎么用

如果你只是想把一套批准后的页面图片转成可编辑 PPT，默认直接用：

```bash
image2ppt-exact full-rebuild path/to/slides --out path/to/rebuild --force
```

如果你想保留背景但去掉 OCR 文本区域：

```bash
image2ppt-exact full-rebuild path/to/slides \
  --out path/to/rebuild \
  --background redact \
  --force
```

如果你已经有 blueprint，还可以继续做高保真重建：

```bash
image2ppt-exact full-rebuild path/to/slides \
  --out path/to/rebuild \
  --blueprint path/to/deck.blueprint.json \
  --assets-root path/to/assets \
  --force
```

## 输出层次

这个包把结果分成三层：

| 层次 | 作用 | 产物 |
| --- | --- | --- |
| exact | 保证画面不走样 | `exact_image_deck.pptx` |
| editable | 恢复可编辑文字 | `editable_text_layer.pptx` |
| blueprint | 重建原生 PPT 对象 | `high_fidelity_editable.pptx` |

## 文档入口

- OCR 可编辑路线: [docs/routes/02-ocr-editable.md](docs/routes/02-ocr-editable.md)
- 图片到 SVG 再到可编辑路线: [docs/routes/03-image-svg-editable.md](docs/routes/03-image-svg-editable.md)
- Blueprint 重建路线: [docs/routes/04-blueprint-rebuild.md](docs/routes/04-blueprint-rebuild.md)
- Exact 导出路线: [docs/routes/01-exact-export.md](docs/routes/01-exact-export.md)
- Blueprint schema: [docs/blueprint-schema.md](docs/blueprint-schema.md)

## 安装

```bash
cd packages/image2ppt-exact
pip install -e .
```

OCR 额外依赖：

```bash
pip install -e .[ocr]
```

## 最小示例

```text
slides/
  slide_01.png
  slide_02.png
```

```bash
image2ppt-exact full-rebuild slides --out rebuild --force
```

默认会生成：

```text
rebuild/
  slides_svg/
  index.html
  exact_image_deck.pptx
  ocr_json/
  editable_text_layer.pptx
  full-rebuild-log.md
```

## 代码结构

```text
src/image2ppt_exact/exporter.py
src/image2ppt_exact/editable.py
src/image2ppt_exact/pipeline.py
src/image2ppt_exact/native_svg.py
src/image2ppt_exact/blueprint.py
src/image2ppt_exact/full_rebuild.py
src/image2ppt_exact/cli.py
tests/
```

