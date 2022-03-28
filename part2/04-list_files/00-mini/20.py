# делаем миниатюры рисунков в заданной папке

from PIL import Image
from os import path
from glob import iglob


def gen_mini_png(inp_dir, out_dir, size, ext):
    for item in iglob(inp_dir + "/*" + ext):  # iglob - это генератор
        file_ext = path.split(item)[1]  # путь | файл
        file, _ = path.splitext(file_ext)  # имя файла | расширение
        with Image.open(item) as img:
            img.thumbnail(size=size)
            img.save(out_dir+"/"+file+".png", "png")


inp_dir, out_dir, ext = "./images", "./mini", ".jpg"
size = (64, 64)
gen_mini_png(inp_dir, out_dir, size, ext)
