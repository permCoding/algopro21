import sys, time


def wait_print(*args, delay=0.15, str_join=''):
    """ Замедленный вывод текста в консоли """
    text = str_join.join(str(x) for x in args)
    n = len(text)
    for i, char in enumerate(text, start=1):
        if i == n:  # если кол-во символов == текущему счетчику
            char = f'{char}\n'  # добавим к последнему символу '\n'
        sys.stdout.write(char)
        sys.stdout.flush()  # очистить буфер - сразу печатать на экран
        time.sleep(delay) 


wait_print('Замедленный вывод текста в консоли')
