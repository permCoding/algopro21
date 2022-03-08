class Person(object):
   def __init__(self, name, age):
       self.name = name
       self.age = age


men2 = Person("Иванов Иван Иванович", 19)
men3 = Person("Ганс Христиан Андерсен", 39)
men1 = Person("Ilon", 51)

persons = [men2, men3, men1]

for person in sorted(persons, key=lambda item: item.age, reverse=True):
    print(person.age, '\t', person.name)
