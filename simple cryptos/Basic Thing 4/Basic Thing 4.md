---
aliases: []
Tags: []
---
``````ad-success
title: # #h/lime ==Basic Thing 4==
#h/lime ==date: 2022-01-28==
#h/lime ==time: 10:17==
----
Status:
Key concepts:
answ: 

```python
In [1]: HEN = b'mFhMh^oUU\APAVWMe|Ae}MzznfS'

In [2]: EGG = b'2e12'

In [10]: test = b'CTF_FLAG{'

In [11]: xor(test,EGG)
Out[11]: b'q1wmt)puI'

In [12]: xor(test,HEN)
Out[12]: b'.\x12.\x12.\x12.\x12.\x1f\x15\x16\x1e\x10\x1b\x0c"\x07\x021;\x12<6/!('

In [15]: xor(b'm',b'\x2e')
Out[15]: b'C'

In [17]: xor(b'F',b'\x12')
Out[17]: b'T'

In [28]: for i, item in enumerate(HEN):
    ...:     res = b''
    ...:     if i % 2 == 0:
    ...:         res += xor(b'\x2e', item)
    ...:     if i % 2 == 1:
    ...:         res += xor(b'\x12', item)
    ...:     print(res)
```

flag: CTF_FLAG{NoBoDy_KnowS_Th@t}
---
``````

---
```ad-example
title: ## #h/white _References_
color: 200,200,200
collapse: open
```

