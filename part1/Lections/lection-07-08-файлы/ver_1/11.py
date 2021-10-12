# задача - считать строки из файла
# там целые числа - отсортировать их
# вывести в одну строку через пробел

file = open('numbers.txt', 'r', encoding="utf-8")
lines = file.readlines()
file.close()

for line in lines:
    print(int(line))
