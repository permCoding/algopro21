from utils import Warlock


w = Warlock(50)

w.__id = 33  # так не работает

print(w)

w.set_power(22)

print(w)
