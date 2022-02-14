from os import listdir
from os.path import isfile, join, isdir

lst = listdir("./")  # текущая папка

print('\n'.join(lst))  # и файлы и папки

print()

dir = "./"
for item in listdir(dir):
    join_path = join(dir, item)
    if isfile(join_path):
        print(f'файл -> {item}')
    if isdir(join_path):
        print(f'папка => {item}')
