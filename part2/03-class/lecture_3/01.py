class Line:
    x = 0
    def __init__(self, p1, p2):
        self.point_1 = p1
        self.point_2 = p2
    def gel_len(self):
        dx = self.point_1.x - self.point_2.x
        dy = self.point_1.y - self.point_2.y
        return (dx**2 + dy**2)**.5


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(0, 0)
p2 = Point(5, 5)
l = Line(p1, p2)
print(round(l.gel_len(),3))
