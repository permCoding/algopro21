"""
найти произведение чисел от 1 до n - факториал числа n
"""


def get(n):
    if n <= 1:
        return 1
    else:
        return get(n - 1) * n


print(get(5))
