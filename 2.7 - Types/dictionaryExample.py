D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

print(D['food'])
print(D['quantity'])
print(D['color'])

D = {}
D['name'] = 'Bob' # Create keys by assignment
D['job'] = 'dev'
D['age'] = 40

print(D)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])) # Zipping
print(bob2)  #dict is another way of doing above

rec = {'name': {'first': 'Bob', 'last': 'Smith'}, #nested example
       'jobs': ['dev', 'mgr'],
       'age': 40.5}

rec['jobs'].append('helpdesk')
print(rec['name'])
print(rec['name']['last'])

print(rec['jobs'])

if not 'salary' in rec:   # checks if key salary is in rec
       print('missing')
       print('no really') # if continues with indention

#sorting keys using for loops _____________________________

Ks = list(rec.keys()) # Unordered keys list

Ks.sort() # Sorted keys list

for key in Ks: # Iterate though sorted keys
 print(key, '=>', rec[key])

rec = 0 #cleans up space

print(rec)

for c in 'SPAM':
    print(c.lower())

x = 4

while x > 0:
    print('string ' * x)
    x-=1

