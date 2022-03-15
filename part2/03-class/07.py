from operator import attrgetter


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_family(self):
        return self.name.split()[-1]
    def __str__(self):
        return f"{self.age}\t{self.get_family()}"


men1 = Person("Лев Николаевич Толстой", 51)
men2 = Person("Иван Иванович Иванов", 19)
men3 = Person("Ганс Христиан Андерсен", 39)

persons = [men2, men3, men1]

for person in sorted(persons, key=attrgetter("age")):
    print(person)
