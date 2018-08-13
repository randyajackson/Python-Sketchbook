#Arguments are passed by automatically assigning objects to local variable names.

#passed by pointer. Objects passed as arguments are never automatically copied.

#Assigning to argument names inside a function does not affect the caller.

#Changing a mutable object argument in a function may impact the caller

#Immutable arguments are effectively passed “by value.”

#Mutable arguments are effectively passed “by pointer.”

def f(a): # a is assigned to (references) the passed object
    a = 99 # Changes local variable a only

b = 88
f(b) # a and b both reference same 88 initially
print(b) #b doesnt change


def changer(a, b): # Arguments assigned references to objects
 a = 2 # Changes local name's value only
 b[0] = 'spam' # Changes shared object in place

X = 1
L = [1, 2] # Caller:
changer(X, L)# Pass immutable and mutable objects

print(X,L)# X is unchanged, L is different!

#Really, the second assignment statement in changer doesn’t change b—it changes part
#of the object that b currently references

X = 1
a = X # They share the same object
a = 2 # Resets 'a' only, 'X' is still 1
print(X)

L = [1, 2]
b = L # They share the same object
b[0] = 'spam' # In-place change: 'L' sees the change too
print(L)

#if you dont want to change the caller, make a copy

def changer(a, b):
    b = b[:] # Copy input list so we don't impact caller
    a = 2
    b[0] = 'spam' # Changes our list copy only
    print(a,b, "in changer")

L = [1, 2]
changer(X, L[:])
print(X,L, "not in changer")

# because return can send back any sort of object, it
# can return multiple values by packaging them in a tuple or other collection type

def multiple(x, y):
    x = 2 # Changes local names only
    y = [3, 4]
    return x, y # Return multiple new values in a tuple

X = 1
L = [1, 2]
X, L = multiple(X, L) # Assign results to caller's names

print(X, L)

#If you don’t use any special matching syntax, Python matches names by position from left to right

def f(a, b, c): print(a, b, c)

f(1, 2, 3)

#you can specify by name and not just position

f(c=3, b=2, a=1)

#defaults, a is required, b and c are not
def f(a, b=2, c=3): print(a, b, c) # a required, b and c optional

f(1)
f(1,5)
f(2,c=6,b=8)

#Python collects all the positional arguments into a new tuple and assigns the variable args to that tuple
def f(*args): print(args)
f(1,2,3,4,5,6,7,8,9,1,2)
f()

#The ** feature is similar, but it only works for keyword arguments—it collects them
#into a new dictionary, which can then be processed with normal dictionary tools.

def f(**args): print(args)
f(a=1,b=2,c=3,d=4,e=5)

def f(a, *pargs, **kargs): print(a, pargs, kargs)
f(1,2,3,x=4,y=5)

# * unpacks a library
# and ** unpacks a dictionary

def function(a, b, c, d): print(a, b, c, d)

args = (1, 2)
args += (3, 4)
function(*args)

#dict = {'aone': 3, 'bone': 2, 'cone': 3}
#dict['done'] = 4
#function(**dict)

function(*(1, 2), **{'d': 4, 'c': 3})

# everything after * must be passed keywords
def kwonly(a, *, b, c):
    print(a, b, c)

kwonly(1, c=3, b=2)

def kwonly(a,*b, c): #a and b can be default, c must be keyword
    print(a,b,c)

kwonly(1,3,c=4)

## example of the use of *args to find the min from unknown amount of inputs
def min3(*args):
    tmp = list(args) # Or, in Python 2.4+: return sorted(args)[0]
    tmp.sort()
    return tmp[0]

print(min3(11,3333,22,333,444,222,1))
print(min3([1,2,3],[4,5,6],[7,8,9]))

