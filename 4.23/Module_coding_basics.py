# Python modules are easy to create; they’re just files of Python program code created
# with a text editor. You don’t need to write special syntax to tell Python you’re making
# a module; almost any text file will do. Because Python handles all the details of finding
# and loading modules, modules are also easy to use; clients simply import a module, or
# specific names a module defines, and use the objects they reference.

# To define a module, simply use your text editor to type some Python code into a text
# file, and save it with a “.py” extension; any such file is automatically considered a
# Python module

from module1 import printer
import module1

module1.printer('test but longer')
printer('test')

# When a module is imported, Python maps the internal module name to an external
# filename by adding a directory path from the module search path to the front, and
# a .py or other extension at the end. For instance, a module named M ultimately maps
# to some external file <directory>\M.<extension> that contains the module’s code.

# As mentioned in the preceding chapter, it is also possible to create a Python module by
# writing code in an external language such as C, C++, and others (e.g., Java, in the
# Jython implementation of the language). Such modules are called extension modules,
# and they are generally used to wrap up external libraries for use in Python scripts.

# import fetches the module as a whole, so you
# must qualify to fetch its names; in contrast, from fetches (or copies) specific names out
# of the module.

test = module1.printer
test('This is a test')

# when we use a * instead of specific
# names, we get copies of all names assigned at the top level of the referenced module.

from module1 import * # Copy out _all_ variables
printer('Hello world!')

# As one consequence, because top-level code in a module file is usually executed only
# once, you can use it to initialize variables.

import simple
print(simple.spam, 'is spam from simple')

# Second and later imports don’t rerun the module’s code; they just fetch the already
# created module object from Python’s internal modules table.

simple.spam = 2 # Change attribute in module
import simple # Just fetches already loaded module
print(simple.spam) # Code wasn't rerun: attribute unchanged

#Just like def, import and from are executable statements, not compile-time declarations.

# Also, like def, the import and from are implicit assignments:
# • import assigns an entire module object to a single name.
# • from assigns one or more names to objects of the same names in another module

from small import x, y, z # Copy two names out x = 1 y = [1,2]
x = 42 # Changes local x only
y[0] = 42 # Changes shared mutable in place
z = 70

print(x, ' ', y[0], y)
print(z, 'first instance')


import small # Get module name
small.z = 3000
print(small.z, 'second instance')

# z is in one module, small.z is in another module

#  Note that the change to
# y[0] in the prior session is different; it changes an object, not a name, and the name in
# both modules references the same, changed object.

#  from only copies names from one module
# to another; it does not assign the module name itself

# from can silently overwrite variables

#  from module import * can cause problems, silently overwrite multiple if not careful

#---------------------------------------------------
# The only time you really must use import instead of from is when you must use the same
# name defined in two different modules

# # M.py
# def func():
#  ...do something...
# # N.py
# def func():
#  ...do something else...

# import M, N # Get the whole modules, not their names
# M.func() # We can call both names now
# N.func() # The module names make them unique

# from M import func as mfunc # Rename uniquely with "as"
# from N import func as nfunc
# mfunc(); nfunc() # Calls one or the other

# ^ this way works for froms, the as call

# Modules are probably best understood as simply packages of names

#  The first time a module is imported
# anywhere in a system, Python creates an empty module object and executes the
# statements in the module file one after another, from the top of the file to the
# bottom.

import module2

# import statements really assign module objects to names,
# and any type of assignment to a name at the top level of a file generates a module
# attribute.

#  internally, module namespaces are stored as dictionary objects

print(list(module2.__dict__.keys()))
print(list(name for name in module2.__dict__.keys() if not name.startswith('__')))

import mod1

# The reload function forces an already loaded module’s code to be reloaded and
# rerun. Assignments in the file’s new code change the existing module object in
# place

# Unlike import and from:
# • reload is a function in Python, not a statement.
# • reload is passed an existing module object, not a new name.
# • reload lives in a module in Python 3.X and must be imported itself

# Clients that used from to fetch attributes
# in the past won’t be affected by a reload; they’ll still have references to the old
# objects fetched before the reload

import changer
changer.printer()

# if changer.py was to change after the first call
from imp import reload
reload(changer)
changer.printer()
reload(changer)
changer.printer()
