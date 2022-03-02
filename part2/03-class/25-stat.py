# статический метод класса

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    @staticmethod
    def get_area(w, h):  # без self и без доступа к атрибутам класса
        return w * h


rect = Rectangle(10, 5)
print(rect.area())

print(Rectangle.get_area(100, 2))
