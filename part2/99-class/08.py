from operator import attrgetter
from utils import Person


persons = [
    Person("Лев Николаевич Толстой", 51),
    Person("Иван Иванович Иванов", 19),
    Person("Ганс Христиан Андерсен", 39)
]

for person in sorted(persons, key=attrgetter("age")):
    print(person)
