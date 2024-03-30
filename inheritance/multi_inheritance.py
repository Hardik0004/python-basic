class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def display_course_info(self):
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")

class Student(Person, Course):
    def __init__(self, name, age, course_name, course_code, student_id):
        Person.__init__(self, name, age)
        Course.__init__(self, course_name, course_code)
        self.student_id = student_id

    def display_student_info(self):
        print("Student Information:")
        super(Person, self).display_personal_info()
        super(Course, self).display_course_info()
        print(f"Student ID: {self.student_id}")

# Create a student
students = Student("Alice", 20, "Computer Science", "CS101", "12345")
# Display student information
students.display_student_info()
