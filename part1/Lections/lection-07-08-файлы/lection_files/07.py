file = open('Bunin.txt', 'r', encoding='utf-8')

lines = []  # создаём пустой список
while True:
    line = file.readline()
    if not line:
        break
    lines.append(line)  # добавляем строку в список

print(''.join(lines))  # объединяем список в строку

file.close()
