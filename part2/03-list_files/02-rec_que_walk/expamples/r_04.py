'''
найти минимальный элемент списка
'''

def get(lst):
	if len(lst) == 1:
		return lst[0]
	else:
		# return lst[0] if lst[0] < get(lst[1:]) else get(lst[1:]) # дублирование вызова = это плохо
		tmp = get(lst[1:])
		return lst[0] if lst[0] < tmp else tmp # нет дублирования

lst = [8, 4, 6, 5, -7, 9]
# lst = [] # нет проверки на дурака
print(get(lst))
