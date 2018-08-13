# like a list that cannot be changed—tuples are sequences, like lists, but they are immutable, like strings.

#The value of some objects can change. Objects whose value can change are said to be mutable;
# objects whose value is unchangeable once they are created are called immutable.

T = (1, 2, 3, 4) # A 4-item tuple
print(len(T))

T += (5,6) #concatenation
print(T)

print(T.index(5)) #index of 5
print(T.count(5)) #number of times that 5 is in the list

#T[0] = 2 will not work since immutable

#to change

T = (2,) + T[1:]
print(T)

#Like lists and dictionaries, tuples support mixed types and nesting, but they don’t grow
# and shrink because they are immutable

# If you pass a collection of objects around your program as a list, it can be changed
#anywhere; if you use a tuple, it cannot.

