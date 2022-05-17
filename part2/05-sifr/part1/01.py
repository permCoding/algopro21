# коды символов в строке

# line = 'Привед Медвед...'
line = 'А БВГДЕ'

# печатает символ, код символа, код символа в двоичной СС
for smb in line:
    print(f'smb={smb}; code={ord(smb)}; bin={bin(ord(smb))[2:]}')
