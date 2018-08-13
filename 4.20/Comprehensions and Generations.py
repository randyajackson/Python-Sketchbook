print(ord('s'))  # gets the number value of an ascii character

# example of comprehension

res = []
for x in 'spam':
    res.append(ord(x))  # Manual results collection

print(res)
# -------------------
res = list(map(ord, 'spam'))  # Apply function to sequence (or other)

print(res)
# -------------------
res = [ord(x) for x in 'spam']  # Apply expression to sequence (or other)

print(res)

# while map maps a function over an iterable, list comprehensions map an expression over a sequence or other iterable

comp = [x ** 2 for x in range(10)]
print(comp)

# ----------------
comp = [x for x in range(5) if x % 2 == 0]
print(comp)

filterUse = list(filter((lambda x: x % 2 == 0), range(5)))
print(filterUse)

# comprehension doesnt need extra lambda like filter does

# [ expression for target1 in iterable1 if condition1
# for target2 in iterable2 if condition2 ...
# for targetN in iterableN if conditionN ]

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)
# nested for loops

# again with letters
res = [x + y for x in 'spam' for y in 'SPAM']
print(res)

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]
print(M[1], "[Row 1]")
print(M[1][2], "[Row 2, item 3]")

print([row[1] for row in M])  # getting Column 2 in M

print([M[row][1] for row in (0, 1, 2)]) # Using offsets if need to skip columns

print([M[i][i] for i in range(len(M))] ) # Diagonals

#comprehensions make new lists

addTen = [[col + 10 for col in row] for row in M] #nested fors, 3 new lists
print(addTen)

mult = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
# multiplies rows and columns in m * n
print(mult)

#map and comprehension calls run at c level speed
# for loops go through a PVM

print( [line.rstrip() for line in open('myfile')] )

# SQL database api returns lists like
listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]
# way to get age would be
age = [age for (name, age, job) in listoftuple]
print(age)

age = list(map((lambda row: row[1]), listoftuple))  # faster
print(age)

#biggest difference between map and list comprehensions in Python 3.X
# is that map is an iterable

#generator functions because they generate a sequence of values over time

# when created, they are compiled specially into
#an object that supports the iteration protocol. And when called, they don’t return a
#result: they return a result generator that can appear in any iteration context

#generator example

def gensquares(N):
    for i in range(N):
        yield i ** 2  # Resume here later

for i in gensquares(5): # Resume the function
    print(i, end=' : ') # Print last yielded value

# the first iteration starts the function and gets
# its first result; thereafter, control returns to the function after its yield statement each
# time through the loop:

x = gensquares(4)
print(x)
# You get back a generator object that supports the iteration protocol

# They allow functions to avoid doing all the work up front, which is
# especially useful when the result lists are large or when it takes a lot of computation to
# produce each value.

ui = (t ** 2 for t in range(4)) # Generator expression: make an iterable
# like comprehension but in parenthesis instead
# they return a generator object

print(ui.__next__(), 'generator')
print(ui.__next__(), 'generator')
print(ui.__next__(), 'generator')
print(ui.__next__(), 'generator')

gen = ''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))
print(gen)

#  they are probably best used only for very large result sets,
# or applications that cannot wait for full results generation

line = 'aaa,bbb,ccc'
print(''.join(x * 2 for x in line.split(',')) )
print(''.join([x.upper() for x in line.split(',')])) # Makes a pointless list

print(list(x * 2 for x in (abs(x) for x in (-1,-2, 3, 4))) ) # Nested generators

# generator versus filter
print(''.join(x.upper() for x in line.split() if len(x) > 1))

print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))

# Generator Functions Versus Generator Expressions

# Generator functions
# A function def statement that contains a yield statement is turned into a generator
# function. When called, it returns a new generator object with automatic retention
# of local scope and code position; an automatically created __iter__ method that
# simply returns itself; and an automatically created __next__ method (next in 2.X)
# that starts the function or resumes it where it last left off, and raises StopItera
# tion when finished producing results.

# Generator expressions
# A comprehension expression enclosed in parentheses is known as a generator expression.
# When run, it returns a new generator object with the same automatically
# created method interface and state retention as a generator function call’s results
# —with an __iter__ method that simply returns itself; and a _next__ method
# (next in 2.X) that starts the implied loop or resumes it where it last left off, and
# raises StopIteration when finished producing results.

def timesfour(S): # Generator function
 for c in S:
    yield c * 4

G = timesfour('spam')
print(list(G)) # Iterate automatically

#  both generator functions and generator expressions are
# their own iterators and thus support just one active iteration—

# If you iterate over the results stream manually with multiple iterators, they will all point
# to the same position

# Moreover, once any iteration runs to completion, all are exhausted—we have to make
# a new generator to start again:

def f(a, b, c): print('%s, %s, and %s' % (a, b, c))

print(f(*(i for i in range(3))))    # Unpack generator expression values

D = dict(a='Bob', b='dev', c=40.5)
print(f(**D))
print(f(*D))

#  starred arguments can unpack an iterable into individual arguments

S = 'spam'
for i in range(len(S)): # For repeat counts 0..3
    S = S[1:] + S[:1] # Move front item to the end
    print(S, end=' ')

print()
def scramble(seq):
    for i in range(len(seq)): # Generator function
        yield seq[i:] + seq[:i] # Yield one item per iteration
print(*list(scramble('test')))
print(*list(scramble('toast')))

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(F(S)) #wont work
#needs list
print(*list(F(S)))
print(list(F([1,2,3])))

#use of permutation
def permute2(seq):
    if not seq: # Shuffle any sequence: generator
        yield seq # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:] # Delete current node
            for x in permute2(rest): # Permute the others
                yield seq[i:i+1] + x # Add node at front

perm = permute2([4,33,55,6])

while perm:
    print(perm.__next__(),perm.__next__(),perm.__next__())

# Explicit is better than implicit.

#wrapping generator in list forces them to print all results at once

