file = open("students.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

lst = []
for line in lines:
    tmp = line.split('|')
    lst += [(tmp[0], int(tmp[1]))]

for item in sorted(lst, key=lambda elm: elm[1], reverse=True):
    print(*item)
