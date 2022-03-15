"""
генератор не хранит все данные в оперативке
но может их возвращать по мере запросов
"""


def create_generator():
    i = 0
    while i < 10:
        yield 2**i
        i += 1


gen = create_generator()  # создаём генератор
print(gen)

for num in gen:
    print(num)
