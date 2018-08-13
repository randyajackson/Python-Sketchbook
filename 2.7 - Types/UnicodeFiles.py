S = 'sp\xc4m' # Non-ASCII Unicode text

print(S)

print(S[2]) # Sequence of characters

file = open('unidata.txt', 'w', encoding='utf-8') # Write/encode UTF-8 text

file.write(S) # 4 characters written

file.close()

text = open('unidata.txt', encoding='utf-8').read() # Read/decode UTF-8 text

print(text)

print(len(text))

raw = open('unidata.txt', 'rb').read()

print(raw)

print(raw.decode('utf-8')) #how to decode utf-8

text = 'sp\xc4m'

print(text.encode('utf-8')) #manual encode to bytes

