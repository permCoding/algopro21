# tutorial: https://matplotlib.org/stable/tutorials/index.html

import matplotlib.pyplot as plt
import numpy as np
import math


def function(x):
    return math.sin(1.5*x) - math.cos(x)


# подготовка данных
label = 'sin(1.5x)-cos(x)'
left, right = -2*math.pi, +2*math.pi
k = 100  # коэффициент для целочисленного цикла for
lst_x = [x/k for x in range(int(left*k), int(right*k)+1)]  # Значения по X
lst_y = [function(x) for x in lst_x]  # Значения по Y

# построение графика
plt.title('График функции')
plt.plot(lst_x, lst_y, 'green', label=label)
plt.grid(True, linestyle='-', color='.80')  # Сетка на плоскости координат
plt.legend()
# построение осей координат
axes = plt.gca()
axes.spines[['left','bottom']].set_position('zero')
axes.spines[['top','right']].set_visible(False)

plt.show()
