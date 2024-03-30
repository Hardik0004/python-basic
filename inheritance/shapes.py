class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)

print("Circle: Color =", circle.color, "Radius =", circle.radius)
print("Rectangle: Color =", rectangle.color, "Width =", rectangle.width, "Height =", rectangle.height)
