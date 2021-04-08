import os
import zlib

def keystream(key):
	index = 0
	while 1:
		index+=1
		if index >= len(key):
			key += zlib.crc32(key).to_bytes(4,'big')
		yield key[index]

f = open("enc","rb")
ciphertext = f.read()

for i in range(0, 2**16):
	plain = []
	k = keystream(i.to_bytes(2, 'little'))
	for i in ciphertext:
		plain.append(i ^ next(k))
	plain = bytes(plain)
	if b'actf' in plain:
		print(''.join(map(chr,plain)))
		break