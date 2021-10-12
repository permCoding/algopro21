# программа с костылём

file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

lines[-1] = lines[-1] + '\n'

new_lines = []
for line in lines:
    new_lines.append(line[:-1])

print(lines)
print(new_lines)