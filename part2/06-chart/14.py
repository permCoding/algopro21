import tkinter as tk
import math
import numpy as np


def axes(width, height, indent, color="blue"):
    # нарисуем оси координат
    canvas.create_line(indent, height//2, width-indent, height//2, fill=color, arrow=tk.LAST, dash=(8, 2))
    canvas.create_line(width//2, height-indent, width//2, indent, fill=color, arrow=tk.LAST, dash=(8, 2))
    # подпишем оси координат
    canvas.create_text(width//2, indent, text="ось Y", anchor=tk.SW, fill="grey")
    canvas.create_text(width-indent, height//2, text="ось X", anchor=tk.SW, fill="grey")


def get_points(x_start, x_stop, point_amount=101):
    lst_x = np.linspace(x_start, x_stop, point_amount, endpoint=True)
    lst_y = np.sin(lst_x)  # тут выбор функции, можно сложнее
    return list(zip(lst_x, lst_y))


def chart(width, height, indent, points, fil_color='black'):
    # определим масштаб по X
    mx = max(abs(points[0][0]), abs(points[-1][0]))
    # определим масштаб по Y
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    my = max(abs(min_y), abs(max_y))

    for i in range(1, len(points)):
        pa, pb = points[i-1], points[i]  # точки начала и конца отрезка
        xa = int(pa[0]/mx * (width/2-indent))
        ya = int(pa[1]/my * (height/2-indent))
        xb = int(pb[0]/mx * (width/2-indent))
        yb = int(pb[1]/my * (height/2-indent))
        line_coords = width//2+xa, height//2-ya, width//2+xb, height//2-yb
        canvas.create_line(line_coords, fill=fil_color, width=2)


def exit_key(event):
    if event.keysym == 'Escape':
        exit()


width, height, indent = 800, 500, 50  # ширина, высота, отступы по краям
left, right = -2.5*math.pi, +2.5*math.pi  # границы графика по оси X

window = tk.Tk()
window.title("График функции sin(x)")

canvas = tk.Canvas(window, width=width, height=height, bg='#fda', cursor="pencil")
canvas.pack()

axes(width, height, indent)
points = get_points(left, right)
chart(width, height, indent, points)

window.bind("<Key>", exit_key)  # выйти по клавише Escape

window.mainloop()
