from os import listdir
from os.path import isfile, join, isdir

dir = "./"  # текущая папка

lst = listdir("./")  # и файлы и папки

for item in lst:
    join_path = join(dir, item)
    if isfile(join_path):
        print(f'файл -> {item}')
    if isdir(join_path):
        print(f'папка => {item}')
