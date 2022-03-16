from operator import attrgetter


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_family(self, index):
        return self.name.split()[index]


men1 = Person("Лев Николаевич Толстой", 51)
men2 = Person("Иван Иванович Иванов", 19)
men3 = Person("Ганс Христиан Андерсен", 39)

persons = [men2, men3, men1]

for person in sorted(persons, key=attrgetter("age")):
    print(f"{person.age}\t{person.get_family()}")
