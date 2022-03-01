name, age = "Ilon", 51
person = (name, age)

print(person)

persons = [
    ("Иванов Иван Иванович", 19),
    ("Ганс Христиан Андерсен", 39)
]

for person in persons:
    print(person[0], '\t', person[1])
