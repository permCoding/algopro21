with open('input.txt') as file:
    lines = file.readlines()

numbers = []
for line in lines:
    numbers.append(int(line))

print(numbers)
