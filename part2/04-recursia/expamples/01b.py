'''
найти степень m числа n => n**m
'''

def get(n, m):
	if m == 0:
		return 1
	# if m == 1:
	# 	return n
	else:
		return get(n, m - 1) * n

print(get(2,10))
