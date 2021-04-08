#!/usr/bin/python
import binascii
from random import choice
from pwn import *
import tqdm

class Cipher:
    BLOCK_SIZE = 16
    ROUNDS = 3
    def __init__(self, k1, k2):
        self.k1 = binascii.unhexlify(k1)
        self.k2 = binascii.unhexlify(k2)

    def __block_encrypt(self, block):
        enc = int.from_bytes(block, "big")
        enc &= int.from_bytes(self.k1, "big")
        enc ^= int.from_bytes(self.k2, "big")
        return hex(enc)[2:].rjust(self.BLOCK_SIZE*2, "0")


    def __pad(self, msg):
        if len(msg) % self.BLOCK_SIZE != 0:
            return msg + (bytes([0]) * (self.BLOCK_SIZE - (len(msg) % self.BLOCK_SIZE)))
        else:
            return msg
    
    def encrypt(self, msg):
        m = self.__pad(msg)
        e = ""
        for i in range(0, len(m), self.BLOCK_SIZE):
            e += self.__block_encrypt(m[i:i+self.BLOCK_SIZE])
        return e.encode()

p = remote('crypto.2021.chall.actf.co', 21602)

p.readuntil("[2]? ")
p.sendline('1')
p.readuntil('encrypt: ')
p.sendline('00000000000000000000000000000000')

k1 = 0
k2 = str(p.readline())[2:-3]

test = int.from_bytes(binascii.unhexlify("00000000000000000000000000000001"), "big")

for i in tqdm.tqdm(range(32*4)):
    p.readuntil("[2]? ")
    p.sendline('1')
    p.readuntil('encrypt: ')
    p.sendline(hex(test)[2:].rjust(32, "0"))

    res = str(p.readline())[2:-3]

    if res != k2:
        k1 |= 1 << i
    
    test = test << 1

print(f'k1 = {hex(k1)[2:].rjust(32, "0")}')
print(f'k2 = {k2}')

k1 = hex(k1)[2:].rjust(32, "0")

# Solve challenge response
cipher = Cipher(k1, k2)
p.readuntil("[2]? ")
p.sendline('2')
for i in tqdm.tqdm(range(10)):
    p.readuntil('Encrypt this: ')
    challenge = str(p.readline())[2:-3]
    solution = cipher.encrypt(binascii.unhexlify(challenge))
    p.sendline(solution)

p.readline()
print(p.readline())
p.close()