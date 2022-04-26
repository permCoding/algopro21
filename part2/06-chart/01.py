import tkinter as tk


def axes(width, height, indent, color="blue"):
    # нарисуем оси координат
    canvas.create_line(indent, height//2, width-indent, height//2, fill=color, arrow=tk.LAST, dash=(8, 2))
    canvas.create_line(width//2, height-indent, width//2, indent, fill=color, arrow=tk.LAST, dash=(8, 2))
    # подпишем оси координат
    canvas.create_text(width//2, indent, text="ось Y", anchor=tk.SW, fill="grey")
    canvas.create_text(width-indent, height//2, text="ось X", anchor=tk.SW, fill="grey")


width, height, indent = 700, 700, 50  # ширина, высота, отступы по краям

window = tk.Tk()
window.title("График функции")

canvas = tk.Canvas(window, width=width, height=height, bg='#fda', cursor="pencil")
canvas.pack()

axes(width, height, indent)

window.mainloop()
