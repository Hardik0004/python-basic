class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")

class RegularStudent(Student):
    def __init__(self, name, age, student_id, program):
        super().__init__(name, age, student_id)
        self.program = program

    def display_student_info(self):
        super().display_student_info()
        print(f"Program: {self.program}")
        print("Type: Regular Student")

class OnlineStudent(Student):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age, student_id)
        self.course = course

    def display_student_info(self):
        super().display_student_info()
        print(f"Course: {self.course}")
        print("Type: Online Student")

# Create instances of different types of students
regular_student = RegularStudent("Alice", 20, "S12345", "Computer Science")
online_student = OnlineStudent("Bob", 22, "O54321", "Data Science")

# Display student information
print("Regular Student Information:")
regular_student.display_student_info()
print()
print("Online Student Information:")
online_student.display_student_info()
