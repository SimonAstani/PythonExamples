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
