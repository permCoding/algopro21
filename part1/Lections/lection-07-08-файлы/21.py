# задача - считать строки из файла
# там данные про студентов
# отсортировать их по убыванию среднего балла
# вывести на экран в столбик

with open('students.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

students = []
for line in lines[1:]:
    id, name, avrg, age = map(str, line.split('\t'))
    students.append((int(id), name, float(avrg)))

for student in students:
    print(student)
