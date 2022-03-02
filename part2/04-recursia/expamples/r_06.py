'''
двойная сумма
'''

def get_row(r,c):
	if c < 0:
		return 0
	else:
		return get_row(r, c - 1) + tab[r][c]

def get(r,c):
	if r < 0:
		return 0
	else:
		return get(r - 1, c) + get_row(r,c)


tab = [
	[1,2,3,4],
	[5,6,7,8],
]
h = len(tab)
w = len(tab[0])
print(get(h-1,w-1))