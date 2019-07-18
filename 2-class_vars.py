class Employee:

    # class variable to be used by type -1 self
    bonus = 500

    # class variable to used by type-2 CLASSNAME
    num_of_emps = 0

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        Employee.num_of_emps += 1

    def fullName(self):
        return self.firstName + ' ' + self.lastName

    def increase_salary(self):
        self.salary = self.salary + self.bonus
        # notice that self.NAME is the way we are using to access the class Variable
        # this way is useful when u want to use it per instance/ things that vary per instance


good_emp = Employee("good", "emp", 100)
good_emp.increase_salary()
print(good_emp.salary)

print(Employee.num_of_emps)

# 100 for one,200 for other notice that it is diff for different instances
better_emp = Employee("better", "emp", 200)
# for class variables which  have probablity of varying with instance u use self.NAME
better_emp.increase_salary()
print(better_emp.salary)

# now U can also use class variables with CLASSNAME.name_of_variable but that is preferable when
# they do noy change with instance
print(Employee.num_of_emps)
# like number of employees do not chnage
