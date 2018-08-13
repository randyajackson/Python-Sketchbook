#Python variables are more like pointers than data storage areas.

#For assignments:
#1.Assignments create object references.
#2.Names are created when first assigned.
#3.Names must be assigned before being referenced
#4.Some operations perform assignments implicitly.
#Implicit variables are variables that you do not define.

spam = 'Spam' #Basic form
spam, ham = 'yum', 'YUM' #Tuple assignment (positional)
[spam, ham] = ['yum', 'YUM'] #List assignment (positional)
a, b, c, d = 'spam' #Sequence assignment, generalized

a, *b = 'spam' #Extended sequence unpacking (Python 3.X)
# a is assigned 's', and b is assigned 'pam'.


spam = ham = 'lunch' #Multiple-target assignment
spam += 'test' #Augmented assignment (equivalent to spams = spams + 42)
print(spam)

#Because Python creates a temporary tuple
#that saves the original values of the variables on the right while the statement runs,
#unpacking assignments are also a way to swap two variables’ values without creating
#a temporary variable of your own—the tuple on the right remembers the prior values
#of the variables automatically:

nudge = 1
wink = 2
nudge, wink = wink, nudge # Tuples: swaps values

string = 'SPAM' #extended unpacking
a, b, c, d = string # Same number on both sides
print(a, d)

a, b, c = string[0], string[1], string[2:] #from 2 to end
print(a,b,c)

print(list(string[:2]) + [string[2:]] )

((a, b), c) = ('SP', 'AM')
print(a,b,c)

#extended unpacking examples
seq = [1, 2, 3, 4]

*a, b, c = seq
print(a,b,c)
a, *b, c = seq
print(a,b,c)
a, b, *c = seq
print(a,b,c)

red, green, blue = range(3)
print(red, blue)

a, b, c, d, *e = seq #e gets empty case not error
print(a, b, c, d, e)

#a*,  = seq does not work

a = b = c = 'spam'
print(a,b,c)

a = b = []
b.append(42)
print(a, b)
#problem here since a and b refer to same object
a = []
b = []
#or
a, b = [], []
b.append(42)
print(a,b)

#Augmented assignments
#X += Y X &= Y X −= Y X |= Y
#X *= Y X ^= Y X /= Y X >>= Y
#X %= Y X <<= Y X **= Y X //= Y

S = "spam"
S += " SPAM"
print(S)

#Python now supports statements like X += Y, it still does not
#have C’s auto-increment/decrement operators (e.g., X++, −−X).

#Variable names must start with an underscore or letter, which can be followed by
#any number of letters, digits, or underscores.

#reserved words
#False class finally is return
#None continue for lambda try
#True def from nonlocal while
#and del global not with
#as elif if or yield
#assert else import pass
#break except in raise

