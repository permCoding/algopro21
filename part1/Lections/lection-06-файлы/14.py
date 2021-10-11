# задача - считать строки из файла
# там целые числа - отсортировать их
# вывести в одну строку через пробел

file = open('numbers.txt', 'r')
lines = file.readlines()
file.close()

for i in range(len(lines)):
    lines[i] = int(lines[i])

lines.sort()

print(lines)
