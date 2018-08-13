#Just about everything related to names, including scope classification, happens at assignment
#time in Python

# all names assigned inside a function are associated with that function’s namespace,
#and no other

#A name X assigned outside a given def (i.e., in a
#different def or at the top level of a module file) is a completely different variable
#from a name X assigned inside that def.

X = 99 # Global (module) scope X
def func():
 X = 88 # Local (function) scope X: a different variable
 return X

print(func())

#When you hear “global” in Python, think “module.”

#With a
#def statement:
#• Name assignments create or change local names by default.
#• Name references search at most four scopes: local, then enclosing functions (if any),
#then global, then built-in.
#• Names declared in global and nonlocal statements map assigned names to enclosing
#module and function scopes, respectively.

#When you use an unqualified name inside a function, Python searches up to four scopes—
#the local (L) scope,
#then the local scopes of any enclosing (E) defs and lambdas,
#then the global (G) scope,
#and then the built-in (B) scope—

X = 99

def func(Y):
 Z = X + Y #Y is local, X is global
 return(Z)

print(func(1))

#global: X, func
#local: Y, Z

#def hider():
# open = 'spam' # Local variable, hides built-in here
# ...
# open('data.txt') # Error: this no longer opens a file in this scope!

X = 88 # Global X
def func():
 X = 99 # Local X: hides global, but we want this here
func()
print(X) # Prints 88: unchanged

#We’ve added a global declaration to the example here, such that the X inside the def
#now refers to the X outside the def; they are the same variable this time, so changing
#X inside the function changes the X outside it.

y, z = 1, 2 # Global variables in module
def all_global():
 global x # Declare globals assigned
 x = y + z # No need to declare y, z: LEGB rule

X = 99
def func1():
 global X
 X = 88
def func2():
 global X
 X = 77

func1()
func2()
print(X)

X = 99 # Global scope name: not used
def f1():
 X = 88 # Enclosing def local
 def f2():
  print(X) # Reference made in nested def
 f2()
f1() # Prints 88: enclosing def local

#factory function
def maker(N):
 def action(X): # Make and return action
  return X ** N # action retains N from enclosing scope
 return action

#This defines an outer function that simply generates and returns a nested function

f = maker(2)

print(f(3))
print(f(4))

# the nested function remembers integer 2, the value of the variable N in maker
# if we now call the outer function again, we get back a new nested
# function with different state information attached

f = maker(3)

print(f(3))
print(f(4))

def maker(N):
 return lambda X: X ** N # lambda functions retain state too

print('lambda')
h = maker(3)
print(h(2))

def f1():
 x = 88
 def f2(x=x): # Remember enclosing scope X with defaults
  print(x)
 f2()

f1() # Prints 88

#x=x means that the argument x will default to the value of x in the enclosing scope

#—in the Pythonic view, flat is generally better than nested.

# if a lambda or def defined
#within a function is nested inside a loop, and the nested function references an enclosing
#scope variable that is changed by that loop, all functions generated within the loop will
#have the same value

def f1():
 x = 99
 def f2():
   def f3():
    print(x) # Found in f1's local scope!
   f3()
 f2()
f1()

#we should note that scopes may nest arbitrarily, but only
#enclosing function def statements (not classes, described in Part VI) are searched when
#names are referenced

# nonlocal both allows assignment to names in enclosing function scopes
# and limits scope lookups for such names to enclosing defs

#nonlocal allows a nested function to change one or more names defined in a
#syntactically enclosing function’s scope

def tester(start):
 state = start  # Referencing nonlocals works normally

 def nested(label):
  print(label, state)  # Remembers state in enclosing scope

 return nested

F = tester(0)
print(F('spam'))
print(F('ham'))

def tester(start):
 state = start # Each call gets its own state
 def nested(label):
  nonlocal state # Remembers state in enclosing scope
  print(label, state)
  state += 1 # Allowed to change it if nonlocal
 return nested

F = tester(0)
print(F('spam'))
print(F('ham'))
print(F('spam'))
print(F('ham'))

#spam = 99
# def tester():
#  def nested():
#   nonlocal spam # Must be in a def, not the module!

def tester(start):
 def nested(label):
    print(label, nested.state)  # nested is in enclosing scope
    nested.state += 1  # Change attr, not nested itself
 nested.state = start  # Initial state after func defined
 return nested

F = tester(0)
print(F('spam'))
print(F('ham'))

