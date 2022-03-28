
def create_generator(f):
    for line in f:
        yield line.strip()


f = open("./csv/students.csv", encoding="utf-8")

gen = create_generator(f)  # создаём генератор

print(next(gen))  # печатаем первую строку с заголовками

print("= " * 9)

while True:
    try: 
        print(next(gen))
    except:
        break
