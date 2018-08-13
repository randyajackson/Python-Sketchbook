#In its most complex form, the while statement consists of a header line with a test
#expression, a body of one or more normally indented statements, and an optional
#else part that is executed if control exits the loop without a break statement being
#encountered.
x = 1
while x: # Loop test
 print('statements') # Loop body
 x = 0
 break;

else: # Optional else
 print('error')# Run if didn't exit loop with break

x = 'spam'
while x:
 print(x, end=' ')
 x = x[1:]

a = 0
b = 10
while a < b:
    print(a, end =" ")
    a += 1

#execute a do-while with a break statement

#break
#Jumps out of the closest enclosing loop (past the entire loop statement)

#continue
#Jumps to the top of the closest enclosing loop (to the loop’s header line)

#pass
#Does nothing at all: it’s an empty statement placeholder

#Loop else block
#Runs if and only if the loop is exited normally (i.e., without hitting a break)

# pass is
#roughly to statements as None is to objects—an explicit nothing

def func1():
 pass # Add real code here later

print()
x = 10
while x:
    x -= 1
    if x % 2 != 0: continue #continue skips the print
    else: print(x, end = ' ')

while True:
    name = input('Enter name:') # Use raw_input() in 2.X
    if name == 'stop': break #loop until break

while x: # Exit when x empty
    if match(x[0]):
        print('Ni')
        break # Exit, go around else
    x = x[1:]
else:
    print('Not found') # Only here if exhausted x

##################################################################for loops

#The for statement also supports an optional else block, which works exactly as it does
#in a while loop

#for target in object: # Assign object items to target
 #statements
 #if test: break # Exit loop now, skip else
 #if test: continue # Go to top of loop now
#else:
 #statements # If we didn't hit a 'break'

for x in ["spam", "eggs", "ham"]:
    print(x, end=' ')

sum = 0
for x in [1, 2, 3, 4]:
    sum = sum + x

print(sum)

T = ("and", "I'm", "okay")
for x in T: print(x, end=' ')


T = [(1, 2), (3, 4), (5, 6)]                #works because of tuple assignment
for (a, b) in T: # Tuple assignment at work
    print(a, b)

D = {'a': 1, 'b': 2, 'c': 3}                #dictionary
for key in D:
    print(key, '=>', D[key])

for (key, value) in D.items():
    print(key, '=>', value)

for both in T:
    a, b = both # Manual assignment equivalent
    print(a, b)

for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c)

for (a, *b, c) in[(1,2,3,4), (5,6,7,8)]:
    print(a,b,c)

#nested for loops

items = ["aaa", 111, (4, 5), 2.01] # A set of objects
tests = [(4, 5), 3.14] # Keys to search for

for key in tests:
    for item in items:
        if key == item:
            print(key, "was found")
            break
    else:
        print(key, "was not found")
# uses the else property with for loop

se1 = "spam"
se2 = "scam"
res = []
for x in se1:
    if x in se2:
        res.append(x)

print(res)

file = open('test.txt')

while True:
    char = file.read(1)
    if not char: break
    print(char.upper(), end=" ")

for char in open('test.txt').read():
    print(char.upper(), end=" ")

for line in open('test.txt'): # Use iterators: best for text input
 print(line.rstrip())

 # ^ it doesn’t load the entire file into memory all at once
 #like open('test.txt').readlines()
#File readlines calls can still be useful, though—to reverse a file’s lines, for example,
#assuming its content can fit in memory.

#resist the temptation to count things in Python—

#############range
print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))
#range creates a list so needs a wrapper to display

X = 'spam'
for item in X: print(item, end=' ') # Simple iteration

i = 0
while i < len(X): # while loop iteration
    print(X[i], end=' ')
    i += 1
print()

x = 'spam'
print(len(x))
print(range(len(x)))

for i in range(len(x)):         #longer way to do next loop
    print(x[i], end = " ")

for item in x: print(item, end=' ')

print()
S = 'abcdefghijk'

for i in range(0,len(S), 2): print(S[i], end=" ")

for c in S[::2]: print(c, end=" ")

#The potential advantage to using range here instead is space
#for very large strings, they may save memory.

L = [1,2,3,4,5]

for x in range(len(L)): #the range of the length of L
    L[x] += 1

print(L)




