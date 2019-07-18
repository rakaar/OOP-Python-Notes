'''
regular methods: methods that take instance as an argument by default
class methods: methods that take class as an argument by default
static methods: just ordinary functions
decorators: things needed to define method type unless its a regular method
alternative constructors: class methods that are capable of creating instances other than __init__
'''


class Employee:

    # class variable
    bonus = 100

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def fullName(self):
        return self.firstName + ' ' + self.lastName

    def increase_salary(self):  # a regular method
        self.salary = self.salary + self.bonus

    # a function that takes class as a argument: class method
    @classmethod  # this is a decorator which tells that this is a class method
    def change_class_bonus(cls, increment):
        cls.bonus += increment

    # a ordinary function in a class
    @staticmethod  # decorator required to tell that this is a regular function
    def subtract(x, y):
        return x - y

    # a alternative constructor: able to create an instance
    @classmethod
    def from_string(cls, the_string):
        first, last, salary = the_string.split('-')
        return cls(first, last, salary)


# Suppose I want a method that takes class as an argument an increases the bonus
# one thing that can be simply done is
Employee.bonus = 200
print(Employee.bonus)  # 200

Employee.change_class_bonus(800)
print(Employee.bonus)  # 200+800 = 1000

print(Employee.subtract(1, 2))  # 1-2 = -1

# using the alternative constructor
alt_emp = Employee.from_string('alt-emp-100')
print(alt_emp.firstName)  # alt
print(alt_emp.lastName)  # emp
print(alt_emp.salary)  # 100
