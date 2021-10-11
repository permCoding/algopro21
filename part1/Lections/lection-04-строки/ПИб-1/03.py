def checkString(s):
    # !.,: ;-?
    s = s.lower()
    s_new = ''
    for smb in s:
        if smb != ' ':
            s_new += smb
    return s_new == s_new[::-1]


lst = [
    '12345',
    'Аргентина манит негра!',
    'А роза упала на лапу азора',
    '123454321',
    'топот',
    'карапуз'
]

for item in lst:
    check = checkString(item)
    s = ' ' if check else ' не'
    print(f"{item} -{s} палиндром")
