# программа с костылём

with open('input.txt') as file:
    lines = file.readlines()

for i in range(len(lines)):
    line = lines[i]
    lines[i] = line[:-1] if line[-1] == '\n' else line

print(lines)
