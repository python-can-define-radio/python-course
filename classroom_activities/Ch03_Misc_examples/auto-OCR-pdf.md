This example assumes a very specific setup:
 
 - You have imagemagick and tesseract-ocr installed
 - you have a pdf named "name_of_your_file.pdf" in your working directory

```python3
import subprocess

for i in range(80):
    subprocess.run(["convert",
                    "-density",
                    "150",
                    f"name_of_your_file.pdf[{i}]",
                    f"output_{str(i).zfill(3)}.png"
                    ])


for i in range(80):
    subprocess.run([
        "tesseract",
        f"output_{str(i).zfill(3)}.png",
        f"output_{str(i).zfill(3)}.txt",
        "-l",
        "eng"])
```
