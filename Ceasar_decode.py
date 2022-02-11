# with open("C:/Users/User/Downloads/total", "r") as file:
#     encode = file.read()
import string
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase


def ceasar_decode(encode):
    for i in range(len(alphabet_lower)):
        decode = ""
        for letter in encode:
            if letter.lower() in alphabet_lower:
                if letter in alphabet_lower:
                    decode += alphabet_lower[(alphabet_lower.find(letter)+1) % len(alphabet_lower)]
                if letter in alphabet_upper:
                    decode += alphabet_upper[(alphabet_upper.find(letter) + 1) % len(alphabet_upper)]
            else:
                decode += letter
        print(decode)
        encode = decode


if __name__ == "__main__":
    encode = "MablBlGhmVetllbvteVtxltkVbiaxk"
    encode = encode.upper()
    print(encode)
    ceasar_decode(encode)
