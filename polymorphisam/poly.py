class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"

class Parrot:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Squawk!"

# Create instances of different animals
dog = Dog("Buddy")
cat = Cat("Whiskers")
parrot = Parrot("Polly")

# Define a function that demonstrates polymorphism
def animal_sound(animal):
    data =(f"{animal.name} says: {animal.speak()}")
    return data

# print(dog.name)
# print(dog.speak())
# Call the function with different anima
animal_data = animal_sound(cat)
print(animal_data)
# animal_sound(cat)
# animal_sound(parrot)

