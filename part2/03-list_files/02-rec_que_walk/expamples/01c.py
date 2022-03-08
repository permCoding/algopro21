'''
найти степень m числа n => n**m
- это ускоренная версия
'''

def get(n,m):
	if m == 0:
		return 1
	elif m%2 == 0:
		r = get(n, m//2)
		return r * r
	else:
		r = get(n, m//2)
		return r * r * n

# 2**4 = 2**2 * 2**2
# 2**5 = 2**4 * 2 = 2**2 * 2**2 * 2
print(get(2,10))
