file = open('Bunin.txt', 'r', encoding="utf-8")

while True:

    line = file.readline()

    if not line:
        break

    print(line)  # выводит с двумя переносами

file.close()


