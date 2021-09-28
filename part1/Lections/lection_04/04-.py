# речь Йоды

def my_split(prefix):
    lst = []
    tmp = ''
    for smb in prefix:
        if smb != ' ':
            tmp += smb
        else:
            lst.append(tmp)
            tmp = ''
    lst.append(tmp)
    return lst

def my_reverce(lst):
    new_lst = []
    for i in range(len(lst)-1, -1, -1):
        new_lst.append(lst[i])
    return new_lst

def my_join(lst, sep=' '):
    s = ''
    for item in lst:
        s += item + ' '
    return s[:-1] 

prefix = "Я изучаю Python"
postfix = ", мой юный падаван."
lst = my_split(prefix)
lst = my_reverce(lst)
new_pr = my_join(lst)

print(new_pr + postfix)

# new_pr = ' '.join(prefix.split(' ')[::-1])
