# смещаем коды символов для сокрытия

key = 9

line = 'Привед Медвед...'

lst = [ord(smb)+key for smb in line]

print(lst)

result = [chr(item) for item in lst]

print(''.join(result))
