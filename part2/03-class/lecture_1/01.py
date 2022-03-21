name, age = "Ilon", 51
person = (name, age)

persons = [
    person,
    ("Иванов Иван Иванович", 19),
    ("Ганс Христиан Андерсен", 39)
]

def get_par(obj):
    return obj[1]

# func = lambda obj: obj[1]

# persons.sort(key=get_par, reverse=True)  # сортирует на месте

persons = sorted(persons, key=lambda obj: obj[1])  # возвращает новый отсортированный список

for person in persons:
    print(person[0].ljust(25, ' '), person[1])
