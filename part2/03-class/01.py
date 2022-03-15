name, age = "Ilon", 51
person = (name, age)

persons = [
    ("Иванов Иван Иванович", 19),
    ("Ганс Христиан Андерсен", 39),
    person
]

persons.sort(key=lambda item: item[1])

for person in persons:
    print(person[0].ljust(25, ' '), person[1])
