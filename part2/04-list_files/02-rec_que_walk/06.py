# рекурсия

from os import listdir, getcwd
from os.path import isfile, join, isdir


def get_files(cur_dir):
    global files

    lst = listdir(cur_dir)  # и файлы и папки

    files += [(cur_dir, elm) for elm in lst if isfile(join(cur_dir, elm))]

    sub_dirs = [join(cur_dir, elm) for elm in lst if isdir(join(cur_dir, elm))]

    for next_dir in sub_dirs:
        get_files(next_dir)


files = []
current_dir = getcwd()  # абсолютный путь к текущей папке
print(current_dir)
get_files(current_dir)  # текущая папка
for item in files:
    print(join(item[0], item[1]))
