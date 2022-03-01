from utils import Ork


lst = []
lst.append(Ork(50))
lst.append(Ork())
lst.append(Ork())
lst.append(Ork(75))

for ork in lst:
    print(ork)

print(lst[0].id)  # атрибут объекта
print(lst[-1].id)
print(Ork.count)  # переменная класса
