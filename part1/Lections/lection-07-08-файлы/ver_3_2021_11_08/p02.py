file = open("numbers.txt")
lines = file.readlines()
file.close()

for line in lines:
    print(line, end="")
