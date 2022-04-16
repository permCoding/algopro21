# tutorial: https://matplotlib.org/stable/tutorials/index.html

import matplotlib.pyplot as plt
import numpy as np
import math


def function(x):
    return math.sin(1.5*x) - math.cos(x)


# подготовка данных
title = 'График функции'
label = 'sin(1.5x)-cos(x)'
left, right = -2*math.pi, +2*math.pi
dx = .02  # шаг изменения X
lst_x = np.arange(left, right, dx)  # Значения по X
lst_y = [function(x) for x in lst_x]  # Значения по Y

plt.plot(lst_x, lst_y, 'green', label=label)  # график

plt.grid(True, linestyle='-', color='.80')  # сетка
plt.legend()

axes = plt.gca()  # построение осей координат
axes.spines[['left','bottom']].set_position('zero')
axes.spines[['top','right']].set_visible(False)

plt.gcf().canvas.set_window_title(title)  # заголовок окна

plt.show()
