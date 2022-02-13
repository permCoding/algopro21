'''
найти НОД двух чисел
+ это алгоритм Евклида
'''

def get(a, b):
	if a == 0 or b == 0:
		return max(a,b)
	elif a > b:
		return get(a % b, b)
	else:
		return get(a, b % a)

print(get(48,64))
