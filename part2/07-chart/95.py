import tkinter as tk


class App_Chart(tk.Tk):
    def __init__(self):
        super().__init__()  # инициализация конструктора базового класса

        width, height, indent = 800, 500, 50  # ширина, высота, отступы по краям

        window = tk.Tk()
        window.title("График функции sin(1.5x)-cos(x)")

        canvas = tk.Canvas(window, width=width, height=height, bg='#fda', cursor="pencil")
        canvas.pack()

        axes(width, height, indent)

        window.bind("<Key>", exit_key)  # выйти по клавише Escape

    def print_event(self, event):
        position = "(x={}, y={})".format(event.x, event.y)
        print(event.type, "event", position)

    def axes(width, height, indent, color="blue"):
        # нарисуем оси координат
        canvas.create_line(indent, height//2, width-indent, height//2, fill=color, arrow=tk.LAST, dash=(8, 2))
        canvas.create_line(width//2, height-indent, width//2, indent, fill=color, arrow=tk.LAST, dash=(8, 2))
        # подпишем оси координат
        canvas.create_text(width//2, indent, text="ось Y", anchor=tk.SW, fill="grey")
        canvas.create_text(width-indent, height//2, text="ось X", anchor=tk.SW, fill="grey")

    def exit_key(event):
        if event.keysym == 'Escape':
            exit()


if __name__ == "__main__":
    app = App_Chart()
    app.mainloop()
