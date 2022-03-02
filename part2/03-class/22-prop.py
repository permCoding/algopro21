# свойства

class Warlock(object):
    # атрибуты класса
    count = 0
    # атрибуты объекта self.xxx
    def __init__(self, power=100):
        Warlock.count += 1
        self.__id = Warlock.count
        self.__power = power
    def __str__(self):
        return f"{self.__id}\t{self.__power}"
    def get_id(self):
        return self.__id
    @property
    def power(self):
        return self.__power
    @power.setter
    def power(self, power=100):
        if 0 < power < 100:
            self.__power = power
        else:
            self.__power = 100


w = Warlock(50)

print(w)

w.power = 222  # сработает сеттер свойства

print(w)

w.power = 77  # сработает сеттер свойства

print(w)
