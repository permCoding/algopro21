
def create_generator():
    for i in range(10):
        yield 2**i


gen = create_generator()  # создаём генератор
print(gen)  # mygenerator является объектом!

for num in gen:
    print(num)
