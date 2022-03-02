class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_family(self):
        return self.name.split()[-1]



men2 = Person("Иван Иванович Иванов", 19)
men3 = Person("Ганс Христиан Андерсен", 39)
men1 = Person("Лев Николаевич Толстой", 51)

persons = [men2, men3, men1]

for i in range(len(persons)):
    print(i+1, '\t', persons[i].age, '\t', persons[i].get_family())
