# задача - считать строки из файла
# там целые числа - выбрать только нечётные
# вывести в одну строку через пробел

with open('numbers.txt', 'r') as file:
    lines = file.readlines()

numbers = map(int, lines)
numbers_odd = filter(lambda x: x%2!=0, numbers)

print(*sorted(numbers_odd))
