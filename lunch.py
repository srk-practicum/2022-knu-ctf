import base64
encode = "cGFzczogZ0hrNHRFM2RXcg=="
print(len(encode))
encode = encode  # b"gHk4tE3dWr"
decode = base64.b64decode(encode)
print(decode)

