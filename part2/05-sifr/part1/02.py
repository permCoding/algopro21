# из строки в список кодов и обратно

line = 'Привед Медвед...'

lst = [ord(smb) for smb in line]

print(lst)

result = [chr(item) for item in lst]

print(''.join(result))
