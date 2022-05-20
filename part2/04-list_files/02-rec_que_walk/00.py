from os import listdir, stat
from os.path import isfile, getsize

# текущую папку - где расположена программа можно указать так "."

for item in listdir("."):  # и файлы и папки
    if isfile(item):  # если файл
        print(f'{stat(item).st_size}b / {getsize(item)}b - {item}')
        # два способа узнать размер файла stat(item).st_size / getsize(item)
