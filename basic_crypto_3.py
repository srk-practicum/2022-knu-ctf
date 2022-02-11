import base64

with open("C:/Users/User/Downloads/1-text.txt", "r") as f:
    encode = f.read()
p = encode
print(encode)
b64encode = encode[:-7]
print(len(b64encode))
print(base64.b64decode(b64encode))

# шифр подскановки далее
