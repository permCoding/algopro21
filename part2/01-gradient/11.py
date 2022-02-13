# сделать градиент, нужно подогнать под размер рисунка
# чтобы цвет менялся от 0 до 255
# в этой программе введём коэффициент, 
# чтобы работало для рисунка любого размера

from PIL import Image

img = Image.open("./images/white444.jpg")

width, height = img.size

kx = 256 / width # добавим коэффициент для пересчёта
ky = 256 / height # добавим коэффициент для пересчёта

for y in range(height):
    for x in range(width):
        # clr = int(ky * y)
        clr = int(kx * x)
        r, g, b = clr, clr, clr
        img.putpixel((x, y), (r, g, b))

img.show()
