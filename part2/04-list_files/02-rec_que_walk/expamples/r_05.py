'''
медленное сложение
сложить рекурсивно два числа,
если доступна только операция +1
'''

def get(a,b):
	if a == 0:
		return b
	elif b == 0:
		return a
	else:
		return get(a - 1, b) + 1

print(get(5,7))