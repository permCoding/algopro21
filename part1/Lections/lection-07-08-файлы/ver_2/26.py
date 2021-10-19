with open('students.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()[1:]

new_list = []
for line in lines:
    obj = line.split('|')
    id, name, avg, age = int(obj[0]), obj[1], float(obj[2]), int(obj[3]) 
    new_list.append([name, avg, age])

new_list.sort(key=lambda item: item[0])

with open('students_sorted.txt', mode='w', encoding='utf-8') as f:
    for lst_obj in new_list:
        line = lst_obj[0] + '|' + str(lst_obj[1]) + '|' + str(lst_obj[2])
        # print(line)
        f.write(line + '\n')
