# переходим на формат файла bmp
# как глубока кроличья нора?

from PIL import Image


name_image = 'белка.bmp'
img = Image.open(name_image)

rastr = img.load()

x = 5; y = 5

color = rastr[x, y]
print(color)

r, g, b = color

bit = 4 # испытываем какой бит можно испортить
shift = 1 << bit # увеличить в 2**bit раз
print(shift)
r -= shift; g -= shift; b -= shift

color = (r, g, b)
print(color)
rastr[x, y] = color

img.save('_' + name_image)
img.show()

# x = 2 # 0010
# x << 1 # 0100 == 4 
# x >> 2 # 0001

x = 3 << 3 
# 000011
# 011000 == 16 + 8 = 24
# print(x)


