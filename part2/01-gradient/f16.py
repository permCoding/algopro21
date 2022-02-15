from os import listdir
from os.path import isfile, join, isdir

dir = "./images"

lst = listdir(dir)  # и файлы и папки

# выбрать только файлы
files = filter(lambda item: isfile(join(dir, item)), lst)

# отфильтровать по расширению
filtred = filter(lambda item: item.endswith('.jpg'), files)

# print('\n'.join(list(filtred)))  # если включить, то filtred исчерпается

# f = open('tmp.txt', 'w')
# f.write(list(filtred)[-1])
# f.close()

# обработать кириллицу
coding = map(lambda item: item.encode('cp1251').decode('1251'), filtred)

# добавить символ переноса и отсортировать
lines = sorted(map(lambda item: item + '\n', coding), reverse=True)

# print(lines)  # вот тут можно проверить пустоту списка

with open('files.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# # print(type(u))
