with open('input.txt') as file:
    lines = file.readlines()

numbers = map(int, lines)

print(*numbers)

'''
map - отображение
filter - фильтрация
reduce - свёртка
'''