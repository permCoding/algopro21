from random import randint


def gen_members(count=10):  # параметр по умолчанию
    age_min, age_max = 10, 99
    return [(i+1, randint(age_min, age_max)) for i in range(count)]


def save_to_file(name_file, lst):
    lines = ["id\tage\n"]
    for item in lst:
        lines += [f"{item[0]}\t{item[1]}\n"]
    with open(name_file, 'w', encoding='utf-8') as file:
        file.writelines(lines)


members = gen_members()  # сгенерировать список участников
sorted_age = sorted(members, key=lambda item: item[1], reverse=True)
save_to_file('sorted.txt', sorted_age)  # сохранить в файл
