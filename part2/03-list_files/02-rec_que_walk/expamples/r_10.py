"""
числа Фибоначчи
"""


def get(n):
    if n <= 2:
        return 1
    else:
        return get(n - 1) + get(n - 2)


print(get(10))
