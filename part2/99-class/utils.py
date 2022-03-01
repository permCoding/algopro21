class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_family(self):
        return self.name.split()[-1]
    def __str__(self):
        return f"{self.age}\t{self.get_family()}"


class Ork(object):
    # переменные класса
    count = 0
    # атрибуты объекта self.xxx
    def __init__(self, power=100):
        Ork.count += 1
        self.id = Ork.count
        self.power = power
    def __str__(self):
        return f"{self.id}\t{self.power}"


class Warlock(object):
    # переменные класса
    count = 0
    # атрибуты объекта self.xxx
    def __init__(self, power=100):
        Warlock.count += 1
        self.__id = Ork.count
        self.__power = power
    def __str__(self):
        return f"{self.__id}\t{self.__power}"
    def get_id(self):
        return self.__id
    def get_power(self):
        return self.__power
    def set_id(self, power=100):
        self.__power = power


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x}:{self.y}"


class Test():
    def __init__(self, array=[1,2,3,4,5], point=Point(), lit='a'):
        self.array = array
        self.point = point
        self.litera = lit
