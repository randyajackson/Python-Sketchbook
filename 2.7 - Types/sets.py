X = set('spam') # Make a set out of a sequence in 2.X and 3.X
Y = {'h', 'a', 'm'} # Make a set with set literals in 3.X and 2.7
print(X, Y) # A tuple of two sets without parentheses

print(X & Y) # Intersection

print(X | Y) # Union

print(X - Y)

print(list(set([1, 2, 1, 3, 1]))) # Filtering out duplicates (possibly reordered)

print(set('spam') - set('ham'))# Finding differences in collections

print(set('spam') == set('asmp')) # Order-neutral equality tests (== is False)

# By checking
#for specific types in your code, you effectively break its flexibility—you limit it to
#working on just one type. Without such tests, your code may be able to work on a
#whole range of types.
#This is related to the idea of polymorphism mentioned earlier, and it stems from
#Python’s lack of type declarations. As you’ll learn, in Python, we code to object interfaces
#(operations supported), not to types. That is, we care what an object does, not
#what it is. Not caring about specific types means that code is automatically applicable
#to many of them—any object with a compatible interface will work, regardless of its
#specific type. Although type checking is supported—and even required in some rare
#cases—you’ll see that it’s not usually the “Pythonic” way of thinking. In fact, you’ll
#find that polymorphism is probably the key idea behind using Python well.