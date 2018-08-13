#every Python tool that scans an object from left to right uses the iteration protocol.

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]

print(squares)

#written another way using list comprehension

squares = []
for x in [1, 2, 3, 4, 5]: # This is what a list comprehension does
 squares.append(x ** 2)

print(squares)

#using comprehension is faster in program more optimized

