
file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

new_lines = []
for line in lines:
    new_lines.append(line[:-1])

print(lines)
print(new_lines)