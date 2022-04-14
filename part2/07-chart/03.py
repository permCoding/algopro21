import tkinter as tk
import math
from PIL import Image


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def axes(width, height, indent, color="blue"):
    # нарисуем оси координат
    canvas.create_line(indent, height//2, width-indent, height//2, fill=color, arrow=tk.LAST, dash=(8, 2))
    canvas.create_line(width//2, height-indent, width//2, indent, fill=color, arrow=tk.LAST, dash=(8, 2))
    # подпишем оси координат
    canvas.create_text(width//2, indent, text="ось Y", anchor=tk.SW, fill="grey")
    canvas.create_text(width-indent, height//2, text="ось X", anchor=tk.SW, fill="grey")


def get_points(function, x_start, x_stop, step=.1):
    points = []
    x = x_start
    while x <= x_stop:
        points.append(Point(x, function(x)))
        x += step
    return points


def chart(width, height, indent, points, fil_color='black'):
    # определим масштаб по X
    mx = max(abs(points[0].x), abs(points[-1].x))
    # определим масштаб по Y
    min_y = min(points, key=lambda p: p.y).y
    max_y = max(points, key=lambda p: p.y).y
    my = max(abs(min_y), abs(max_y))

    for i in range(1, len(points)):
        pa, pb = points[i-1], points[i]  # точки начала и конца отрезка
        xa = int(pa.x/mx * (width/2-indent))
        ya = int(pa.y/my * (height/2-indent))
        xb = int(pb.x/mx * (width/2-indent))
        yb = int(pb.y/my * (height/2-indent))
        line_coords = width//2+xa, height//2-ya, width//2+xb, height//2-yb
        canvas.create_line(line_coords, fill=fil_color, width=2)


def function(x):  # функция для построения графика
    return math.sin(1.5*x)-math.cos(x)


def print_key(event):
    print(event.keysym)  # просто для контроля названий клавиш
    if event.keysym == 'Escape':
        exit()


width, height, indent = 700, 700, 50  # ширина, высота, отступы по краям
left, right = -2*math.pi, +2*math.pi  # границы графика по оси X

window = tk.Tk()
window.title("График функции sin(1.5x)-cos(x)")

# иконка окна программы на панели задач
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='notebook.png'))  # для Linux
# window.iconbitmap("notebook.png")  # для windows

canvas = tk.Canvas(window, width=width, height=height, bg='#fda', cursor="pencil")
canvas.pack()

axes(width, height, indent)
points = get_points(function, left, right)
chart(width, height, indent, points)

window.bind("<Key>", print_key)  # выйти по клавише Escape

window.mainloop()
