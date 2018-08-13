L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    L[i] += 10

print(L)

L = [x + 10 for x in L]

print(L)

# In Python, most people find that
#a list comprehension simply looks like a backward for loop.

#—a new list containing x + 10, for every x in L

#Using List Comprehensions on Files
lines = [line.rstrip() for line in open('script2.py')]
print(lines)

#line.readlines() puts whole file in memory, above is cheaper/faster

print( [line.rstrip().upper() for line in open('script2.py')] )

print( [line.split() for line in open('script2.py')] )

print( [line.rstrip() for line in open('script2.py') if line[0] == 'p'] )

print([x + y for x in 'abc' for y in 'lmn'])

print( list(map(str.upper, open('script2.py'))))

print( sorted(open('script2.py')) )

print(list(zip(open('script2.py'), open('script2.py'))))

print(list(enumerate(open('script2.py'))))

print(list(filter(bool, open('script2.py'))))

print('&&'.join(open('script2.py')))

print()
a, b, c, d = (line.rstrip() for line in open('script2.py'))
print(a,d, end=" ")

print()

print(sum([3, 2, 4, 1, 5, 0])) # sum expects numbers only

print(any(['spam', '', 'ni']))

print(all(['spam', '', 'ni']))

print(max([3, 2, 5, 1, 4]))

print(min([3, 2, 5, 1, 4]))

X = (1, 2)
Y = (3, 4)

print(list(zip(X, Y))) # Zip tuples: returns an iterable

A, B = zip(*zip(X, Y)) #unzips
print(A)
print(B)