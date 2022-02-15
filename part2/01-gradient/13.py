# инверсия rgb-рисунка

from PIL import Image

img = Image.open("./images/ждун.jpeg")

width, height = img.size

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x,y))
        # r = 255 - r
        # g = 255 - g
        b = 255 - b
        img.putpixel((x, y), (r,g,b))

img.show()
