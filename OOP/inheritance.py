'''
Inheritance, as the name suggests, is a process of inheriting features.
It is a technique of building new classes called derived classes from the existing class called a base class by inheriting
the features of the base class. The features include different attributes and behavioral methods.



Inheritance is one of the powerful features of OOP. In the derived class, we can add extra features and also can override
the data members and methods from the parent.For example, if the vehicle is the parent class, then cars, buses, and trucks
are the derived classes which have inherited all the features of parent class vehicle with many more additional features as well.

Syntax

class derived_class_name(base_class_name):
  ##Body of the derived class

'''

# example 1st
#
class Person:
    def __init__(self):
        pass


# Single level inheritance
class Employee(Person):
    def __init__(self):
        pass


# Multi-level inheritance
class Manager(Employee):
    def __init__(self):
        pass


# Multiple Inheritance
class Enterprenaur(Person, Employee):
    def __init__(self):
        pass


# another example 2
class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    pass


x = Robot("Marvin")
y = PhysicianRobot("James")
print(x, type(x))
print(y, type(y))
y.say_hi()


# example 4
class Vehicle:  # parent class
    "Parent Class"

    def __init__(self, price):
        self.price = price

    def display(self):
        print('Price = $', self.price)


class Category(Vehicle):  # derived class
    "Child/Derived class"

    def __init__(self, price, name):
        Vehicle.__init__(self, price)
        self.name = name

    def disp_name(self):
        print('Vehicle = ', self.name)


obj = Category(1200, 'BMW')
obj.disp_name()
obj.display()
