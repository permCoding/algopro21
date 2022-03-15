'''
развернуть строку
'''

def get(s):
	if s == '':
		return ''
	else:
		return get(s[1:]) + s[0]


s = 'строка'
print(s[::-1]) # для контроля
print(get(s))
