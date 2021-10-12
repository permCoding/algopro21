# программа с костылём

file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

for i in range(len(lines)):
    line = lines[i]
    lines[i] = line[:-1] if line[-1] == '\n' else line

print(lines)
