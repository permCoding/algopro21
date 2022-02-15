from os import listdir

lst = listdir("./images")

print('\n'.join(lst))

print()


def check(name_file, ext='.jpg'):
    return name_file.endswith(ext)

check_ = lambda item: item.endswith('.jpg')


# filtred = filter(check_, lst)

# print(list(filtred))

filtred = filter(lambda item: item.endswith('.jpg'), lst)

# filtred = []
# for item in lst:
#     if item.endswith('.jpg'):
#         filtred += [item]  # filtred.append(item)

print('\n'.join(filtred))
