with open('Bunin.txt', 'r', encoding="utf-8") as file:
    lines = reversed(file.readlines())

print(''.join(lines))
