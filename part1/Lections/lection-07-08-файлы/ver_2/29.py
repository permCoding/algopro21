from functools import reduce


with open('students.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()[1:]

list_objs = list(map(lambda line: line.split('|'), lines))

acc_ages = reduce(lambda acc, cur: acc + int(cur[3]), list_objs, 0)

print(acc_ages/len(list_objs))  # найти средний возраст студентов


# list_objs = []
# for line in lines:
#     obj = line.split('|')
#     id, name, avg, age = int(obj[0]), obj[1], float(obj[2]), int(obj[3]) 
#     list_objs.append([name, avg, age])

