'''
проверить палиндромность строки
'''

def get(s):
	n = len(s)
	if n <= 1:
		return True
	else:
		return (s[0]==s[-1]) and get(s[1:-1])
		# return get(s[1:-1]) and (s[0]==s[-1]) # так дольше

s = '_адар'
print('Палиндром' if get(s) else 'Не палиндром')
