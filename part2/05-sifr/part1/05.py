# одна функция для шифрования

def code(line, key, z=1):
    return ''.join([chr(ord(smb)+z*key) for smb in line])


key = 9
line = 'Привед Медвед...'

print(line)
line_code = code(line, key)
print(line_code)
line_decode = code(line_code, key, -1)
print(line_decode)
