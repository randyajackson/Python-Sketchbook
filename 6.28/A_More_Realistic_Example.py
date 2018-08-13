# Specifically, in this chapter we’re going to code two classes:
# • Person—a class that creates and processes information about people
# • Manager—a customization of Person that modifies inherited behavior

from person import Person, Manager

bob = Person('Bob Smith') # Test the class
sue = Person('Sue Jones', job='dev', pay=100000) # Runs __init__ automatically
tom = Manager('Tom Jones', 50000) # Job name not needed:

import shelve
db = shelve.open('persondb') # Filename where objects are stored
for obj in (bob, sue, tom): # Use object's name attr as key
    db[obj.name] = obj # Store object on shelve by key
db.close() # Close after making changes

db = shelve.open('persondb') # Reopen the shelve
len(db) # Three 'records' stored
list(db.keys()) # keys is the index
bob = db['Bob Smith'] # Fetch bob by key
bob.lastName()
for key in db: # Iterate, fetch, print
    print(key, '=>', db[key])
#bob.giveRaise(.10)
#sue.giveRaise(.10)
#print(bob) # Fetch attached attributes
#print(sue)
#tom.giveRaise(.10) # Runs custom version
#print(tom.lastName()) # Runs inherited method
#print(tom) # Runs inherited __repr__

