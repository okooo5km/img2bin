# img2bin

二值化图像工具。这个工具可以将图像文件或目录中的图像文件转换为二值化图像。

## 安装

首先，确保你已经安装了 Python 和 Poetry。然后，你可以使用以下命令来安装 img2bin：

```bash
poetry install
```

在撰写 README.md 文件时，你可能需要包括以下几个部分：

1. 项目的简介和目的
2. 安装指南
3. 如何使用你的工具
4. 示例
5. 贡献指南
6. 许可证信息

根据你的 `img2bin/main.py` 文件，以下是一个可能的 README.md 文件的草案：

```markdown
# img2bin

二值化图像工具。这个工具可以将图像文件或目录中的图像文件转换为二值化图像。

## 安装

首先，确保你已经安装了 Python 和 Poetry。然后，你可以使用以下命令来安装 img2bin：

```bash
poetry install
```

## 使用

你可以使用 `img2bin` 命令来二值化一个图像文件或目录中的所有图像文件。以下是一些示例：

```bash
# 二值化一个图像文件
img2bin /path/to/image.png --threshold 128

# 二值化一个目录中的所有图像文件
img2bin /path/to/directory --threshold 128
```

在这些命令中，`--threshold` 参数是可选的，它指定了二值化的阈值。默认值是 128。

## 示例

以下是一些使用 img2bin 的示例：

```bash
# 二值化一个图像文件，使用默认的阈值
img2bin image.png

# 二值化一个图像文件，使用自定义的阈值
img2bin image.png --threshold 200

# 二值化一个目录中的所有图像文件，使用自定义的阈值
img2bin images/ --threshold 200
```

## 贡献

欢迎任何形式的贡献。如果你发现了任何问题，或者有任何建议，可以通过 GitHub 提交 issue 或 pull request。
