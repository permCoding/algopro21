file = open('Bunin.txt', 'r', encoding="utf-8")

lines = []
while True:
    line = file.readline()
    if not line:
        break
    lines.append(line)

print(lines)

file.close()
