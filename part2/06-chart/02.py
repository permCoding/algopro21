import tkinter as tk
from random import randint


def axes(width, height, indent, color="blue"):
    # нарисуем оси координат
    canvas.create_line(indent, height//2, width-indent, height//2, fill=color, arrow=tk.LAST, dash=(8, 2))
    canvas.create_line(width//2, height-indent, width//2, indent, fill=color, arrow=tk.LAST, dash=(8, 2))
    # подпишем оси координат
    canvas.create_text(width//2, indent, text="ось Y", anchor=tk.SW, fill="grey")
    canvas.create_text(width-indent, height//2, text="ось X", anchor=tk.SW, fill="grey")


def set_ovals(width, height, indent, n=50, r=3):
    for _ in range(n):
        x = randint(indent, width-indent)
        y = randint(indent, height-indent)
        color = "yellow" if x-width//2>0 and y-height//2<0 else "red"
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color)


width, height, indent = 700, 700, 50  # ширина, высота, отступы по краям

window = tk.Tk()
window.title("График функции")

canvas = tk.Canvas(window, width=width, height=height, bg='#fda', cursor="pencil")
canvas.pack()

axes(width, height, indent)
set_ovals(width, height, indent)

window.mainloop()
