# программа с костылём

file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

new_lines = []
for line in lines:
        tmp = line[:-1] if line[-1] == '\n' else line
        new_lines.append(tmp)

print(lines)
print(new_lines)