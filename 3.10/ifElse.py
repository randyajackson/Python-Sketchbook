#As mentioned previously, in Python’s syntax model:
#• The end of a line terminates the statement on that line (without semicolons).
#• Nested statements are blocked and associated by their physical indentation
#(without braces).

#Although statements normally appear one per line, it is possible to squeeze more than
#one statement onto a single line in Python by separating them with semicolons:
a = 1; b = 2; print(a + b) # Three statements on one line
#This is the only place in Python where semicolons are required: as statement separators

x = 4
y = 2

#Multi line is possible with parenthesis
X = (9 + 4 +
    2 + 3)


if x > y:
    x = 7
elif y > x:
    y = 0
else:
    x = 1
    y = 1

print(x)
print(y)

if x == 4:
    if y == 2:
        print('first')
else:
    print('second')