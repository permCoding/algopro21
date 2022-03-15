# запишем один символ в несколько подряд идущих пикселей
# только в один компонент цвета каждого пикселя

from PIL import Image
from stegano import get_alph, get_bit, get_text

alph = get_alph() # загружаем алфавит
text = get_text('block.txt') # загружаем текст

name_image = 'белка.bmp'
img = Image.open(name_image) # загружаем рисунок
width, height = img.size # исходные размеры рисунка
rastr = img.load() # в двумерную матрицу для удобства


x, y = 0, 0 # начнём с левого верхнего пикселя
i = 0 # индекс символа в шифруемом тексте
while i < len(text): # пока не достигли конца текста

    smb = text[i] # берём очередной символ из текста
    pos = alph.find(smb) # узнаём его позицию в алфавите
    # эту позицию и будем записывать в пиксели рисунка
    # print(pos) # это просто для контроля

    # будем записывать биты двоичного представления позиции
    for shift in range(8): # пробегаем по всем битам позиции символа
        (r,g,b) = rastr[x, y]
        b = (b & 254) | get_bit(pos, shift)
        rastr[x,y] = (r,g,b)
        x += 1
        if x == width:
            x = 0
            y += 1
    i += 1

img.save('1_' + name_image)

# нет контроля: если текст больше, чем может вместить рисунок