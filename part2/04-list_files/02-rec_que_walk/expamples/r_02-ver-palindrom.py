'''
развернуть строку
'''

def get(s):
	if s == '':
		return ''
	else:
		return get(s[1:]) + s[0]

s = 'топот'

if s == get(s):
	print('Палиндром')
else:
	print('Не палиндром')

result = 'Палиндром' if s == get(s) else 'Не палиндром'
print(result)
