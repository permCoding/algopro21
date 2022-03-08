# изменяем значение цвета в младшем разряде центрального пикселя

from PIL import Image


name_image = 'white.jpg'
img = Image.open(name_image)
width, height = img.size  # исходные размеры рисунка

x = width//2; y = height//2

r, g, b = img.getpixel((x, y))
r -= 4; g -= 4; b -= 4

print(r, g, b)

color = (r, g, b)
img.putpixel((x, y), color)

img.save('_' + name_image)
img.show()
