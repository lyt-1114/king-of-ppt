# image2ppt-exact

`image2ppt-exact` 现在只推荐一条路线：

```text
一组 PPT 页面图片
  -> 像素级保底复刻
  -> OCR 提取可编辑文字
  -> 结构化 SVG / Blueprint 原生对象重建
  -> 统一校验日志
  -> 交付一套可追溯的 editable PPT 结果
```

也就是说，用户不需要在 5 条路线里纠结。真正的入口只有一个：

```bash
image2ppt-exact full-rebuild path/to/slides --out path/to/rebuild --force
```

如果你要保留原页面视觉，但不能让原图里的文字和 OCR 文字重复，使用清字背景：

```bash
image2ppt-exact full-rebuild path/to/slides \
  --out path/to/rebuild \
  --background redact \
  --force
```

如果你已经有高保真重建用的 blueprint，再加上：

```bash
image2ppt-exact full-rebuild path/to/slides \
  --out path/to/rebuild \
  --blueprint path/to/deck.blueprint.json \
  --assets-root path/to/assets \
  --force
```

## 核心逻辑

图片版 PPT 转可编辑 PPT 不能靠一句“转成 PPTX”解决，因为目标其实分成三层：

| 层级 | 解决的问题 | 产物 |
| --- | --- | --- |
| 像素保底层 | 原图必须能 100% 看起来一致 | `exact_image_deck.pptx` |
| 文字恢复层 | 页面里的文字要能复制、编辑、改字体 | `editable_text_layer.pptx` |
| 原生重建层 | 形状、线条、图片、面板、标签等尽量恢复成 PPT 对象 | `high_fidelity_editable.pptx` / `native_editable.pptx` |

所以这不是“把一张图塞进 PPT”，而是一个有证据链的重建流程：

1. 先生成像素级保底 PPT，确保视觉不丢。
2. 再跑 OCR，把图片里的文字恢复成 PowerPoint 文本框。
3. 如果需要带背景的可编辑版本，用 `--background redact` 清除原图文字区域，再叠加原生文本框，避免重复文字。
4. 如果有结构化 SVG 或 blueprint，就把形状、线条、图片和组件恢复成原生 PowerPoint 对象。
5. 最后写日志，记录每一层生成了多少页、多少文本框、多少对象。

## 为什么只暴露一条终极路线

包里仍然保留底层命令：

- `export`
- `ocr`
- `editable`
- `image-svg-editable`
- `svg-native-rebuild`
- `blueprint-rebuild`

但这些现在都应该理解为 **内部层 / 调试入口**，不是普通用户要选择的路线。

普通用户只跑：

```bash
image2ppt-exact full-rebuild ...
```

底层命令只在排查问题时使用，比如：

- 只想看像素级复刻是否正确，用 `export`
- 只想检查 OCR 结果，用 `ocr`
- 只想验证文字层，用 `editable`
- 已经有结构化 SVG，想单独测试 SVG 到原生 PPT 对象，用 `svg-native-rebuild`
- 已经有 blueprint，想单独测试高保真对象重建，用 `blueprint-rebuild`

## 安装

在本包目录下安装：

```bash
cd packages/image2ppt-exact
pip install -e .
```

如果需要自动 OCR：

```bash
pip install -e .[ocr]
```

## 最小使用方式

准备一组页面图片：

```text
slides/
  slide_01.png
  slide_02.png
  slide_03.png
```

运行终极路线：

```bash
image2ppt-exact full-rebuild slides --out rebuild --force
```

推荐的可编辑交付版本：

```bash
image2ppt-exact full-rebuild slides --out rebuild --background redact --force
```

默认输出：

```text
rebuild/
  slides_svg/
  index.html
  exact_image_deck.pptx
  ocr_json/
  editable_text_layer.pptx
  editable_text_layer_assets/
  pipeline-execution-log.md
  full-rebuild-log.md
```

如果提供 blueprint：

```bash
image2ppt-exact full-rebuild slides \
  --out rebuild \
  --blueprint deck.blueprint.json \
  --assets-root assets \
  --force
```

会额外输出：

```text
rebuild/
  high_fidelity_editable.pptx
  high_fidelity_editable.blueprint-log.md
```

## 新增的 SVG 原生重建逻辑

`svg-native-rebuild` 是为了吸收 `ppt-master` 的核心思想：  
**只要 SVG 是结构化的，就不要把它当图片贴进去，而要把 SVG 元素翻译成 PowerPoint 原生对象。**

支持的第一批 SVG 元素：

- `<text>` -> PPT 文本框
- `<rect>` -> PPT 矩形 / 圆角矩形
- `<circle>` / `<ellipse>` -> PPT 椭圆
- `<line>` -> PPT 线条
- `<polyline>` / `<polygon>` -> PPT 自由形状
- 简单 `<path>` -> PPT 自由形状
- `<image>` -> PPT 图片对象
- `<g>` -> 递归处理子元素

单独调试命令：

```bash
image2ppt-exact svg-native-rebuild path/to/svg_slides \
  --pptx path/to/native_editable.pptx
```

重要边界：

```text
如果 SVG 里面只是嵌了一张整页 PNG，
那它仍然只是图片，不会自动变成可编辑文字和形状。
```

要真正可编辑，输入必须是结构化 SVG，或者由 AI / 视觉分析先把截图拆成结构化 SVG / blueprint。

## 产物怎么判断

交付时优先看 `full-rebuild-log.md`：

- `Slides`：页数是否一致
- `OCR text blocks`：OCR 识别到多少文字块
- `Editable PPT text boxes`：PPT 里实际生成了多少可编辑文本框
- `Blueprint text/shape/picture/line objects`：高保真重建生成了多少原生对象

如果没有 blueprint，`full-rebuild` 仍然是有效产物，只是高保真对象层会被日志标记为 skipped。

## 源码结构

```text
src/image2ppt_exact/exporter.py     # 像素级图片 / SVG wrapper / PPTX 保底
src/image2ppt_exact/editable.py     # OCR JSON 与可编辑文字层
src/image2ppt_exact/pipeline.py     # 图片 -> SVG proof -> OCR -> editable PPTX
src/image2ppt_exact/native_svg.py   # 结构化 SVG -> 原生可编辑 PPT 对象
src/image2ppt_exact/blueprint.py    # blueprint -> 高保真 PPT 原生对象
src/image2ppt_exact/full_rebuild.py # 终极路线编排
src/image2ppt_exact/cli.py          # 命令行入口
tests/                              # 路线测试
```

## 验证

```bash
cd packages/image2ppt-exact
python -m unittest discover -s tests
image2ppt-exact full-rebuild --help
```
