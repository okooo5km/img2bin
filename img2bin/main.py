# Desc: 图像二值化工具
import typer
from PIL import Image
import os
from pathlib import Path
from typing import List


def process_image(input_path: Path, threshold: int):
    # 打开图像
    typer.echo(f"\n处理图像 {input_path}")
    image = Image.open(input_path)
    # 将图像转换为灰度图像
    gray_image = image.convert("L")
    # 使用提供的阈值进行二值化处理
    binary_image = gray_image.point(lambda x: 255 if x > threshold else 0, '1')
    # 构建输出路径
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{input_path.stem}-bin{input_path.suffix}"
    # 保存处理后的图像
    binary_image.save(output_path)
    typer.echo(f"  保存到 {output_path}, 完成!", color=typer.colors.YELLOW)


def process(threshold: int = typer.Option(128, '--threshold', '-t', help="二值阈值"),
            input: str = typer.Argument(..., help="输入文件或目录路径")):
    input_path = Path(input)
    if input_path.is_file():
        # 如果是文件，直接处理
        process_image(input_path, threshold)
    elif input_path.is_dir():
        # 如果是目录，遍历目录
        for root, dirs, files in os.walk(input_path):
            for file in files:
                # 检查文件扩展名是否为图像文件
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    file_path = Path(root) / file
                    process_image(file_path, threshold)


def main():
    typer.run(process)
