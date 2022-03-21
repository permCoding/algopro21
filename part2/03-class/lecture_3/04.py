import tkinter as tk
import random as rnd
from tools import Oval


def set_move():
    for item in lst:
        item.move()
    set_ovals(lst)


def set_ovals(lst):
    canvas.delete("all")
    for oval in lst:
        x = oval.x
        y = oval.y
        r = oval.r
        c = oval.c
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=c)


def get_list(n):
    lst = []
    for i in range(n):
        x = rnd.randint(pole,w-pole)
        y = rnd.randint(pole,h-pole)
        r = rnd.randint(2, 7)
        c = ["#3D3","#33D","#D33","#FF0"][rnd.randint(0,3)]
        lst.append(Oval(x,y,r,c))
    return lst


def motion():
    if move:
        set_move()
        window.after(100, motion)


def start_stop():
    global move
    move = not(move)
    btn_move["text"] = "СТОП" if move else "СТАРТ"
    motion()


def move_center():
    for item in lst:
        item.x = w // 2
        item.y = h // 2
    set_ovals(lst)

w, h, pole, n = 800, 600, 80, 300

window = tk.Tk()

canvas = tk.Canvas(window, width=w, height=h, bg='#ddc')
canvas.pack()

btn_move = tk.Button(
    text="Move", 
    font="12",
    width=25,
    command=start_stop)  # двигаем объекты
btn_move.pack(side=tk.RIGHT, padx=10, pady=10)

btn_center = tk.Button(
    text="Center", 
    font="12",
    width=25,
    command=move_center)  # двигаем объекты
btn_center.pack(side=tk.LEFT, padx=10, pady=10)

lst = get_list(n)
set_ovals(lst)
move = False

window.mainloop()
