import tkinter as tk
import random as rnd
from tools import Oval
from functools import partial


def set_move(step):
    for item in lst:
        item.move(step)
    set_ovals(lst)


def set_ovals(lst):
    canvas.delete("all")
    for oval in lst:
        x = oval.x
        y = oval.y
        r = oval.r
        c = oval.c
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=c)


def get_list(n, rad, pole):
    lst = []
    for _ in range(n):
        x = rnd.randint(pole,w-pole)
        y = rnd.randint(pole,h-pole)
        r = rnd.randint(2, rad)
        c = ["#3A3","#55F","#A33"][rnd.randint(0,2)]
        lst.append(Oval(x,y,r,c))
    return lst


w, h, pole, n, r = 800, 600, 80, 200, 16

window = tk.Tk()

canvas = tk.Canvas(window, width=w, height=h, bg='#fda')
canvas.pack()
btn = tk.Button(
    text="Move", 
    font=("Times","12","bold"), 
    command=partial(set_move, 8))  # partial для передачи функции с параметрами
btn.pack()

lst = get_list(n, r, pole)
set_ovals(lst)

window.mainloop()
