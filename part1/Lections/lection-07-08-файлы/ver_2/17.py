with open('input.txt') as file:
    lines = file.readlines()

lines.sort()  # строки сортируются в лексико-графическом порядке
print(lines)

x, y = '100', '99'
print(f"{y}\t{x}" if x > y else f"{x}\t{y}") 

lines.sort(reverse=True)
print(lines)
