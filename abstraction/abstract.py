class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create instances of shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate and display the areas of the shapes
shapes = [circle, rectangle]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area()} square units")
