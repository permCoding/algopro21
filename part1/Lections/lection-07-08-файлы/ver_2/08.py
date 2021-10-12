# программа с костылём

file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

new_lines = []
for line in lines:
    if line[-1] == '\n':
        new_lines.append(line[:-1])
    else:
        new_lines.append(line)

print(lines)
print(new_lines)