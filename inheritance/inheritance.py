class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")

class RegularStudent(Student):
    def __init__(self, name, roll_number, program):
        super().__init__(name, roll_number)
        self.program = program

    def display(self):
        super().display()
        print(f"Program: {self.program}")
        print("Type: Regular Student")

class OnlineStudent(Student):
    def __init__(self, name, roll_number, course):
        super().__init__(name, roll_number)
        self.course = course

    def display(self):
        super().display()
        print(f"Course: {self.course}")
        print("Type: Online Student")

# Create instances of different types of students
student1 = RegularStudent("Alice", 101, "Computer Science")
student2 = OnlineStudent("Bob", 102, "Data Science")

# Display student information
student1.display()
print()
student2.display()
