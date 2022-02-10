---
aliases: []
Tags: []
---
``````ad-success
title: # #h/lime ==Android 2==
#h/lime ==date: 2022-02-01==
#h/lime ==time: 15:25==
----
Status:
Key concepts:
answ:
```python
from cffi import FFI
ffi = FFI()
ffi.set_source("_Android_3", """
unsigned int sub_deadbeef(unsigned int param1, unsigned int param2)
{
 return param1 >> (-param2 & 7) | param1 << (param2 & 0xff) & 0xff;
}

unsigned char sub_100500(unsigned char param1)
{
 return ~param1;
}

  

unsigned int sub_31337(unsigned int param1, unsigned int param2)
{
 return param1 ^ param2;
}

  

unsigned int sub_c0ffee(unsigned int param1, unsigned int param2)
{
 return sub_deadbeef(param1, 8 - param2);
}

""")
ffi.cdef("""unsigned int sub_deadbeef(unsigned int, unsigned int);""")
ffi.cdef("""unsigned char sub_100500(unsigned char);""")
ffi.cdef("""unsigned int sub_31337(unsigned int, unsigned int);""")
ffi.cdef("""unsigned int sub_c0ffee(unsigned int, unsigned int);""")
ffi.compile()
```
```python
from _Android_3 import lib
#replaced with _Android_3

'''
def ROL(data, shift, size=32):
 shift %= size
 remains = data >> (size - shift)
 body = (data << shift) - (remains << size )
 return (body + remains)

def ROR(data, shift, size=32):
 shift %= size
 body = data >> shift
 remains = (data << (size - shift)) - (body << size)
 return (body + remains)

def sub_deadbeef(x, y):
 # ROR OR ROL AND
 return ROR(x, (-y & 0x7)) |  ROL(x, y & 0xff) & 0xff
  

def sub_31337(x, y):
 return x ^ y
 ...

'''

  

'''

def sub_100500(x):
 print("0b"+bin(x)[2:].rjust(32,'0'))
 res =  x ^ int("0b"+"1"*len(bin(x)[2:]), 2)
 res = "0b" + bin(res)[2:].rjust(32,'1')
 print((res))
 return res

  

sub_100500(34) 

''' 

'''

def sub_c0ffee(x, y):

 return lib.test(x, 8-y)

'''

  

check = [0x69, 0xa7, 0x55, 0xf3, 0x03, 0x60, 0x4f, 0xa6, 0xb5, 0x35, 0xc3, 0xe0, 0x89, 0x46]

check2 = [0xad, 0x3a, 0x12, 0x90, 0x19, 0x99]


  
  

'''

print(lib.sub_deadbeef(96,4))

print(lib.sub_100500(int("010101",2)))

print(lib.sub_31337(1,2))

print(lib.sub_c0ffee(96,4))

'''

  
  

print("::STARTING::")

for x in range(14):

 temp = 0

 for y in range(256):

 temp = lib.sub_deadbeef(y, 4)

 temp = lib.sub_31337(temp, check2[x%6])

 temp  = lib.sub_100500(temp)

 temp  = lib.sub_c0ffee(temp, 7)

 if temp == check[x]:

 print(chr(y), end = '')

 break
```
flag: CTF_FLAG{native_is_pain}
---
``````

---
```ad-example
title: ## #h/white _References_
color: 200,200,200
collapse: open
```
- 
