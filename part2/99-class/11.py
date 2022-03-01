from utils import Ork
from copy import copy, deepcopy

ork1 = Ork(50)
ork2 = Ork()
ork3 = copy(ork2)  # поверхностное копирование

print(ork1.id)
print(ork1.power)

print(ork1)
print(ork2)

ork3.power = 25

print(ork1)
print(ork2)
print(ork3)
