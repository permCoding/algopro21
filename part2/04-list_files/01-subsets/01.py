
def get_subsets(count):
    if count == 0:
        subsets.append(subset[:])
    else:
        subset.append(r[count-1])
        get_subsets(count-1)
        subset.pop()
        get_subsets(count-1)


r = [1, 4, 7]

subsets = []
subset = []

get_subsets(len(r))
print(subsets)

# стек функций ограничен
