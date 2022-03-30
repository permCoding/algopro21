# делаем миниатюры рисунков в заданной папке

from PIL import Image
from os import path
import glob

size = 64, 64

out_dir = "./mini"

for item in glob.glob("./images/*.jpeg"):
    file, ext = path.splitext(item)
    # print(file)
    file = out_dir + "/" + file.split('\\')[-1]
    with Image.open(item) as img:
        img.thumbnail(size)
        img.save(file + ".png", "png")
