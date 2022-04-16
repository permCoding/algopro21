import tkinter as tk
from random import randint


class Chart(tk.Tk):
    def __init__(self, width, height, indent):
        super().__init__()  # инициализация конструктора базового класса
        
        self.width, self.height, self.indent = width, height, indent
        self.title("График функции")
        self.canvas = tk.Canvas(self, width=width, height=height, bg='#fda')
        self.canvas.pack()

    def axes(self, color="blue"):  # оси координат
        w, h, indent = self.width, self.height, self.indent
        self.canvas.create_line(indent, h//2, w-indent, h//2, fill=color, arrow=tk.LAST)
        self.canvas.create_line(w//2, h-indent, w//2, indent, fill=color, arrow=tk.LAST)
        self.canvas.create_text(w//2, indent, text="Y", anchor=tk.SW, fill=color)
        self.canvas.create_text(w-indent, h//2, text="X", anchor=tk.SW, fill=color)
    
    def set_ovals(self, n=50, r=3, color="red"):
        for _ in range(n):
            x = randint(self.indent, self.width-self.indent)
            y = randint(self.indent, self.height-self.indent)
            self.canvas.create_oval(x-r,y-r,x+r,y+r,fill=color)


if __name__ == "__main__":
    app = Chart(800, 500, 50)  # ширина, высота, отступы
    app.axes(color='grey')
    app.set_ovals(r=5, color="pink")
    app.mainloop()
