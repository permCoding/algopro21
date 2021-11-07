file = open('numbers.txt', 'r')
line = file.readline()
file.close()

numbers = list(map(int, line.split()))
print(sum(numbers))
