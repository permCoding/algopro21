class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.first_name = name.split()[0]
        self.last_name = name.split()[1]
        self.other_name = name.split()[2]
        self.age = age
    def get_part_name(self, index):
        return self.name.split()[index]


def arrow_func(item):
    # return item.name.split()[-1]
    return item.get_part_name(2)
    # return -item.age


men1 = Person("Лев Николаевич Толстой", 51)
men2 = Person("Иван Иванович Иванов", 19)
men3 = Person("Ганс Христиан Андерсен", 39)

persons = [men2, men3, men1]

for person in sorted(persons, key=arrow_func):
    print(f"{person.age}\t{person.get_family()}")
