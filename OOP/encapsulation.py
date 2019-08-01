'''
Private properties have double underscore (__) in the start, while protected properties have single underscore (_).
By default, all other variable and methods are public.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def _protected_method(self):
        print("protected method")

    def __private_method(self):
        print("privated method")


if __name__ == "__main__":
    p = Person("mohan", 23)
    p._protected_method()  # shows a warning
    p.__private_method()  # throws Attribute error saying no such method exists
