# наследование

class Figure:
    def __init__(self, color):
        self.__color = color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):  # наследование
    def __init__(self, width, height, color):
        super().__init__(color)  # отсылка к конструктору базового класса
        self.__width = width
        self.__height = height
    def __str__(self):
        return f"{self.width}:{self.height},{self.color}"
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError 

    def area(self):
        return self.__width * self.__height


rect = Rectangle(3, 4, "yellow")
print(rect)
rect.color = "pink"
print(rect)
