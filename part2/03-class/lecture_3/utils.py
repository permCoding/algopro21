import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x = {self.x}; y = {self.y}"


class Line:
    def __init__(self, _p1, _p2):
       self.p1 = _p1
       self.p2 = _p2
    def get_len(self):
        k1 = self.p1.x - self.p2.x
        k2 = self.p1.y - self.p2.y
        return round(math.pow((k1**2 + k2**2), .5), 3) 
