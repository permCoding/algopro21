with open('students.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()[1:]

new_list = []
for i in range(len(lines)):
    obj = lines[i].split('|')
    id, name, avg, age = int(obj[0]), obj[1], float(obj[2]), int(obj[3]) 
    new_list.append([id, name, avg, age])

print(lines)    
print(new_list)

# with open('students_filter.txt', mode='w', encoding='utf-8') as f:
#     f.writelines(lines)

# filter
# lambda
