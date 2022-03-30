from os import listdir
# from os.path import isfile, join, isdir

cur_dir = "."  # текущая папка

lst = listdir(cur_dir)  # и файлы и папки

print('\n'.join(lst))
