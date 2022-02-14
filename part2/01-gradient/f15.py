from os import listdir
from os.path import isfile, join, isdir

dir = "./images"

lst = listdir(dir)  # и файлы и папки

# выбрать только файлы
files = list(filter(lambda item: isfile(join(dir, item)), lst))

print('\n'.join(files))
