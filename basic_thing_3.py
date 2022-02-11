numbs = '82 64 112 85 95 89 114 103 103 114 69 95 85 64 70 95 48 74 97 95 65 104 122 79 51 69'
numbs = numbs.split()
print(numbs)
text = ""
for n in numbs:
    text += chr(int(n))
print(text)

from Ceasar_decode import ceasar_decode

ceasar_decode(text)
