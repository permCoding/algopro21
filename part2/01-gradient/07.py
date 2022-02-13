# делаем миниатюры рисунков в текущей папке

from PIL import Image

size = 64, 64

with Image.open("./images/белка.jpg") as img:
    img.resize(size).show()
