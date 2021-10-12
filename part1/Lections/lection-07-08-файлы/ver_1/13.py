# задача - считать строки из файла
# там целые числа - отсортировать их
# вывести в одну строку через пробел

file = open('numbers.txt', 'r')
lines = file.readlines()
file.close()

numbers = []
for line in lines:
    numbers.append(int(line))

numbers.sort()

print(numbers)
