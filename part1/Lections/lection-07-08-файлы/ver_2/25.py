with open('students.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()[1:]

new_list = []
for line in lines:
    obj = line.split('|')
    id, name, avg, age = int(obj[0]), obj[1], float(obj[2]), int(obj[3]) 
    new_list.append([name, avg, age])

new_list.sort(key=lambda item: item[1])  # сортировка по ср баллу

for item in new_list:
    print(item)

# with open('students_sorted.txt', mode='w', encoding='utf-8') as f:
#     f.writelines(lines)

# filter
# lambda
