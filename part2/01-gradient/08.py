# делаем миниатюры рисунков в текущей папке

from PIL import Image
from os import path
import glob

size = 64, 64

for input in glob.glob("./images/*.jpg"):
    file, ext = path.splitext(input)
    with Image.open(input) as img:
        img.thumbnail(size)
        img.save(file + ".png", "png")
