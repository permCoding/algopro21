from os import listdir, getcwd, walk
from os.path import isfile, join, isdir


def print_files(cur_dir):
    """
        текущая папка, все подпапки, все файлы
        cur_dir, dirs, files
    """
    for cur_dir, dirs, files in walk(cur_dir):
        for file in files:
            print(join(cur_dir,file))


current_dir = getcwd()  # абсолютный путь к текущей папке
current_dir = "."  # относительный путь к текущей папке
print(current_dir)
print_files(current_dir)
