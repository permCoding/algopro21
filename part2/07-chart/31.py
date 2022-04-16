import matplotlib.pyplot as plt


def function(x,a,b,c,d):
    return (a*x**2 + b*x + c) / (x+d)  # разрыв


def get_data():
    lst_x, lst_y = [], []
    pos_x = left
    while pos_x <= right:
        try:
            pos_y = function(pos_x, a, b, c, d)
            lst_x.append(pos_x)
            lst_y.append(pos_y)
        except:
            pass
        pos_x += step
    return (lst_x, lst_y)


styles = plt.style.available
plt.style.use(styles[0])

a, b, c, d = -5, 200, 100, -3
left, right, step = -100, 100, .5

lst_x, lst_y = get_data()

plt.plot(lst_x, lst_y, color='darkviolet', lw=3)
plt.grid(True)
plt.axhline(lw=1, color='#064')
plt.axvline(lw=1, color='#064')

plt.show()
