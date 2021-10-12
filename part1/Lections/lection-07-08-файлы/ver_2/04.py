
file = open('input.txt', 'r')

while True:
    line = file.readline()
    if line:
        num = int(line)
        print(num)
    else:
        break

file.close()


