def get_list(s):
    lst = []
    line = ''
    for smb in s:
        if smb != ' ':
            line += smb
        else:
            lst.append(line)
            line = ''
    return lst

def speak_like_jeday(s):
    '''формируем список из строки'''
    lst = get_list(s)
    return lst
    # new_lst = revers_list(lst)
    # result = join_lst(new_lst)
    # return result

s = 'Я изучаю Питон '
print(speak_like_jeday(s), ", мой юный падаван.")