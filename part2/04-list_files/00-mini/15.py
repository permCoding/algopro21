from os import listdir
from os.path import isfile, join, isdir


def get_files(dir):  # выбрать только файлы
    lst = listdir(dir)  # и файлы и папки
    return filter(lambda item: isfile(join(dir, item)), lst)


dir = "./images"
for i, file in enumerate(get_files(dir)):
    print(str(i+1).ljust(3, ' '), file)
