class Person:

    def __init__(self, name, job='none', pay=0): # Constructor takes three arguments
        self.name = name # Fill out fields when created
        self.job = job # self is the new instance object
        self.pay = pay

    def lastName(self): # Behavior methods
        return self.name.split()[-1] # self is implied subject

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent)) # Must change here only

    def __repr__(self):  # Added method
        return '[Person: %s, %s]' % (self.name, self.pay)  # String to print

class Manager(Person):
    def __init__(self, name, pay):  # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)  # Run original with 'mgr'

    def giveRaise(self, percent, bonus=.10):  # Redefine to customize
        Person.giveRaise(self, percent + bonus)  # Good: augment original
        #since it calls the giveRaise from Person, change in one place

if __name__ == '__main__':  # When run for testing only
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    sue.giveRaise(.10)  # Give this object a raise
    print(bob)
    print(sue)
    tom = Manager('Tom Jones', 50000)  # Job name not needed:
    tom.giveRaise(.10)  # Runs custom version
    print(tom.lastName())  # Runs inherited method
    print(tom)  # Runs inherited __repr__

    print('--All three--')
    for obj in (bob, sue, tom):  # Process objects generically
        obj.giveRaise(.10)  # Run this object's giveRaise
        print(obj)  # Run the common __repr__