from random import randint

count = 10  # всего участников
age_min = 10  # от 
age_max = 99  # до 
ages = [randint(age_min, age_max) for _ in range(count)]

print("id\tage")
for i, item in enumerate(ages):
    print(f"{i+1}\t{item}")
