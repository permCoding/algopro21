# пиксели рисунка заменим на символы

from PIL import Image


def get_image_resize(img, height_new):
    ''' изменить размеры рисунка '''    
    width, height = img.size  # исходные размеры рисунка
    width_new = width // (height//height_new)
    img_new = img.resize((width_new, height_new), Image.ANTIALIAS)
    return img_new


name_image = 'ждун.jpeg'
img = Image.open(name_image)
img_new = get_image_resize(img, 50)  # привести к размеру 50 пикселей

symbols = ' .+#'  # эти символы отражают градацию яркости

count = len(symbols)
full = 256 + 256 + 256  # максимальное значение
segment = full // count  # длина сегмента

result = ''
width, height = img_new.size
for y in range(height):
    for x in range(width):
        r, g, b = img_new.getpixel((x, y))
        color = r + g + b
        pos = 0
        if color >= segment * 1:
            pos = 1
        if color >= segment * 2:
            pos = 2
        if color >= segment * 3:
            pos = 3
        result += symbols[pos] * 3
    result += '\n'

print(result)
