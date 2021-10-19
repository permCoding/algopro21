with open('students.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()[1:]

list_objs = []
for line in lines:
    obj = line.split('|')
    id, name, avg, age = int(obj[0]), obj[1], float(obj[2]), int(obj[3]) 
    list_objs.append([name, avg, age])

list_sorted = sorted(list_objs, key=lambda item: item[2])
new_lines = []
for obj in list_sorted:
    new_lines.append(obj[0] + '|' + str(obj[1]) + '|' + str(obj[2]) + '\n')

with open('students_sorted.txt', mode='w', encoding='utf-8') as f:
    f.writelines(new_lines[:3])  # берём первую тройку
