"""
найти НОД двух чисел - вычитанием
+ алгоритм Евклида
"""


def get(a, b):
	if a == b:
		return a
	elif a > b:
		return get(a - b, b)
	else:
		return get(a, b - a)


print(get(48, 64))
