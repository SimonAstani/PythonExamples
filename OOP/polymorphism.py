class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_salary(self):
        print("Salary is unknown")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_salary(self):
        print("Salary is", self.salary)


if __name__ == "__main__":
    p = Person("y", 23)
    x = Employee("x", 20, 100000)
    p.show_salary()  # Salary is unknown
    x.show_salary()  # Salary is 100000
