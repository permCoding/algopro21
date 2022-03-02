class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


men1 = Person("Иванов Иван Иванович", 19)
men2 = Person("Ганс Христиан Андерсен", 39)

print(men1.age, '\t', men1.name)

print(men2.age, '\t', men2.name)
