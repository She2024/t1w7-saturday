class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Axel", "Mastiff", " dark brindle")
neighbors_dog = Dog ("Scooby", "Labrador", "black")

# Fetching the attributes of the class using objects
print(my_dog.name)

print(my_dog.bark())

Droid

class Droid:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def bark(self):
        return f"{self.name} says Woof!"