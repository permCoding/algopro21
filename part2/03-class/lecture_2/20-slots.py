class Warlock(object):
    # разрешённые атрибуты объекта
    __slots__ = ["name", "power"]
    id = 0

    def __init__(self, _name, _power=100):
        self.name = _name
        self.power = _power

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.power}"

    @staticmethod
    def set_id(_id):
        Warlock.id = _id


w = Warlock("Nemo", 50)

w.name = "Groggy"
w.power = 155
try:
    w.id = 256
except AttributeError as err:
    print(err)

print(w)
w.set_id(124)
print(w)
Warlock.id = 1024
print(w)
