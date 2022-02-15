from os import listdir
from os.path import isfile, join, isdir


def get_files(dir):
    global files

    lst = listdir(dir)  # и файлы и папки

    files += [(dir, item) for item in lst if isfile(join(dir, item))]

    cur_dirs = [join(dir, item) for item in lst if isdir(join(dir, item))]
    for next_dir in cur_dirs:
        get_files(next_dir)


files = []
get_files(".")  # текущая папка
for item in files:
    print(join(item[0],item[1]))
