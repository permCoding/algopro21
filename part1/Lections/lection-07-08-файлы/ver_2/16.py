with open('input.txt') as file:
    lines = file.readlines()

# s = '1234456543tsdjfvjs'
# print(list(s))

numbers = list(map(int, lines))
print(numbers)
