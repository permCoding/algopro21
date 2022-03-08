# изменим размерность рисунка

from PIL import Image


def get_image_resize(img, height_new):    
    width, height = img.size  # исходные размеры рисунка
    width_new = width // (height//height_new)
    img_new = img.resize((width_new, height_new), Image.ANTIALIAS)
    return img_new


name_image = 'ждун.jpeg'
img = Image.open(name_image)
img_new = get_image_resize(img, 100)  # привести к размеру 100 пикселей

print(img_new.size)
img_new.save('1_' + name_image)

