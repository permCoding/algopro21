# бинарные маски

def get_sorted_subsets(lst):
    n = len(lst)
    count = 2**n
    subsets = []
    for comb in range(count):
        cur = []
        for pos in range(n):
            if (comb & (1 << pos)) > 0:
                cur.append(lst[pos])
        subsets.append(cur)
    return sorted(subsets, key=len)


lst = [1, 4, 9, 5]
for sub in get_sorted_subsets(lst):
    print(sorted(sub))

# 000
# 001
# 010
# 100
# 011
# 110
# 101
# 111

# comb = 5  # 101

# mask = 1  # 001
# res = comb & mask
# print(res>0)

# mask <<= 1  # 010
# res = comb & mask
# print(res>0)

# mask <<= 1  # 100
# res = comb & mask
# print(res>0)
