from os import listdir, stat
from os.path import isfile, getsize

for item in listdir("."):  # и файлы и папки
    if isfile(item):  # если файл
        print(f'{stat(item).st_size}b / {getsize(item)}b - {item}')
        # два способа узнать размер файла stat(item).st_size / getsize(item)
