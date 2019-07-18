class Employee:
    # this is the constuctor function(func that runs by default)
    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def fullName(self):  # this is a regular method': takes instance automatically as an argument
        return self.firstName + ' ' + self.lastName

# the above is a class
# function in a class is called a method
# notice that every method takes self as argument


# lets create instances of the above class
emp1 = Employee("raghavendra", "kaushik", 10)
emp2 = Employee("kaushik", "archak", 20)

print(emp1.salary)  # 10

print(emp1.fullName())  # raghavendra kaushik
# notice that when you call a method you need to specify those empty paranthesis,
# it seems no arg is passed but behind the scene self is passed automatically,
# when emp1.fullName is used it is actually converted to this thing below:

print(Employee.fullName(emp1))
# here you need to specify the instance you want to perform the method on, since it is being called from the class
