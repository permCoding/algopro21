from random import randint


def gen_members(count=10):  # параметр по умолчанию
    age_min, age_max = 10, 99
    return [(i+1, randint(age_min, age_max)) for i in range(count)]


def save_to_file(name_file, lst):
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(f"id\tage\n")
        for item in lst:
            file.write(f"{item[0]}\t{item[1]}\n")


members = gen_members()  # сгенерировать список участников

print("id\tage")
for item in members:
    print(f"{item[0]}\t{item[1]}")  # вывести на экран

older50 = list(filter(lambda item: item[1] > 50, members))  # выбрать по фильтру

save_to_file('older50.txt', older50)  # сохранить в файл
