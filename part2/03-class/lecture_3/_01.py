from utils import Student


def get_lines(fn):
    f = open(file_name, encoding="utf-8")
    lines = f.readlines()
    f.close()
    return lines


def get_objects(lines):
    objs = []
    for line in lines:
        id, name, group = tuple(line.split("|"))
        st = Student(id, name, group)  # объект студента
        objs.append(st)
    return objs


file_name = "students.csv"
lines = get_lines(file_name)
students = get_objects(lines[1:])
for student in students:
    print(student)
