class SharedData:
    spam = 42 # Generates a class data attribute

x = SharedData() # Make two instances
y = SharedData()

# We can change it by going
# through the class name, and we can refer to it through either instances or the class

SharedData.spam = 99
print(x.spam)
print(y.spam)# They inherit and share 'spam' (a.k.a. SharedData.spam)

class MixedNames: # Define class
    data = 'spam' # Assign class attr

    def __init__(self, value): # Assign method name
        self.data = value # Assign instance attr

    def display(self):
        print(self.data, MixedNames.data) # Instance attr, class attr

x = MixedNames(1) # Make two instance objects
y = MixedNames(2) # Each has its own data
x.display()
y.display()# self.data differs, MixedNames.data is the same

class NextClass: # Define class

 def printer(self, text): # Define method
    self.message = text # Change instance
    print(self.message) # Access instance

x = NextClass() # Make instance
x.printer('instance call') # Call its method
print(x.message) # Instance changed

class Super:
    def method(self):
        print('in Super.method') # Default behavior

    def delegate(self):
        self.action() # Expected to be defined

class Inheritor(Super): # Inherit method verbatim
    pass

class Replacer(Super): # Replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super): # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super): # Fill in a required method
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()

    print('\nProvider...')
    x = Provider()
    x.delegate()

# class Super(metaclass=ABCMeta):
#  def delegate(self):
#  self.action()
#  @abstractmethod
#  def action(self):
#  pass

# Coded this way, a class with an abstract method cannot be instantiated (that is, we
# cannot create an instance by calling it) unless all of its abstract methods have been
# defined in subclasses

# Assignment (X = value)
# Makes names local by default: creates or changes the name X in the current local
# scope, unless declared global (or nonlocal in 3.X).

# Reference (X)
# Looks for the name X in the current local scope, then any and all enclosing functions,
# then the current global scope, then the built-in scope, per the LEGB rule.
# Enclosing classes are not searched: class names are fetched as object attributes
# instead.

# Because attributes are actually dictionary keys inside Python, there are really two ways
# to fetch and assign their values—by qualification, or by key indexing:
# >>> X.data1, X.__dict__['data1']
# ('spam', 'spam')
# >>> X.data3 = 'toast'
# >>> X.__dict__
# {'data2': 'eggs', 'data3': 'toast', 'data1': 'spam'}
# >>> X.__dict__['data3'] = 'ham'
# >>> X.data3
# 'ham'

