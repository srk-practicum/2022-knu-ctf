---
aliases: []
Tags: []
---
``````ad-success
title: # #h/lime ==RE 1==
#h/lime ==date: 2022-02-05==
#h/lime ==time: 14:50==
----
Status:
Key concepts:
answ: 

the idea was to find two strings: one containing resulting values of the opereation over the input data, and the other containing info which function should be used on the byte at a stecific index

knowing that two strings, and the exact length (`0x17`) of the input strnig we can easily recreate the flag

![[Pasted image 20220205150312.png]]
# length ![[Pasted image 20220205150604.png]]

# commands
![[Pasted image 20220205150340.png]]
# resulting value
![[Pasted image 20220205150646.png]]


```python
#!/usr/bin/env python3
import string
from pwn import *
print("Starting to work!")

def int_to_bytes(INT):
    return INT.to_bytes((INT.bit_length() + 7) // 8, byteorder='big')


#https://www.aldeid.com/wiki/Category:Encryption/rol-ror
# Rotate left. Set max_bits to 8.
rol = lambda val, r_bits, max_bits=8: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right. Set max_bits to 8.
ror = lambda val, r_bits, max_bits=8: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))    

'''
EBX  0x804a049 (vmp) ◂— add    eax, dword ptr [esi] /* 0x3040603 */
ECX  0x804a077 (inp) ◂— xor    al, 0x35 /* 0xa3534; '45\n' */
EDI  0x804a060 (vmr) ◂— or     eax, 0xfd3aeb99 /* 0x3aeb990d */
ESI  0x804a077 (inp) ◂— xor    al, 0x35 /* 0xa3534; '45\n' */
'''

length = 0x17

#resulting value
edi = "0d 99 eb 3a fd 5f 76 3b 98 63 3a 19 2c 8d cb d9 08 cf 0d a4 02 a2 c0 61 0a 00 00 00 00 00 00 00"

#commands
ebx = "03 06 04 03 01 02 07 06 06 07 06 02 02 04 00 00 04 00 04 07 02 07 01 0d 99 eb 3a fd 5f 76 3b 98"

edi  = [int("0x"+x, 16) for x in edi.split(' ')][:0x17]
ebx  = [int("0x"+x, 16) for x in ebx.split(' ')][:0x17]


print(ebp)
print(edi)
print(ebx)



print(hex(len(ebp)))

for i, x in enumerate(ebx):
    if x == 1: print(i, x)

print()
for x in range(0,0x17):
    for i in range(256):
        #3
        if (i ^ 0x7a) & 0xff == edi[x] and (x == 0 or x == 3): #edi
            print(chr(i), end = "")
            break

        #6
        if (rol(i, 7)) & 0xff == edi[x] and (x == 1 or x == 7 or x == 8 or x == 10): #edi
            print(chr(i), end = "")
            break

        #4
        if (rol(i, 5)) & 0xff == edi[x] and (x == 2 or x == 13 or x == 16 or x == 18): #edi
            print(chr(i), end = "")
            break

        #1
        if (i-0x75) & 0xff == edi[x] and (x == 4 or x == 22): #edi
            print(chr(i), end = "")
            break

        #2
        if (i ^ 0x6c) & 0xff == edi[x] and (x == 5 or x == 11 or x == 12 or x == 20): #edi
            print(chr(i), end = "")
            break

        #0
        if  (i + 0x6c) & 0xff == edi[x] and(x == 14 or x == 15 or x == 17): #edi
            print(chr(i), end = "")
            break

        #7
        if ~(i + 0x2a) & 0xff == edi[x] and (x == 6 or x == 9 or x == 19 or x == 21): #edi
            print(chr(i), end = "")
            break



```

flag: CTF_FLAG{w3_@r3_v1rtu@l_m@ch1n35}
---
``````

---
```ad-example
title: ## #h/white _References_
color: 200,200,200
collapse: open
```
- 
