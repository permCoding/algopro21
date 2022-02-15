"""
найти сумму чисел от 1 до n
- по умолчанию стек вызовов функций ограничен числом 1000
- увеличить величину стека: setrecursionlimit(XXX)
"""
from sys import setrecursionlimit


def get(n):
    if n <= 1:
        return 1
    else:
        return get(n - 1) + n


# setrecursionlimit(2000)
print(get(1555))
