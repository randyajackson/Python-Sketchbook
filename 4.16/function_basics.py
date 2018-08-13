#—your function does not exist until Python reaches and runs the def
#def creates an object and assigns it to a name

#lambda creates an object but returns it as a result

#return sends a result object back to the caller.

#yield sends a result object back to the caller, but remembers where it left off

#global declares module-level variables that are to be assigned

#By default, all names assigned in a function are local to that function and exist only while the function runs

#nonlocal declares enclosing function variables that are to be assigned
#enclosing functions to serve as a place to retain state—information remembered between function calls—without using shared global names.

#The Python return statement can show up anywhere in a function body;

#If the value is omitted, return sends back a None.

#The Python def is a true executable statement: when it runs, it creates a new function
#object and assigns it to a name. (Remember, all we have in Python is runtime; there is
#no such thing as a separate compile time.)

#def is much like an = statement

def times(x, y): # Create and assign function
    return x * y # Body executed when called

print(times(3,4))

x = times(3.4,17)
print(x)

print(times('test ', 4))

#* is just a dispatch mechanism that routes control to the objects being processed.

# in Python, your code is not supposed to care about specific data types

#By and large, we code to object interfaces in Python, not data types

#duck typing—the essential idea
#being that your code is not supposed to care if an object is a duck, only that it quacks

def intersect(seq1, seq2):
    res = [] # Start empty
    for x in seq1: # Scan seq1
        if x in seq2: # Common item?
            res.append(x) # Add to end
    return res

A = [1,2,3,4,5]
B = [1,7,6,3,4]

print(intersect(A,B))

A = "SPAM"
B = "SCAM"

print(intersect(A,B))

C = [x for x in A if x in B]    #quicker way to do intersect using comprehension

print(C)

x = intersect([1, 2, 3], (1, 4))  # Mixed types
print(x)

#the variable res inside intersect is what in Python is called a local variable




