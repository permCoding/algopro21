# задача - считать строки из файла
# там целые числа - выбрать только нечётные
# вывести в одну строку через пробел

def odd(x):
    return x % 2 != 0


with open('numbers.txt', 'r') as file:
    lines = file.readlines()

numbers_odd = sorted(filter(odd, map(int, lines)))

print(*numbers_odd)
