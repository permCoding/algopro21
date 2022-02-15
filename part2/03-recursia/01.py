from os import listdir
from os.path import isfile, join, isdir

dir = "./"  # текущая папка

lst = listdir("./")  # и файлы и папки

print('\n'.join(lst))
