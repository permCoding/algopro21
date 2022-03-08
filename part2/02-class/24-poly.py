# полиморфизм

class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, c):
        self.__color = c

    def info(self):
       print("Figure")
       print("Color: " + self.__color)


class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height

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

    def info(self):  # переопределим метод
        print("Rectangle")
        print("Color: " + self.color)
        print("Width: " + str(self.width))
        print("Height: " + str(self.height))
        print("Area: " + str(self.area()))

    def area(self):
        return self.__width * self.__height


fig = Figure("orange")
fig.info()
print()
rect = Rectangle(3, 4, "yellow")
rect.info()
