from utils import Point, Test
from copy import copy, deepcopy

test1 = Test()

print(test1.array)
print(test1.point)
print(test1.litera)

test2 = copy(test1)  # поверхностное копирование

test2.litera = "zzz"
test2.point.x = -666
test2.array[0] = 99

print(test1.array)
print(test1.point)
print(test1.litera)

print(test2.array)
print(test2.point)
print(test2.litera)

