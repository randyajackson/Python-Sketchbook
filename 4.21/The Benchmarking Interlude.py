import timer
def timer(func, *args): # Simplistic timing function
    start = time.clock()
    for i in range(1000):
      func(*args)
      return time.clock() - start # Total elapsed time in seconds

#print(timer(pow, 2, 1000))
#print(timer(str.upper, 'spam'))

print(timer.total(1000, str.upper, 'spam') )

#timer import and functions