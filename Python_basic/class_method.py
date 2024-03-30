class Dog:
    total_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.total_dogs += 1

    @classmethod
    def get_total_dogs(cls):
        return cls.total_dogs

# Usage:
dog1 = Dog("Buddy")
dog2 = Dog("Rex")

print(Dog.get_total_dogs()) 
