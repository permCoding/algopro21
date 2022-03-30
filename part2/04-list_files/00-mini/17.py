from os import listdir
from os.path import isfile, join, getsize


dir = "./images"

lst = listdir(dir)  # и файлы и папки

# выбрать только файлы
files = filter(lambda item: isfile(join(dir, item)), lst)

# преобразовать в кортежи
objs = map(lambda item: (item, getsize(join(dir,item))), files)
# for item in objs:
#     print(item)
# print(list(objs))

# отсортировать по размеру
lst = sorted(objs, key=lambda item: item[1], reverse=True)

for item in lst:
    print(f"{str(item[1]).rjust(12, ' ')} byte\t{item[0]}")
