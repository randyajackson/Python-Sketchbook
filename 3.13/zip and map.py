#the range builtin
#allows us to traverse sequences with for in a nonexhaustive fashion

#the built-in zip function allows us to use for loops to visit multiple sequences
#in parallel—not overlapping in time, but during the same loop.

#zip takes one or more sequences as arguments and returns a series of tuples that pair
#up parallel items taken from those sequences.

L1 = [1,2,3,4]
L2 = [5,6,7,8]

#Like
#range, zip is a list in Python 2.X, but an iterable object in 3.X where we must wrap it
#in a list call to display all its results at once

X = list(zip(L1, L2))
print(X)

for (x,y) in zip(L1,L2):
    print(x, "+", y, "=", x+y)

A=[1,2,3,4,5,6,7]
B=[10,9,8]

print(list(zip(A,B)))

#print(list(map(None, A,B))) doesn't work 3.x

#the zip call used here can
#also be handy for generating dictionaries when the sets of keys and values must be
#computed at runtime

keys = ['spam', 'eggs', 'toast']
values = [1,2,3]

print(list(zip(keys,values)))

D2 = {}

for (x, y) in zip(keys,values): D2[x] = y

print(D2)

#can skip the for with 3.x
D3 = dict(zip(keys,values))
print(D3)

#enumerate to get iterator value
S = 'spam'
for (i, char) in enumerate(S):
    print(char, ' is at position ', i)

#from urllib.request import urlopen
#for line in urlopen('https://mywings.unf.edu'):
#    print(line)
#using for to obtain source from web address