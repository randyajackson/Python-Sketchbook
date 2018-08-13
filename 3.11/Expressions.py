#Operation Interpretation
#spam(eggs, ham) Function calls
#spam.ham(eggs) Method calls
#spam Printing variables in the interactive interpreter
#print(a, b, c, sep='') Printing operations in Python 3.X
#yield x ** 2 Yielding expression statements

L = [1, 2]
L.append(3) # Append is an in-place change
print(L)

L = L.append(4) # But append returns None, not L
print(L) # So we lose our list!