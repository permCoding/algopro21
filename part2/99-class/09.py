from operator import attrgetter
from utils import Ork


lst = []
lst.append(Ork(50))
lst.append(Ork())
lst.append(Ork())
lst.append(Ork(75))

for ork in lst:
    print(ork)

print(lst[0].id)
print(lst[-1].id)
print(Ork.count)
