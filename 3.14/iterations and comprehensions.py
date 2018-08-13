# readline returns empty string at end-of-file

#>>> f = open('script2.py') # Read a four-line script file in this directory
#>>> f.readline() # readline loads one line on each call
#'import sys\n'
#>>> f.readline()
#'print(sys.path)\n'
#>>> f.readline()
#'x = 2\n'
#>>> f.readline() # Last lines may have a \n or not
#'print(x ** 32)\n'
#>>> f.readline()


# __next__ raises a built-in StopIteration exception at
#end-of-file instead of returning an empty string

#>>> f = open('script2.py') # __next__ loads one line on each call too
#>>> f.__next__() # But raises an exception at end-of-file
#'import sys\n'
#>>> f.__next__() # Use f.next() in 2.X, or next(f) in 2.X or 3.X
#'print(sys.path)\n'
#>>> f.__next__()
#'x = 2\n'
#>>> f.__next__()
#'print(x ** 32)\n'
#>>> f.__next__()
#Traceback (most recent call last):
 #File "<stdin>", line 1, in <module>
#StopIteration

#all iteration tools
#normally work internally by calling __next__ on each iteration and catching the StopIt
#eration exception to determine when to exit.

for line in open('script2.py'): # Use file iterators to read by lines
    print(line.upper(), end='') # Calls __next__, catches StopIteration

#uses end='' here to suppress adding a \n, because line strings
#already have one (without this, our output would be double-spaced;

#readlines loads entire file into memory

print()

I = [1, 2, 3]
L = iter(I)
print(L.__next__())
print(L.__next__())
print(L.__next__())

#Lists and many other built-in objects, though, are not their own iterators because they
#do support multiple open iterations—for example, there may be multiple iterations in
#nested loops all at different positions. For such objects, we must call iter to start iterating:


#This initial step is not required for files, because a file object is its own iterator.

#AUTO ITERATION

L = [1, 2, 3]

for X in L: # Automatic iteration
    print(X ** 2, end=' ') # Obtains iter, calls __next__, catches exceptions

#MANUAL ITERATION
print()
I = iter(L) # Manual iteration: what for loops usually do

while True:
    try: # try statement catches exceptions
        X = next(I) # Or call I.__next__ in 3.X
    except StopIteration:
        break
    print(X ** 2, end=' ')

D = {'a':1, 'b':2, 'c':3}
print()

for key in D:
    print(key, D[key], end=' ')

R = range(5)
I = iter(R)  # Use iteration protocol to produce results
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(list(range(5)))  # Or use list to collect all results at once

E = enumerate('spam') # enumerate is an iterable too

I = iter(E)

print(I.__next__()) # Generate results with iteration protocol
#(0, 's')
print(I.__next__())
#(1, 'p')
print(list(enumerate('spam'))) # Or use list to force generation to run
