#input is collected as a string
while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    print(reply.upper())

#changing from string to int so math.pow works
while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    print(int(reply) ** 2)
print('Bye') #this line works here because it is indented along with while

# checks if input is a digit
while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('no' * 8)
    else:
        print(int(reply) ** 2)

#checks if input is a digit but uses try catch
while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    try:
        num = int(reply) #checks if number is present, if not it prints bad
    except:
        print('bad' * 8)
    else:
        print(num ** 2)

