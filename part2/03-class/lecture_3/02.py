import tkinter as tk
import random as rnd


def axes(x0, y0, xm, ym, color):
    canvas.create_line(x0, y0, xm, y0, fill=color, arrow=tk.LAST, dash=(4, 2))
    canvas.create_line(x0, y0, x0, ym, fill=color, arrow=tk.LAST, dash=(4, 2))


w, h, pole, r, n = 800, 600, 40, 3, 250
x0, y0 = pole, h-pole
xm, ym = w-pole, pole

window = tk.Tk()

canvas = tk.Canvas(window, width=w, height=h, bg='#fda')
canvas.pack()

axes(x0, y0, xm, ym, 'blue')

for i in range(n):
    x = rnd.randint(pole,w-pole)
    y = rnd.randint(pole,h-pole)
    canvas.create_oval(x-r,y-r,x+r,y+r)

btn = tk.Button(text="Move")  # как объекты подвинуть?
btn.pack()

window.mainloop()
