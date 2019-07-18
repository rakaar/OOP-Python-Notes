'''
inheritance: taking the property from the parent
sub-class: the class that has inherited from another class
super(): allows us to use the parent class' attributes
method of resolution:
    the order in which python looks for classes while creating instances
'''


class Employee:

    bonus = 100

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def increase_salary(self):  # a regular method
        self.salary = self.salary + self.bonus


class Developer(Employee):  # Developer subclass inherting from Employee subclass

    # Suppose we want to add another attribute called language, we need to define the __init__ method for that

    def __init__(self, firstName, lastName, salary, language):
        # this is a 'super' easy way, instead of Repeating the process self.something = something
        super().__init__(firstName, lastName, salary)
        self.language = language


dev_1 = Developer("jan", "doe", 100, "python3")
emp_1 = Employee("alice", "james", 100)

# changing class variables in subclass won't affect the parent class
emp_1.increase_salary()
print(emp_1.salary)  # 100 +100 = 200

Developer.bonus = 500
dev_1.increase_salary()
print(dev_1.salary)  # 100 + 500 = 600

emp_1.increase_salary()
print(emp_1.salary)  # 200+100= 300

# this shows the method of resolution of order as
# 1.Developer
# 2.Employee
# 3.builtins.object
print(help(Developer))

# will return true or false
isinstance(dev_1, Developer)  # True
isinstance(dev_1, Employee)  # True

issubclass(Developer, Employee)  # True
