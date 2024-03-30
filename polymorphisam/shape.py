class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Create instances of different shapes
rectangle = Rectangle(5, 4)
circle = Circle(3)
triangle = Triangle(6, 8)

# Calculate and display the areas of the shapes
shapes = [rectangle, circle, triangle]

for shape in shapes:
    if isinstance(shape, Shape):
        print(f"Area of {shape.__class__.__name__}: {shape.area()} square units")
