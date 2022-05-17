# применение XOR для шифрования/дешифрования строки
# одна функция применяется и для шифрования и для дешифрации

def code(line, key):
    return ''.join([chr(ord(smb) ^ key) for smb in line])


key = 999
line = 'Привед Медвед...'
print(line)  # исходная строка

line_code = code(line, key)
print(line_code)  # зашифрованная строка

line_decode = code(line_code, key)
print(line_decode)  # дешифрованная строка
