# прочитаем один символ из несколько подряд идущих пикселей

from PIL import Image
from stegano import get_alph


alph = get_alph()
name_image = '3_белка.bmp'
img = Image.open(name_image)
rastr = img.load()

x, y = 0, 0

# начало блока повтора
shift = 0
pos_b = ''
for p in range(3):
    (r,g,b) = rastr[x, y]
    pos_b += str(r&1); shift += 1
    pos_b += str(g&1); shift += 1
    pos_b += str(b&1); shift += 1
    x += 1
pos = int(pos_b[::-1], 2)
print(pos)
print(alph[pos])
# конец блока повтора

