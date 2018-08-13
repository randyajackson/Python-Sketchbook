M = [[1, 2, 3], # A 3 × 3 matrix, as nested lists
    [4, 5, 6], # Code can span lines if bracketed
    [7, 8, 9]]

print(M)

print(M[1][2])

col = [row[1] for row in M] # print column 1

print(col)

col = [row[1] + 100 for row in M] # print column 1 + 100

print(col)

col = [row[1] for row in M]

print(col)

diag = [M[i][i] for i in [0,1,2]] # prints diagonal ( 00,11,22 )

print(diag)

doubles = [c * 2 for c in 'SPAM'] # creates list of double characters in the string SPAM

print(doubles)

listTest = list(range(-6, 7, 2)) # counts from -6 to 6 by 2

print(listTest)

ranger = list(range(4))     # creates a list [0,1,2,3]
print(ranger)

print(list(range(4)))

nestedComp = [[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]

print(nestedComp)

G = (sum(row) for row in M) # Create a generator of row sums

print(next(G)) #row 1 sum
print(next(G)) #row 2 sum
print(next(G)) #row 3 sum

G = list(map(sum, M)) # does above but puts it into list

print(G)

