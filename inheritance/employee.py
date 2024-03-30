class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Engineer(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def display_info(self):
        super().display_info()
        print(f"Specialization: {self.specialization}")

manager = Manager("Alice", 101, "HR")
engineer = Engineer("Bob", 102, "Software Development")

manager.display_info()
print()
engineer.display_info()
