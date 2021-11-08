# сумму чисел второй строки
file = open("numbers.txt")
lines = file.readlines()
file.close()

summa = 0
lst = lines[1].split(" ")
for item in lst:
    summa += int(item)
print(summa)
