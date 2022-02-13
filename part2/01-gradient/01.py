# rgb-компоненты разных точек рисунка

from PIL import Image

img = Image.open("./images/color.jpg")

print(img.size)
width, height = img.size

point1 = (0, 0)
point2 = (width-1, 0)
point3 = (0, height-1)
point4 = (width-1, height-1)

for point in point1, point2, point3, point4:
    color = img.getpixel(point)
    r, g, b = color
    print(f'r = {r}, g = {g}, b = {b}')
