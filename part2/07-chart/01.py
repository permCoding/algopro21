import tkinter as tk
import math


def axes(x0, y0, xm, ym, color="blue"):
    canvas.create_line(x0, y0, xm, y0, fill=color, arrow=tk.LAST, dash=(8, 2))
    canvas.create_line(x0, y0, x0, ym, fill=color, arrow=tk.LAST, dash=(8, 2))


def chart(function, tm, x0, y0, xm, ym, fil_color='black'):
    xb = x0; t = 0; yb = y0+(ym-y0)*function(t)
    canvas.create_line(xb, yb, xb, yb, fill=fil_color)
    for x in range(x0+2, xm, 2):
        t = tm*(x-x0)/(xm-x0)
        y = y0+(ym-y0)*function(t)
        canvas.create_line(xb, yb, x, y, fill=fil_color)
        xb = x; yb = y


w, h, indent = 800, 600, 40  # ширина, высота, отступы по краям
x0, y0 = indent, h-indent  # размещение осей координат
xm, ym = w-indent, indent

window = tk.Tk()
window.title("График функции")
canvas = tk.Canvas(window, width=w, height=h, bg='#fda', cursor="pencil")
canvas.pack()

axes(x0, y0, xm, ym)
chart(math.sin, 7, x0, y0, xm, ym)

canvas.create_text(indent, indent, text="ось Y", anchor=tk.SW, fill="grey")

window.mainloop()
