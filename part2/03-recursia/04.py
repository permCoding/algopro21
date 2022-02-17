# очередь

from os import listdir
from os.path import isfile, isdir, join


results = []
dirs = ["."]  # текущая папка

while dirs != []:
    last = dirs.pop()
    lst = listdir(last)  # и файлы и папки

    for file in filter(lambda item: isfile(join(last, item)), lst):
        results.append((last, file))

    cur_dirs = [join(last, item) for item in lst if isdir(join(last, item))]
    dirs = cur_dirs + dirs


for item in results:
    print(join(item[0],item[1]))
