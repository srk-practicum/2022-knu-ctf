with open("C:/Users/User/Downloads/code.txt", "r") as file:
    encode = file.read()
print(len(encode), encode)
encode = encode.replace("0", " ")
encode = encode.replace("1", "*")
counter = 0
for let in encode:
    counter += 1
    print(let, end="  ")
    if counter % 5 == 0:
        print("", end="")
    if counter % 25 == 0:
        print("")
