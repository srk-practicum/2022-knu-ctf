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