# прочитаем один символ из несколько подряд идущих пикселей

from PIL import Image
from stegano import get_alph


name_image = '1_белка.bmp'
img = Image.open(name_image)
width, height = img.size
rastr = img.load()

alph = get_alph()
result = ''
x, y = 0, 0
i = 0
while i < 100: # тут недоработка
    pos_b = ''
    for shift in range(8): # это сдвиг по битам символа
        (r,g,b) = rastr[x, y]
        pos_b += str(b&1) # достаём последний бит
        x += 1
        if x == width:
            x = 0
            y += 1
    pos = int(pos_b[::-1], 2)
    i += 1
    # print(pos)
    result += alph[pos]

print(result)
