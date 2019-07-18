'''
@property
a decorator used to access the methods as attributes

setters
allows us to set the attributes

deleter
runs when something is deleted
'''


class Employee:

    bonus = 100

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    # this decorator allows us to access the below function as an attribute
    @property
    def fullname(self):
        return self.firstName + ' ' + self.lastName

    # basically the syntax is funcname(or attribute name to be set).setter and define a function with same name
    @fullname.setter
    def fullname(self, new):
        first, last = new.split(' ')
        self.firstName = first
        self.lastName = last

    @fullname.deleter
    def fullname(self):
        print('deleted')


emp_1 = Employee("jan", "doe", 100)

# Before @property
# print(emp_1.fullname())

#After @property
print(emp_1.fullname)


# BEOFRE USING SETTER
# suppose
emp_1.fullname = "new name"
# error : says can't set an attribute, LETS USE A SETTER THEN !
print(emp_1.fullname)
# AFTER, using setters this will print new name

del emp_1.fullname
