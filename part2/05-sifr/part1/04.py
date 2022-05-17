# теперь сделаем функции кодирования и декодирования
# при кодировании сдвигаем позицию символа на +key
# при декодировании сдвигаем позицию обратно на -key

def code(line, key):  # функция кодирования
    return ''.join([chr(ord(smb)+key) for smb in line])


def decode(line, key):  # функция декодирования
    return ''.join([chr(ord(smb)-key) for smb in line])


key = 9  # величина сдвига
line = 'Привед Медвед...'  # исходная строка
print(line)

line_code = code(line, key)
print(line_code)  # зашифрованная строка

line_decode = decode(line_code, key)
print(line_decode)  # расшифрованная строка
