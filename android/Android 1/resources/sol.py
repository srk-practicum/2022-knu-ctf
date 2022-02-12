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
res  = [int(res[i:i+2],16) for i in range(0, len(res), 2)]
values = [100, -1, 127, -57, -59, 62, 56, 8, 46, -40, -52, -10, -104, -74, 12, -63]

print(res)
print(values)

key = [(res[x]+values[x])%256 for x in range(16)]
print(key)
key = ''.join([hex(x)[2:].rjust(2,'0') for x in key])
print(key)
