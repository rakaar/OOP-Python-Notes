'''
repr: to make things clear
str: to make things readable
'''


class Employee:

    bonus = 100

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def increase_salary(self):  # a regular method
        self.salary = self.salary + self.bonus

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.firstName, self.lastName, self.salary)


emp_1 = Employee("jan", "doe", 100)
print(emp_1)
