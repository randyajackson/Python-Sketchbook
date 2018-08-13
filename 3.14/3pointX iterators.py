#One of the fundamental distinctions of Python 3.X is its stronger emphasis on iterators
#than 2.X

#we’ve had to wrap up some function
#and method call results in a list(...) call in order to force them to produce all their
#results at once for display:

# values in 3.X are exhausted
#after a single pass:

R = range(10) # range returns an iterable, not a list

I = iter(R) # Make an iterator from the range iterable
print(next(I)) # Advance to next result
# What happens in for loops, comprehensions, etc.
print(next(I)) # Advance to next result
print(next(I)) # Advance to next result
print(list(range(10)))

D = dict(a=1,b=2,c=3)
print(D)

K = D.keys()
V = D.values()
print(list(K))
print(list(V))
for (k,v) in D.items(): print(k,v, end=" ")

print()
for key in D: print(key, end=' ') # Still no need to call keys() to iterate
#key is iterable in 3.x

print()
#convert
#keys views first with a list call, or use the sorted call on either a keys view or the
#dictionary itself, as follows.

for k in sorted(D): print(k, D[k], end=' ')

