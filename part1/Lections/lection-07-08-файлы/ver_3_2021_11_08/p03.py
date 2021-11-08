# сумму чисел второй строки
file = open("numbers.txt")
lines = file.readlines()
file.close()

print(lines[1], end="")
