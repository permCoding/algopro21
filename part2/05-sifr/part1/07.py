# одна функция для шифрования XOR

def code(line, key):
    return ''.join([chr(ord(smb)^key) for smb in line])


key = 999
line = 'Привед Медвед...'

print(line)
line_code = code(line, key)
print(line_code)
line_decode = code(line_code, key)
print(line_decode)
