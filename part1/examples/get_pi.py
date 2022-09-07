from random import random as r

n, k = 1000, 0
for i in range(n):
    x, y = r(), r()
    l = x**2 + y**2
    if l <= 1:
        k += 1
pi = round(4 * k / n, 2)

print(f"pi = {pi}")
print("pi = {}".format(pi))
print("pi =", "%.2f" % pi)

'''
s1 = pi * r * r
s2 = 4 * r * r

s1/s2 = k/n

pi * r * r       k
---------- == -------
 4 * r * r       n

pi = 4 * k / n
'''