# коды символов в строке

line = 'Привед Медвед...'
line = 'А БВГДЕ'

for smb in line:
    print(f'smb={smb}; code={ord(smb)}; bin={bin(ord(smb))[2:]}')
