from os import listdir
from os.path import isfile, join, isdir

dir = "./"

lst = listdir(dir)  # и файлы и папки

# выбрать только файлы
files = [item for item in lst if isfile(join(dir, item))]

print('\n'.join(files))
