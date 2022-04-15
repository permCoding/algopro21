import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


xa = np.linspace(-np.pi, np.pi, 101, endpoint=True)
ya = np.sin(xa)

fig = plt.Figure(figsize=(6, 4))
axes = fig.add_subplot(1, 1, 1)
axes.plot(xa, ya, color='red')

root = Tk()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(fill=BOTH, expand=YES)
frame = Frame(root) ; frame.pack()

root.mainloop()