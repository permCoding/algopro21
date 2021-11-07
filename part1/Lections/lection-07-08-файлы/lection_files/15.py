from random import randint

count = 10  # всего участников
age_min = 10  # от 
age_max = 99  # до 
members = [(i+1, randint(age_min, age_max)) for i in range(count)]

print("id\tage")
for item in members:
    print(f"{item[0]}\t{item[1]}")
