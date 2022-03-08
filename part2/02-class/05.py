class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_family(self):
        return self.name.split()[-1]


def arrow_func(item):
    # return item.name.split()[-1]
    return item.get_family()
    # return -item.age


men1 = Person("Лев Николаевич Толстой", 51)
men2 = Person("Иван Иванович Иванов", 19)
men3 = Person("Ганс Христиан Андерсен", 39)

persons = [men2, men3, men1]

for person in sorted(persons, key=arrow_func):
    print(f"{person.age}\t{person.get_family()}")
