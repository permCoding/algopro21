with open('input.txt') as file:
    lines = file.readlines()

numbers = map(int, lines)
for num in numbers:
    print(num)
