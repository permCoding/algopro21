# сделать градиент
# нужно подогнать под размер рисунка
# чтобы цвет менялся от 0 до 255
# если размеры рисунка 256х256,
# то эта программа будет работать

from PIL import Image

img = Image.open("./images/white.jpg")

width, height = img.size
print(width, height)

for y in range(height):
    for x in range(width):
        r, g, b = y, y, y # очень простой градиент
        img.putpixel((x, y), (r, g, b))

img.show()
