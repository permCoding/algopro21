# запишем один символ в несколько подряд идущих пикселей
# во все три компонента цвета пикселя

from PIL import Image
from stegano import get_alph, get_bit, get_text


alph = get_alph()
text = get_text('block.txt')
name_image = 'белка.bmp'
img = Image.open(name_image)
rastr = img.load()

x, y = 0, 0 # от этой точки будем начинать
i = 0 # индекс символа в шифруемом тексте

# начало блока повтора
smb = text[i]
pos = alph.find(smb)
print(pos)
shift = 0 # это сдвиг по битам позиции символа
for p in range(3):
    (r,g,b) = rastr[x, y]
    r = (r & 254) | get_bit(pos, shift); shift += 1
    g = (g & 254) | get_bit(pos, shift); shift += 1
    b = (b & 254) | get_bit(pos, shift); shift += 1
    rastr[x,y] = (r,g,b)
    x += 1
i += 1
# конец блока повтора

img.save('3_' + name_image)
