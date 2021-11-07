file = open('Bunin.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

print(''.join(lines))
