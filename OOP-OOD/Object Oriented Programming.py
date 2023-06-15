"""
Implementing Polymorphism Using Inheritance
Consider the example of a Shape class, which is the base class while many shapes like Rectangle and Circle
extending from the base class are derived classes. These derived classes inherit the getArea() method and
 provide a shape-specific implementation, which calculates its area
"""

class Shape:
    def __init__(self):  # initializing sides of all shapes to 0
        self.sides = 0

    def getArea(self):
        pass


class Rectangle(Shape):  # derived from Shape class
    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)


class Circle(Shape):  # derived from Shape class
    # initializer
    def __init__(self, radius=0):
        self.radius = radius

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


# shapes = [Rectangle(6, 10), Circle(7)]
# print("Area of rectangle is:", str(shapes[0].getArea()))
# print("Area of circle is:", str(shapes[1].getArea()))


'''
Implementing duck typing

'''
class Dog:
    def Speak(self):
        print("Woof woof")


class Cat:
    def Speak(self):
        print("Meow meow")


class AnimalSound:
    def Sound(self, animal):
        animal.Speak()


# sound = AnimalSound()
# dog = Dog()
# cat = Cat()
# sound.Sound(dog)
# sound.Sound(cat)

'''
Abstract Base Classes (ABC): define a set of methods and properties that a class must implement 
in order to be considered a duck-type instance of that class.
from abc import ABC, abstractmethod
class ParentClass(ABC):
    @abstractmethod
    def method(self)
    
Note: Methods with @abstractmethod decorators must be defined in the child class
Abstract methods must be defined in child classes for proper implementation of inheritance.
'''
from abc import ABC, abstractmethod

class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)

#shape = Shape()
#square = Square(5)
# this code will not compile since Shape has abstract methods without
# method definitions in it


'''
Aggregation: the lifetime of the owned object does not depend on the lifetime of the owner.
The owner object could get deleted, but the owned object can continue to exist in the program. 
In aggregation, the parent only contains a reference to the child, which removes the child’s dependency.
Aggregation is when objects have their own life cycle and child object can associate with only one owner object.
'''
class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country Name:", self.name)
        print("Country Population", self.population)


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person Name:", self.name)
        self.country.printDetails()


c = Country("Wales", 1500)
p = Person("Joe", c)
p.printDetails()
# deletes the object p
del p
print("")
c.printDetails()

'''
composition: the lifetime of the owned object depends on the lifetime of the owner.
Composition relationships are Part-of relationships where the part must constitute a segment of the whole object. 
We can achieve composition by adding smaller parts of other classes to make a complex unit.
'''
class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details:", self.capacity)

class Tires:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires:", self.tires)

class Doors:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of doors:", self.doors)

class Car:
    def __init__(self, eng, tr, dr, color):
        self.eObj = Engine(eng)
        self.tObj = Tires(tr)
        self.dObj = Doors(dr)
        self.color = color

    def printDetails(self):
        self.eObj.printDetails()
        self.tObj.printDetails()
        self.dObj.printDetails()
        print("Car color:", self.color)

car = Car(1600, 4, 2, "Grey")
car.printDetails()

