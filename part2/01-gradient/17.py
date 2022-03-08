# понизим неравномерно яркость у всех пикселей

from PIL import Image

img = Image.open("./images/белка.jpg")
width, height = img.size
ky = 256 / height

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        r -= y * ky
        r = 0 if r < 0 else int(r)
        g -= y/9 * ky
        g = 0 if g < 0 else int(g)
        b += y/6 * ky
        b = 255 if b > 255 else int(b)
        img.putpixel((x, y), (r, g, b))

img.show()
