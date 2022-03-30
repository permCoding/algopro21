from os import listdir
from os.path import isfile, join, isdir
# import os


def ex_01(dir):
    lst = listdir(dir)  # текущая папка
    print('\n'.join(lst))  # и файлы и папки


def ex_02(dir):
    for item in listdir(dir):
        join_path = join(dir, item)
        if isfile(join_path):
            print(f'файл -> {item}')
        if isdir(join_path):
            print(f'папка => {item}')


dir = "."  # так тоже можно обозначать текущую папку
# ex_01(dir)
ex_02(dir)
