
f = open("./csv/students.csv", encoding="utf-8")

lines = [line.strip() for line in f]

for line in lines[1:]:
    print(line)
