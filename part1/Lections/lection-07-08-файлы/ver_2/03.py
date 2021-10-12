
file = open('input.txt', 'r')

while True:
    line = file.readline()
    if line:
        print(line, end='')
    else:
        break

file.close()


