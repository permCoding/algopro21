# задача - считать строки из файла
# там целые числа - отсортировать их
# вывести в одну строку через пробел

file = open('numbers.txt', 'r')
lines = file.readlines()
file.close()

numbers = map(int, lines)
print(numbers)

numbers = list(map(int, lines))
print(numbers)

numbers.sort()
print(numbers)

numbers.sort()
print(*numbers)
