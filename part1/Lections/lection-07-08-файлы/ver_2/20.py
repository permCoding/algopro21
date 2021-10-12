lst = sorted(map(int, open('input.txt').readlines()))

s = '\t'.join(map(str, lst))

print(type(s))

print(s)
