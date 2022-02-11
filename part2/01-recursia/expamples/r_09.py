'''
перевод числа из 10-ой в 2-ую
'''

def get(x):
	if x//2 == 0:
		return x%2
	else:
		return str(get(x//2)) + str(x%2)

x = 14 # это для проверки
print(bin(x)[2:])

print(get(x))
