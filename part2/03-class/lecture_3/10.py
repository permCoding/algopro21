f = open("./csv/students.csv", encoding="utf-8")
lines = f.readlines()
f.close()


lines = list(map(lambda line: line.strip(), lines))

print(lines[1:])
