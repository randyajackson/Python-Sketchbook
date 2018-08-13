if 1:
    print('true') #need a /n after

x = 'a'
if x =='x':
    print("this is x")
elif x =='3':
    print("this is 3")
else:
    print('this is a')

#there
#is no switch or case statement in Python that selects an action based on a variable’s
#value. Instead, you usually code multiway branching as a series of if/elif tests, as in
#the prior example, and occasionally by indexing dictionaries or searching lists

choice = 'carrot'
print({'spam': 'chose spam',        # A dictionary-based 'switch'
       'carrot': 'chose carrot',    # Use has_key or get for default
       'ham': 'chose ham'} [choice])

#handling switch defaults

branch = {'cheese': "chose cheese",
          'carrot': "chose carrot"}
print(branch.get(choice, "bad choice"))

#alternate using if

if choice in branch:
    print(branch[choice])
else:
    print('not present')

#alternate using try

try:
    print(branch[choice])
except KeyError:
    print('not present')

#1. Statements execute one after another, until you say otherwise
#Because Python’s path through a program is
#called the control flow, statements such as if that affect it are often called controlflow
#statements.

#2. Block and statement boundaries are detected automatically
#Similarly, Python statements are not normally terminated
#with semicolons; rather, the end of a line usually marks the end of the
#statement coded on that line

#3.Compound statements = header + “:” + indented statements

#4.Blank lines, spaces, and comments are usually ignored.

##########################################################Block Delimiters: Indentation Rules

#All statements indented
#the same distance to the right belong to the same block of code.

x = 1
if x:
    y = 2
    if y:
        print('block2')
    print('block1')
print('block0')

# Python doesn’t care
#how you indent your code; it only cares that it’s done consistently

# Python lets you continue typing a statement on the next line if you’re coding
#something enclosed in a (), {}, or [] pair
#Continuation lines—lines 2 and beyond of the statement
#—can start at any indentation level you like, but you should try to make them align
#vertically for readability if possible.

#parenthesis can be used for multi-line
a = b = c = d = e = f = 1

if (a == b and c == d and
    d == e and e == f):
    print('new')

x = 1; y = 2; print(x) # More than one simple statement
#semi-colon allows more commands on one line

#Python lets you move a compound statement’s body up to the header line,
#provided the body contains just simple (noncompound) statements.
if True: print('true')

#All objects have an inherent Boolean true or false value.
#• Any nonzero number or nonempty object is true.
#• Zero numbers, empty objects, and the special object None are considered false.
#• Comparisons and equality tests are applied recursively to data structures.
#• Comparisons and equality tests return True or False (custom versions of 1 and 0).
#• Boolean and and or operators return a true or false operand object.
#• Boolean operators stop evaluating (“short circuit”) as soon as a result is known

#Boolean operators are typed out as
#words in Python (instead of C’s &&, ||, and !). Also, Boolean and and or operators return
#a true or false object in Python, not the values True or False

#Magnitude comparisons such as these return True or False as their truth results
# 23 > 45 returns False = 0

#On the other hand, the and and or operators always return an object

# Python stops at the first true operand it finds.

print(2 or 3) # 2 and 3 are both true, python returns first true, which is 2
print([] or 4)

#“if X then
#Y else Z.”

X = []
A = 'Y' if X else 'Z'
print(A)

X = 9
A = 'Y' if X else 'Z'
print(A)

print(['f', 't'][bool('')])
print(['f', 't'][bool('spam')])

#tmp1, tmp2 = f1(), f2()
#if tmp1 or tmp2: ...
#ensures a value is gathered

L = [1, 0, 2, 0, 'spam', '', 'ham', []]
print(list(filter(bool, L))) # Get true values