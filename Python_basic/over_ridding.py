class Animal:
    def speak(self):
        return "voice of animal"

class Dog(Animal):
    def speak(self):
        return 5

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the speak method for each instance
print("Dog says:", dog.speak())
# print("Cat says:", cat.speak())
