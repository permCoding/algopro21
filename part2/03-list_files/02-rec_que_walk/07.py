# стандартное решение

from os import listdir, getcwd, walk
from os.path import isfile, join, isdir


def print_files(cur_dir):
    """
        cur_dir - текущая папка
        sub_dirs - все подпапки
        files - все файлы
    """
    for cur_dir, sub_dirs, files in walk(cur_dir):
        for file in files:
            print(join(cur_dir, file))


# current_dir = getcwd()  # абсолютный путь к текущей папке - get current working directory
current_dir = "."  # относительный путь к текущей папке

print(current_dir)
print_files(current_dir)
