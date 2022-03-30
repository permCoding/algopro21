from os import listdir


def ex_01(lst):
    print('\n'.join(lst))
    

def ex_02(lst, ext):
    filtred = []
    for item in lst:
        if item.endswith(ext):
            filtred.append(item)
            # filtred += [item]
    print('\n'.join(filtred))


def ex_03(lst, ext):
    filtred = filter(lambda item: item.endswith(ext), lst)
    print('\n'.join(filtred))


def ex_04(lst, ext):
    filtred = [item for item in lst if item.endswith(ext)]
    print('\n'.join(filtred))


def check(name_file):
    return name_file.endswith(".jpg")


check_ = lambda item: item.endswith(".jpg")


def ex_05(lst):
    # filtred = filter(check, lst)
    filtred = filter(check_, lst)
    print('\n'.join(filtred))


lst = listdir("./images")
# ex_01(lst)
# ex_02(lst, '.jpg')
ex_03(lst, '.jpg')
# ex_04(lst, '.jpg')
# ex_05(lst)
