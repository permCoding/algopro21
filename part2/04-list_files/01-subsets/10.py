# бинарные маски

def get_subsets(lst):
    subsets = []
    n = len(lst)
    count = 2**n # кол-во комбинаций
    for comb in range(count):
        cur = []
        s = bin(comb)[2:].rjust(n,'0')
        for i in range(n):
            if s[i] == '1':
                cur.append(lst[i])
        subsets.append(cur)
    return sorted(subsets, key=len)  # lambda x: len(x)


lst = [1, 4, 9, 5]
for sub in get_subsets(lst):
    print(sub)

# 000
# 001
# 010
# 100
# 011
# 110
# 101
# 111
