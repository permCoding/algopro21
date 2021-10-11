def get_list(s):
    '''
    если последний символ не пробел
    то функция не работает
    '''
    lst = []
    line = ''
    for smb in s:
        if smb == ' ':
            lst.append(line)
            line = ''
        else:
            line += smb
    return lst


def revers_list(lst):
    new_lst = []
    i = len(lst) - 1 
    while i >= 0:
        new_lst.append(lst[i]) 
        i -= 1
    return new_lst


def join_lst(new_lst):
    result = ''
    for i in range(len(new_lst)):
        postfix = ' ' if i != len(new_lst) - 1 else ''
        result += new_lst[i] + postfix
    return result


def speak_like_jeday(s):
    '''формируем список из строки'''
    lst = get_list(s)
    new_lst = revers_list(lst)
    result = join_lst(new_lst)
    return result


s = 'Я изучаю Питон' # если последний символ не пробел
print(speak_like_jeday(s), ", мой юный падаван.")