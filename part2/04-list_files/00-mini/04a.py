import sys, time
from random import random


def wait_print(smbs):
    """ Замедленный вывод текста в консоли """
    for char in list(smbs):
        sys.stdout.write(char)
        sys.stdout.flush()  # очистить буфер - сразу печатать на экран
        time.sleep(random())


wait_print('Замедленный вывод текста в консоли')
