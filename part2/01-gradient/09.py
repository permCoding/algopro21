# делаем миниатюры рисунков в заданной папке

from PIL import Image
from os import path
import glob

size = 64, 64

inp_dir = "./images"
out_dir = "./mini"
imgs_filter = "*.jpg"
imgs_dir = inp_dir + "/" + imgs_filter

for input in glob.glob(imgs_dir):
    file, ext = path.splitext(input)
    file = out_dir + "/" + file.split('\\')[-1]
    # print(file)
    with Image.open(input) as img:
        img.thumbnail(size)
        img.save(file + ".png", "png")
