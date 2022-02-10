---
aliases: []
Tags: []
---
``````ad-success
title: # #h/lime ==Android 1==
#h/lime ==date: 2022-02-04==
#h/lime ==time: 17:27==
----
Status:
Key concepts:
answ:
```python
#class g
class g:

 def __init__(self):

 print("Hello")

 var2 = 0

 a = [48, 59, 44, 59, 116, 41, 63, 57, 47, 40, 51, 46, 35, 116, 23, 63, 41, 41, 59, 61, 63, 30, 51, 61, 63, 41, 46]

 b = [-30, -32, -15, -52, -21, -10, -15, -28, -21, -26, -32]

 c = [65, 72, 57]

  

 var3 = a

 for var0 in range(len(a)):

 var3[var0] = (var3[var0] ^ 90)

 var0 = 0

  

 while True:

 var1 = var2

 if (var0 >= len(b)):

 while(var1 < len(c)):

 var3 = c

 var3[var1] = (var3[var1] ^ 12)

 var1+=1

 self.d = a

 self.e = b

 self.f = c

 break

  

 var3 = b

 var3[var0] ^= -123

 var0+=1

  

G = g()

  

print("d: ",''.join([chr(x) for x in G.d]))

print("e: ",''.join([chr(x) for x in G.e]))

print("f: ",''.join([chr(x) for x in G.f]))
d:  java.security.MessageDigest
e:  getInstance
f:  MD5
```


```python
import string

import g

  

G = g.g()

  

print(G.d)

print(G.e)

print(G.f)

  
  

print("g ended")

 # "6253e1406b64bbe6ba7b00ac0bf81257" cocacola

 # "96a3be3cf272e017046d1b2674a52bd3"

res = "fe546279a62683de8ca334b673420696"

res  = [int(res[i:i+2],16) for i in range(0, len(res), 2)]

values = [100, -1, 127, -57, -59, 62, 56, 8, 46, -40, -52, -10, -104, -74, 12, -63]

  

print(res)

print(values)

  

key = [(res[x]+values[x])%256 for x in range(16)]

print(key)

key = ''.join([hex(x)[2:].rjust(2,'0') for x in key])

print(key)
```
flag: CTF_FLAG{cocacola}
---
``````

---
```ad-example
title: ## #h/white _References_
color: 200,200,200
collapse: open
```
- 
