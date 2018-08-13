import struct
#Creating a packed binary file
packed = struct.pack('>i4sh', 7, b'spam', 8)# Create packed binary data
print(packed) # 10 bytes, not objects or text


file = open('data.bin', 'wb') # Open binary output file
file.write(packed) # Write packed binary data

file.close()
#unpacking a packed binary file
data = open('data.bin', 'rb').read() # Open/read binary data file

data[4:8] # Slice bytes in the middle

print(list(data)) # A sequence of 8-bit bytes

print(struct.unpack('>i4sh', data) )