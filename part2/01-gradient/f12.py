from os import listdir

lst = listdir("./images")

print('\n'.join(lst))

print()

filtred = filter(lambda x: x.endswith('.jpg'), lst)

print('\n'.join(filtred))
