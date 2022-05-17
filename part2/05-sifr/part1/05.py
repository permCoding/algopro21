# можно объединить функции кодирования и декодирования
# просто добавив дополнительный параметр в функцию
# направление сдвига - direct = -1 или +1


# одна функция для шифрования
def code(line, key, direct=1):  # значение по умолчанию +1
    return ''.join([chr(ord(smb)+direct*key) for smb in line])


key = 9
line = 'Привед Медвед...'
print(line)

line_code = code(line, key)  # кодируем
print(line_code)

line_decode = code(line_code, key, -1)  # декодируем
print(line_decode)
