import json
import subprocess
from pathlib import Path
from pdf2image import convert_from_path
import ocrmypdf

# PDFファイルのパス
pdf_path = Path("./dummy.pdf")


# outputのファイルパス
img_path = Path("./output")


def handler(event, content):

    print("Hello World !!!")
    try:
        convert_from_path(
            pdf_path, output_folder=img_path, fmt="jpeg", output_file=pdf_path.stem
        )
        ret = subprocess.run(
            ["pdftoppm", "--help"], capture_output=True, text=True, check=True
        )
        print("return code", ret.returncode)
        print("standard out put", ret.stdout)
    except subprocess.CalledProcessError as e:
        print(e.cmd)
        print(e.returncode)
        print(e.output)
        print(e.stdout)
        print(e.stderr)
    return "hello world"
