# очередь

from os import listdir
from os.path import isfile, join, isdir

cur_dir = "."  # текущая папка

dirs = ["."]  # стартуем очередь с текущей папки

while dirs:  # dirs != []
    last = dirs.pop()
    lst = listdir(last)  # и файлы и папки
    files = list(filter(lambda item: isfile(join(last, item)), lst))
    print(last, '\n', files)
    cur_dirs = filter(lambda item: isdir(join(last, item)), lst)
    cur_dirs = list(map(lambda item: join(last, item), cur_dirs))
    dirs = cur_dirs + dirs
    # print(dirs)
