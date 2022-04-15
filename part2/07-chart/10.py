# tutorial: https://matplotlib.org/stable/tutorials/index.html

import matplotlib.pyplot as plt
import math


def function(x):
    return math.sin(1.5*x) - math.cos(x)


# подготовка данных
left, right = -2*math.pi, 3.8*math.pi
k = 100  # коэффициент для целочисленного цикла for
lst_x = [x/k for x in range(int(left*k), int(right*k)+1)]  # Значения по X
lst_y = [function(x) for x in lst_x]  # Значения по Y

# построение графика
plt.title("График функции sin(1.5x)-cos(x)")
plt.xlabel("X"); plt.ylabel("Y")
plt.plot(lst_x, lst_y, 'r')
plt.grid(True, linestyle='-', color='0.75')  # Сетка на плоскости координат
# построение осей координат
axes = plt.gca()
# axes.spines['left'].set_position('center')
# axes.spines['bottom'].set_position('center')
# axes.spines['top'].set_visible(False)
# axes.spines['right'].set_visible(False)
axes.axhline(y=0, color='k')
axes.axvline(x=0, color='k')

plt.show()
