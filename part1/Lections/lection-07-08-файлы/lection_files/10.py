file = open('numbers.txt', 'r')
line = file.readline()
file.close()

lst = line.split()
summa = 0
for item in lst:
    summa += int(item)
print(summa)
