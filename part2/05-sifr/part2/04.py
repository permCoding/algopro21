# исследуем какие символы кодировать

def ex_1():
    line = '012 ABC abc АБВ абв'
    for char in line:
        print(char, ord(char))


def ex_2():
    ''' соберём алфавит шифрования '''
    eng = 'abcdefghijklmnopqrstuvwxyz'
    rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    nums = '1234567890'
    smbs = ':; !&-+=()*/.,_{}[]#№'
    arr = [chr(9), chr(13), chr(10)]
    alph = eng + eng.upper() + rus + rus.upper() + nums + smbs + ''.join(arr)

    print(alph)
    print(len(alph))


# ex_1()

ex_2()
