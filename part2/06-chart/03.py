from module import Chart

if __name__ == "__main__":
    app = Chart(800, 500, 50)  # ширина, высота, отступы
    app.axes(color='grey')
    app.set_ovals(n=15)
    app.mainloop()
