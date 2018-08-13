# The class statement creates a class object and assigns it a name

# Assignments inside class statements make class attributes

# Class attributes provide object state and behavior

class FirstClass: # Define a class object

    def setdata(self, value): # Define class's methods
        self.data = value # self is the instance

    def display(self):
        print(self.data) # self.data: per instance

x = FirstClass() # Make two instances
y = FirstClass()

x.setdata("King Arthur") # Call methods: self is x
y.setdata(3.14159)

x.display()
y.display()

# there are no declarations for instance attributes

x.data = "New value" # Can get/set attributes
x.display() # Outside the class too

# we could even generate an entirely new attribute in the instance’s
# namespace by assigning to its name outside the class’s method functions

x.anothername = "spam"  # Can set new attributes here too!

# Superclasses are listed in parentheses in a class header

# Classes inherit attributes from their superclasses

# Instances inherit attributes from all accessible classes.

# Each object.attribute reference invokes a new, independent search

class SecondClass(FirstClass): # Inherits setdata

    def display(self): # Changes display
        print('Current value = "%s"' % self.data)

z = SecondClass()
z.setdata(42) # Finds setdata in FirstClass
z.display()

# # food.py
# var = 1 # food.var
# def func(): ... # food.func
# class spam: ... # food.spam
# class ham: ... # food.ham
# class eggs: ... # food.eggs

# major difference between classes and modules:
# operator overloading

# operator overloading lets objects coded with
# classes intercept and respond to operations that work on built-in types: addition, slicing,
# printing, qualification, and so on

# • Methods named with double underscores (__X__) are special hooks
#  Such methods are called automatically when instances appear in built-in
# operations. For instance, if an instance object inherits an __add__ method, that
# method is called whenever the object appears in a + expression. The method’s
# return value becomes the result of the corresponding expression.

# There are no defaults for operator overloading methods, and none are required

class ThirdClass(SecondClass): # Inherit from SecondClass
    def __init__(self, value): # On "ThirdClass(value)"
        self.data = value

    def __add__(self, other): # On "self + other"
        return ThirdClass(self.data + other)

    def __str__(self): # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data

    def mul(self, other): # In-place change: named
        self.data *= other

a = ThirdClass('abc') # __init__ called
a.display()
print(a)

b = a + 'xyz' # __add__: makes a new instance
b += '123'

b.display() # b has all ThirdClass methods

print(b)

a.mul(3) # mul: changes instance in place
print(a)
# __init__ sets the value

# __add__(self,other) b = a + 'xyz'
# a is the self and after plus is the other
# returns a thirdclass object

class Person:
    def __init__(self, name, jobs, age=None): # class = data + logic
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return (self.name, self.jobs)

rec1 = Person('Bob', ['dev', 'mgr'], 40.5) # Construction calls
rec2 = Person('Sue', ['dev', 'cto'])

#def __str__(self): # On "print(self)", "str()" like toString method
# return '[ThirdClass: %s]' % self.data

print(rec1.jobs)
print(rec2.info())

