'''
медленное сложение
сложить рекурсивно два числа,
если доступна только операция +1
- это ускоренная версия
'''

def get(a,b):
	if a == 0:
		return b
	elif b == 0:
		return a
	elif a < b:
		return get(a - 1, b) + 1
	else:
		return get(a, b - 1) + 1

print(get(5,7))
