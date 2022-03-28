
def create_generator(f):
    for line in f:
        yield line.strip()


f = open("./csv/students.csv", encoding="utf-8")

print(f)  # это объект ввода/вывода

gen = create_generator(f)  # создаём генератор

gen.__next__()  # пропускаем первую строку с заголовками

for num in gen:
    print(num)
