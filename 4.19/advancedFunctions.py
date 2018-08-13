#When you start using functions in earnest, you’re faced
#with choices about how to glue components together—for instance,
# how to decompose a task into purposeful functions (known as cohesion),
# how your functions should communicate (called coupling), and so on

#Coupling: use arguments for inputs and return for outputs
#Coupling: use global variables only when truly necessary
#Coupling: don’t change mutable arguments unless the caller expects it

#Cohesion: each function should have a single, unified purpose

#Size: each function should be relatively small.

#Coupling: avoid changing variables in another module file directly

#The more self-contained a function is, the easier it will be to understand, reuse, and modify

#recursion

def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:]) # Call myself recursively

print(mysum([1,2,3,4]))

#recursion used less in python
L = [1, 2, 3, 4, 5]
sum = 0
for x in L: sum += x
print(sum)

#less recursion = less memory on the call stack

#case like [1, [2, [3, 4], 5], 6, [7, 8]] needs recursion

def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]] # Arbitrary nesting
print(sumtree(L)) # Prints 36

#Also note that standard Python limits the depth of its runtime call stack—crucial to
#recursive call programs—to trap infinite recursion errors. To expand it, use the sys
#module:
#>>> sys.getrecursionlimit() # 1000 calls deep default
#1000
#>>> sys.setrecursionlimit(10000) # Allow deeper nesting
#>>> help(sys.setrecursionlimit) # Read more about it

# first-class object model;
# function can be renamed / passed to other functions

def echo(message): # Name echo assigned to function object
    print(message)

X = echo
X("test")

def indirect(func, arg):
    func(arg) # Call the passed-in object by adding ()

indirect(echo, 'Argument call!') # Pass the function to another function

schedule = [ (echo, 'Spam!'), (echo, 'Ham!') ]
for (func, arg) in schedule:
    func(arg)

def make(label): # Make a function but don't call it
    def echo(message):
        print(label + ':' + message)
    return echo

F = make('Spam') # Label in enclosing scope is retained
F('Ham!') # Call the function that make returned
F('Eggs!')

def func(a:'spam'=4, b:(1,10)=5, c:float=6)->int:
    return a + b + c

print(func(1, 2)) # 1 + 2 + 6
print(func.__annotations__)

#annotations being used to specify constraints for argument types or values

#Like def, this expression creates a function to be called later, but it returns the
#function instead of assigning it to a name. This is why lambdas are sometimes known
#as anonymous (i.e., unnamed) functions.

#lambda is an expression, not a statement.
#lambda can appear in places a def is not allowed by Python’s syntax

#lambda’s body is a single expression, not a block of statements
# lambda is designed for coding simple functions, and def handles larger tasks.

f = lambda x, y, z: x + y + z

print(f(2, 3, 4), 'lambda')

#defaults work on lambdas

x = (lambda a="fee", b="fie", c="foe": a + b + c)

print(x("wee"))

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x) # Title in enclosing def scope
    return action # Return a function object

act = knights()
msg = act('robin') # 'robin' passed to x
print(msg)

#lambda comes in handy as a sort of function shorthand that allows
#you to embed a function’s definition within the code that uses it

#lambda is also commonly used to code jump tables, which are lists or dictionaries of
#actions to be performed on demand

L = [lambda x: x ** 2, # Inline function definition
     lambda x: x ** 3,
     lambda x: x ** 4] # A list of three callable functions

for f in L:
    print(f(2)) # Prints 4, 8, 16

print(L[0](3))

lower = (lambda x, y: x if x < y else y)
print(lower('bb', 'aa'))


def action(x):
    return (lambda y: x + y)  # Make and return function, remember x

act = action(99)
print(act(2))

counters = [1, 2, 3, 4]

updated = []
for x in counters:
    updated.append(x + 10) # Add 10 to each item

print(updated, 'counters')

def inc(x): return x + 10 # Function to be run

print(list(map(inc, counters)), 'map')

print(list(map((lambda x: x + 3), counters)), 'map using lambda') # Function expression)

print(list(map(pow, [1, 2, 3], [2, 3, 4])) )

print(list(filter((lambda x: x > 0), range(-5, 5)))) #using filter

from functools import reduce # Import in 3.X, not in 2.X

print(reduce((lambda x, y: x + y), [1, 2, 3, 4])) #reduce

import operator
print(reduce(operator.add, [2, 4, 6]) ) #operator

