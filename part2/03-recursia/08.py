# yield

lst = [2**x for x in range(10)]

# =======================
for i in lst:
    print(i)

print(lst)

for i in range(len(lst)):
    print(lst[i])
# =======================
print('-'*9)
# =======================
genr = (2**x for x in range(10))
for i in genr:
    print(i)

# генератор работает один раз
for i in genr:  # тут уже нет данных
    print(i)

# for i in range(len(genr)):  # так вообще нельзя
#     print(i)

print(genr)
# =======================