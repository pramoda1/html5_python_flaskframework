#creating a inheritance 

class car:
    def __init__(self) :
        print("car contructor is exucuting")
    def bmw(self):
        print("this is BMW")
    def benz(self):
        print("this is benz")


#onother class and inherite the above class
class bike(car):
    def __init__(self):
        super().__init__()
        print("the bike constroctor is exucuting")
    def h2r(self):
        print("this is h2r bike")

#create a object in inherited class
bikeobject=bike()
bikeobject.bmw()
bikeobject.benz()
bikeobject.h2r()


# exaample 2

# Base class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic sound"

# Derived class
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the base class
        super().__init__(name, species="Dog")
        self.breed = breed

    # Overriding the method from the base class
    def make_sound(self):
        return "Woof!"

# Another derived class
class Cat(Animal):
    def __init__(self, name, color):
        # Call the constructor of the base class
        super().__init__(name, species="Cat")
        self.color = color
        
    # Overriding the method from the base class
    def make_sound(self):

        print(self.species)
        return "Meow!"

# Creating objects of the derived classes
dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", color="Gray")

# Accessing variables and methods
print(f"{dog.name} is a {dog.breed} and says {dog.make_sound()}.")
print(f"{cat.name} is a {cat.color} cat and says {cat.make_sound()}.")



#polymorphism
class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

# Function that demonstrates polymorphism
def animal_sound(animal):
    print(animal.make_sound())

# Creating instances of the classes
dog = Dog()
cat = Cat()
cow = Cow()

# Using the function to demonstrate polymorphism
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(cow)  # Output: Moo!
