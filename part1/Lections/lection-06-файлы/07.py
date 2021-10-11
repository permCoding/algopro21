file = open('Bunin.txt', 'r', encoding="utf-8")

lines = file.readlines()

print(''.join(lines))

file.close()
