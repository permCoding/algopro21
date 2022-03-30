import sys, time


def wait_print(args, delay=0.15, joiner=''):
    """ Замедленный вывод текста в консоли """
    text = joiner.join(x for x in list(args))
    n = len(text)
    for i, char in enumerate(text, start=1):
        if i == n:  # если кол-во символов == текущему счетчику
            char = f'{char}\n'  # добавим к последнему символу '\n'
        sys.stdout.write(char)
        sys.stdout.flush()  # очистить буфер - сразу печатать на экран
        time.sleep(delay) 


wait_print('Замедленный вывод текста в консоли')

# lst = [1,2,3,4,5]
# print(*lst)