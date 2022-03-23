from decanat import get_lines, get_objects


lines = get_lines("./csv/students.csv")

students = get_objects(lines)

for student in sorted(students, key=lambda st: st.id, reverse=True):
    print(student)
