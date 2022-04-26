# tutorial: https://matplotlib.org/stable/tutorials/index.html

import matplotlib.pyplot as plt
import numpy as np
import math


def func_a(x):
    return math.sin(1.5*x) - math.cos(x)


def func_b(x):
    return -.5 - math.sin(x) - .2*math.cos(5*x)


# подготовка данных
title = 'График функции'
label_a = 'sin(1.5x)-cos(x)'
label_b = '-0.5-sin(x)-0.2*cos(5*x)'
left, right = -2*math.pi, +2*math.pi
dx = .02  # шаг изменения X
lst_x = np.arange(left, right, dx)  # Значения по X

lst_y = [func_a(x) for x in lst_x]  # Значения по Y
plt.plot(lst_x, lst_y, 'green', label=label_a)  # график

lst_y = [func_b(x) for x in lst_x]  # Значения по Y
plt.plot(lst_x, lst_y, 'blue', label=label_b)  # график

plt.grid(True, linestyle='-', color='.80')  # сетка
plt.legend()

axes = plt.gca()  # построение осей координат
axes.spines[['left','bottom']].set_position('zero')
axes.spines[['top','right']].set_visible(False)

plt.gcf().canvas.set_window_title(title)  # заголовок окна

plt.show()
