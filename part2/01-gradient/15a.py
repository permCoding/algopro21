# понизим в два раза яркость у всех пикселей

from itertools import count
from PIL import Image
from random import randint

img = Image.open("./images/белка.jpg")

width, height = img.size

count, i = 2000, 0
while i < count:
    i += 1
    cur_x = randint(0, width-1)
    cur_y = randint(0, height-1)
    r, g, b = img.getpixel((cur_x, cur_y))
    r //= randint(1, 5); 
    g //= randint(1, 5); 
    b //= randint(1, 5); 
    color = (r, g, b)
    img.putpixel((cur_x, cur_y), color)

img.show()

# обсудим потом как генерить без повторов
