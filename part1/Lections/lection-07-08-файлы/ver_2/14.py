def getX2(num):
    return num**2


with open('input.txt') as file:
    lines = file.readlines()

numbers = map(int, lines)
print(*numbers)

numbers2 = map(getX2, numbers)
print(*numbers2)

'''
map - отображение
filter - фильтрация
reduce - свёртка
'''