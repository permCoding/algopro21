# делаем миниатюры рисунков в текущей папке

from PIL import Image
from os import path
import glob

dir = "./images"
fltr = "*.jpg"
size = 64, 64

for item in glob.glob(path.join(dir,fltr)):
    file, ext = path.splitext(item)
    with Image.open(item) as img:
        img.thumbnail(size)
        img.save(file + ".png", "png")
