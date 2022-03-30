from os import listdir
from os.path import isfile, join, isdir


def get_files(dir):  # выбрать только файлы
    lst = listdir(dir)  # и файлы и папки
    files = [item for item in lst if isfile(join(dir, item))]
    print('\n'.join(files))


def get_dirs(dir):  # выбрать только директории
    lst = listdir(dir)  # и файлы и папки
    dirs = [item for item in lst if isdir(join(dir, item))]
    print('\n'.join(dirs))


dir = "."
# get_files(dir)
get_dirs(dir)
