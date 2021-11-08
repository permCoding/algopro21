# сумму чисел второй строки
file = open("numbers.txt")
lines = file.readlines()
file.close()

print(sum(map(int, lines[1].split())))
