while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    elif not reply.isdigit():
        print('bad' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print('high')
print('Bye')
