name, age = "Ilon", 51
person = (name, age)

persons = [
    person,
    ("Иванов Иван Иванович", 19),
    ("Ганс Христиан Андерсен", 39)
]

def get_par(obj):
    pass
    pass
    return -obj[1]

# persons.sort(key=get_par)  # сортирует на месте

sort_persons = sorted(persons, key=lambda obj: obj[1], reverse=True)  # возвращает новый отсортированный список


for person in sort_persons:
    print(person[0].ljust(25, ' '), person[1])
