import random as rnd


class Oval():
    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.r = r  # radius
        self.c = c  # color
    def move(self, step=3):
        self.x += rnd.randint(-step, step)
        self.y += rnd.randint(-step, step)
