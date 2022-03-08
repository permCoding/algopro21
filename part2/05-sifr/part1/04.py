# функции кодирования и декодирования

def code(line, key):
    return ''.join([chr(ord(smb)+key) for smb in line])


def decode(line, key):
    return ''.join([chr(ord(smb)-key) for smb in line])


key = 9
line = 'Привед Медвед...'

print(line)
line_code = code(line, key)
print(line_code)
line_decode = decode(line_code, key)
print(line_decode)
