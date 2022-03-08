# модуль для стеганографии


def get_alph():
    eng = 'abcdefghijklmnopqrstuvwxyz'
    rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    nums = '1234567890'
    smbs = ':; !&-+=()*/.,_{}[]#№'
    arr = [chr(9), chr(13), chr(10), chr(0)]
    alph = rus + rus.upper() + eng + eng.upper() + nums + smbs + ''.join(arr)
    return alph


def get_text(file_name):
    with open(file_name, mode='r', encoding='utf-8') as f:
        text = f.read()
    return text


def get_bit(pos, shift):
    mask = 1 << shift # формируем маску
    sign = (pos & mask) >> shift # узнаём значение бита
    return sign

