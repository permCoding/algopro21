# пискели рисунка на символы - компактно

from PIL import Image


def get_image_resize(_img, height_new):
    """ изменить размеры рисунка """
    _width, _height = _img.size  # исходные размеры рисунка
    width_new = _width // (_height // height_new)
    return img.resize((width_new, height_new), Image.ANTIALIAS)


name_image = 'ждун.jpeg'
img = Image.open(name_image)
img_new = get_image_resize(img, 50)  # привести к размеру 50 пикселей

symbols = ' .+#'  # 1 тут добавить больше градаций яркости и подобрать свои символы

# 2 тут код убрать в метод get_image_symbols получение строки символов с картинкой
count = len(symbols)
full = 256 + 256 + 256  # максимальное значение
segment = full // count  # длина сегмента

result = ''
width, height = img_new.size
for y in range(height):
    for x in range(width):
        r, g, b = img_new.getpixel((x, y))
        color = r + g + b
        pos = color // segment
        result += symbols[pos] * 2
    result += '\n'


# 3 тут добавить вывод в текстовый файл
print(result)

# на основе этого кода сделать класс и поместить его в отдельный модуль
