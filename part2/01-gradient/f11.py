from os import listdir

lst = listdir("./images")

print('\n'.join(lst))

for item in lst:
    print(item)
