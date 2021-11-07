with open('numbers.txt') as file:
    lines = file.readlines()

lst = list(map(int, lines[-1].split()))

print(*sorted(lst, reverse=True))
