from os import listdir
from os.path import isfile, join, isdir


def get_files(dir):  # выбрать только файлы
    lst = listdir(dir)  # и файлы и папки
    return filter(lambda item: isfile(join(dir, item)), lst)


dir = "./images"
for index, file in enumerate(get_files(dir), start=8):
    # index = tpl[0]
    # file = tpl[1]
    print(str(index).rjust(3, ' '), file)
