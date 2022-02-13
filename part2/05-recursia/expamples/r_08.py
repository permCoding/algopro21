'''
перевод числа из 2-ой в 10-ую
'''

def get(s):
	if s == '':
		return 0
	else:
		return get(s[1:]) + int(s[0])*2**(len(s)-1)

# 1110
x = 14 # это для проверки
b = bin(x)
print(b) # для контроля
s = b[2:]
print(s) # вот это число мы переводим
print(get(s))