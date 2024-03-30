class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Fido", "Canine")
cat = Cat("Whiskers", "Feline")

print(f"{dog.name} ({dog.species}) says: {dog.speak()}")
print(f"{cat.name} ({cat.species})")

