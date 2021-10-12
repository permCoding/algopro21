with open('students.csv', 'r', encoding='utf-8') as f:
    lines = reversed(f.readlines()[1:])

with open('students_rev.txt', mode='w', encoding='utf-8') as f:
    f.writelines(lines)


# filter
# lambda

# dict