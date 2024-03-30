polymorphism in Python using a more practical scenario. We'll create a program to calculate the area of different shapes like rectangles, circles, and triangles.

```python
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
```

In this example:

1. We have a base class `Shape` with a method `area()` that is overridden in each derived class.

2. We create three derived classes: `Rectangle`, `Circle`, and `Triangle`, each with its own attributes and an `area` method that calculates and returns the area of the shape.

3. We create instances of these shape objects: `rectangle`, `circle`, and `triangle`.

4. We create a list `shapes` that holds these shape objects.

5. We iterate through the `shapes` list and call the `area()` method on each object. Polymorphism allows us to call the same method on objects of different classes, and the appropriate method for each shape is executed.

When you run the code, it will calculate and display the areas of the different shapes:

```
Area of Rectangle: 20 square units
Area of Circle: 28.26 square units
Area of Triangle: 24.0 square units
```

This example demonstrates polymorphism by allowing us to perform the same operation (calculating the area) on objects of different shapes, with each object using its specific implementation of the `area()` method. It showcases how polymorphism simplifies working with diverse objects in a unified way.