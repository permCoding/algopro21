from os import listdir
from os.path import isfile, join, isdir


def get_files(dir, ext):
    lst = listdir(dir)  # и файлы и папки
    # выбрать только файлы
    files = filter(lambda item: isfile(join(dir, item)), lst)
    # отфильтровать по расширению
    filtred = filter(lambda item: item.endswith(ext), files)
    return filtred


def list_to_file(list_images, name_file):
    # обработать кириллицу
    # coding = map(lambda item: item.encode('cp1251').decode('1251'), list_images)
    # добавить символ переноса и отсортировать
    lines = sorted(map(lambda item: item+'\n', list_images), reverse=True)
    # f = open(name_file, "w", encoding="utf-8")
    # for line in lines:
    #     f.write(line+'\n')
    # f.close()
    print(lines)
    with open(name_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)


dir = "./images"
list_images = get_files(dir, ".jpg")
list_to_file(list_images, "images.txt")

