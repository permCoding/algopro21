from itertools import combinations


lst = [1, 4, 7]

subsets = []
for count in range(len(lst)+1):
    for combo in combinations(lst, count):
        subsets.append(combo)

print(subsets)
