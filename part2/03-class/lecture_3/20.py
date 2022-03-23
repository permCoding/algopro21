import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.point_1 = p1
        self.point_2 = p2
    def get_len(self):
        k1 = self.point_1.x - self.point_2.x
        k2 = self.point_1.y - self.point_2.y
        return round(math.pow(k1**2 + k2**2, .5), 3)


line = Line(Point(0,0), Point(5,5))

print(line.get_len())
