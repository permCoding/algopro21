'''
найти НОД двух чисел
+ это алгоритм Евклида - с определённым порядком параметров
'''

def get(a, b):
	if b == 0:
		return a
	else:
		return get(b, a % b)

print(get(64,48))
