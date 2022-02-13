# понизим в два раза яркость у всех пикселей

from PIL import Image

img = Image.open("./images/белка.jpg")

width, height = img.size

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        r //= 2; g //= 2; b //= 2
        color = (r, g, b)
        img.putpixel((x, y), color)

img.show()
