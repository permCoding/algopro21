from os import listdir
from os.path import isfile, join, isdir

cur_dir = "."  # текущая папка

lst = listdir(cur_dir)  # и файлы и папки

for item in lst:
    join_path = join(cur_dir, item)
    if isfile(join_path):
        print(f'файл -> {item}')
    if isdir(join_path):
        print(f'папка => {item}')
