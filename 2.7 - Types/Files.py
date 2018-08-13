f = open('data.txt', 'w') # Make a new file in output mode ('w' is write)

f.write('Hello\n') # Write strings of characters to it

f.write('world\n') # Return number of items written in Python 3.X

f.close()

f = open('data.txt') # 'r' (read) is the default processing mode

text = f.read()

for line in open('data.txt'): print(line) # uses for loop to print lines in text file

print(text)

print(text.split())

print(dir(f))