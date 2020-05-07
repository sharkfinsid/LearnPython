# Object Orientated Programming in Python Part 2
# Inheritance


class Pet:  # Contains all the methods and attributes that all pet classes have

    number_of_pets = 0      # Class variable (Not specific to any one instance)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.add_pet()

    def show(self):
        print(f"I am {self.name} and am {self.age} years old")

    def speak(self):
        print("I don't know how to speak")


    @classmethod
    def add_pet(cls):
        cls.number_of_pets += 1


    @classmethod
    def total(cls):
        return cls.number_of_pets


class Cat(Pet):  # Contains all the methods and attributes that are specific to Cats

    def speak(self):
        print("Meow")


class Dog(Pet):  # Contains all the methods and attributes that are specific to Dogs

    def speak(self):
        print("Bork")


class Fish(Pet):  # We want to add another attribute

    def __init__(self, name, age, color):
        super().__init__(name, age)  # Go to inherited class, call init method and pass name and age args
        self.color = color

    def show(self):
        print(f"I am {self.name}, {self.color} and am {self.age} years old")


# Using the classes

p1 = Pet("Tim", 10)
p1.show()
p1.speak()
c1 = Cat("Lucy", 13)
c1.show()
c1.speak()
d1 = Dog("Tom", 8)
d1.show()
d1.speak()
f1 = Fish("Noel", 2, "Blue")
f1.show()
f1.speak()  # inherits the speak from the upper class because it has none

print(f" => Total pets are: {Pet.total()}")

# Note: Also discussed : Static methods in classes - methods that dont need an instance of the class to be executed (good for grouping similar methods into a package)