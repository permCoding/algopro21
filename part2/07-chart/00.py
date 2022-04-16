import tkinter as tk


width, height, indent = 700, 700, 50  # ширина, высота, отступы по краям

window = tk.Tk()
window.title("График функции")

canvas = tk.Canvas(window, width=width, height=height, bg='#fda', cursor="pencil")
canvas.pack()

canvas.create_line(
    indent, 
    height//2, 
    width-indent, 
    height//2, 
    fill='#000', 
    arrow=tk.LAST)

canvas.create_line(width//2, height-indent, width//2, indent, fill='#000', arrow=tk.LAST)

window.mainloop()
