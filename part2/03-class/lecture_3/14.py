from decanat import get_lines, get_objects


lines = get_lines("./csv/students.csv")

students = get_objects(lines)

find_group = "ПИб-1"

for student in filter(lambda st: st.group == find_group, students):
    print(student)
