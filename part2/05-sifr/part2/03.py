# запишем в последний бит каждого компонента цвета
# в один пиксель только нули

from PIL import Image


name_image = 'белка.bmp'
img = Image.open(name_image)

rastr = img.load()

x = 155; y = 155 # ищем точку где видны изменения

color = rastr[x, y]
print(color)
r, g, b = color

dr = 0; dg = 0; db = 0 # это запишем в младшие биты
# берём самый правый бит
r = (r & 254) | dr
g = (g & 254) | dg
b = (b & 254) | db

color = (r, g, b)
print(color)

rastr[x, y] = color

img.save('_' + name_image)
img.show()
