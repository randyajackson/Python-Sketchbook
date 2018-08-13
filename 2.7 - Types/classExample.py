class Worker:
 def __init__(self, name, pay): # Initialize when created
  self.name = name
  self.pay = pay

 def lastName(self):
  return self.name.split()[-1] # Split string on blanks

 def giveRaise(self, percent):
  self.pay *= (1.0 + percent)

bob = Worker('Bob Smith', 50000)  # Make two instances
sue = Worker('Sue Jones', 60000)  # Each has name and pay attrs
print(bob.lastName()) # Call method: bob is self

print(sue.lastName()) # sue is the self subject

sue.giveRaise(.10)  # Updates sue's pay
sue.pay

