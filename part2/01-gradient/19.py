# придумаем градиентную заливку

from PIL import Image

img = Image.open("./images/white.jpg")
width, height = img.size
ky = 256 / height
kx = 256 / width

for y in range(height):
    for x in range(width):
        r = int(y * ky)
        g = int(x * kx)
        b = int(255 - (y*ky))
        img.putpixel((x, y), (r, g, b))

img.save('./gradients/_' + '98.jpg')
img.show()
