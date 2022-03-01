from utils import Ork


ork1 = Ork(50)
ork2 = Ork()
ork3 = ork2  # присваивается по ссылке

print(ork1.id)
print(ork1.power)

print(ork1)
print(ork2)

ork3.power = 25

print(ork1)
print(ork2)
print(ork3)
