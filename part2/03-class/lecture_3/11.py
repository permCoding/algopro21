from decanat import get_lines, get_objects


lines = get_lines("./csv/students.csv")

students = get_objects(lines)

for st in students:
    print(st)
