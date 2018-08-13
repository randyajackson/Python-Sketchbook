#The standard output stream (often known as stdout) is simply a default place to
#send a program’s text output.

print() # Display a blank line
x = 'spam'
y = 99
z = ['eggs']
print(x,y,z)

#By default, print calls add a space between the objects printed. To suppress
#this, send an empty string to the sep keyword argument, or send an alternative separator
#of your choosing:

print(x, y, z, sep='')
print(x, y, z, sep=', ')

print(x, y, z, '*** no line break ***', end='') # Suppress line break
print(x, y, z, end=''); print(x, y, z) # Two prints, same output line
print(x, y, z, end='...\n') # Custom line end

print(x, y, z, sep='...', end='!\n') # Multiple keywords

print(x, y, z, sep='...', file=open('data.txt', 'w'))
print(open('data.txt').read())

text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
print(text)

#print >> afile, x, y       2.X way of printing doesnt work here

import sys

temp = sys.stdout # Save for restoring later

sys.stdout = open('log.txt', 'w') # Redirects prints to a file

print(x, y, x) # Shows up in log.txt


print('spam') # Prints go to file, not here
print(1, 2, 3)
sys.stdout.close() # Flush output to disk
sys.stdout = temp # Restore original stream
print('back here') # Prints show up here again

print(open('log.txt').read()) # Result of earlier prints

#In 3.X, the file keyword allows a single print call to send its text to the write method
#of a file (or file-like object), without actually resetting sys.stdout.

log = open('log.txt', 'w') # 3.X
print(x, y, z, 'IN LOG.TXT', file=log) # Print to a file-like object
log.close()                                                         #needs to close before opening
print(open('log.txt').read()) # Result of earlier prints

print(1, 2, 3) # Print to original stdout
