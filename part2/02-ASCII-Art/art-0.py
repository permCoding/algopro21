# pip3 install pillow
# изменим размерность рисунка

from PIL import Image


def get_image_resize(img, k):
    width, height = img.size  # исходные размеры рисунка
    width *= k; height *= k
    img_new = img.resize((int(width), int(height)), Image.ANTIALIAS)
    return img_new


name_image = 'ждун.jpeg'
img = Image.open(name_image)
k = 1/2  # коэффициент увеличения
img_new = get_image_resize(img, k)

print(img_new.size)
img_new.save('0_' + name_image)
