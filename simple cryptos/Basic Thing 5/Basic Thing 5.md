---
aliases: []
Tags: []
---
``````ad-success
title: # #h/lime ==Basic Thing 5==
#h/lime ==date: 2022-01-28==
#h/lime ==time: 10:36==
----
Status:
Key concepts:
answ:
```python
In [47]: data = '%4e%7a%6b%7a%4d%7a%63%30%4e%57%59%32%4d%54%5a%6c%4d%7a%41%33%4e%44%59%34%4e%6a%55%33%4d%6a%56%6d%4e%7
    ...: a%51%32%4d%54%63%7a%4e%6d%49%3d'

In [48]: import urllib.parse

In [49]: urllib.parse.unquote(data)
Out[49]: 'NzkzMzc0NWY2MTZlMzA3NDY4NjU3MjVmNzQ2MTczNmI='

In [50]: data = urllib.parse.unquote(data)

In [51]: import base64

In [52]: base64.b64decode(data)
Out[52]: b'7933745f616e30746865725f7461736b'

In [53]: base64.b64decode(data).decode('utf-8')
Out[53]: '7933745f616e30746865725f7461736b'

In [54]: data = base64.b64decode(data).decode('utf-8')

In [61]: print("CTF_FLAG{", end = '')
    ...: for x in range(0,len(data), 2):
    ...:     print(chr(int(data[x:x+2], 16)), end = '')
    ...: print("}")
CTF_FLAG{y3t_an0ther_task}

```
flag: CTF_FLAG{y3t_an0ther_task}
---
``````

---
```ad-example
title: ## #h/white _References_
color: 200,200,200
collapse: open
```
- 
