# 2.5.1.1 - Caesar Cipher: Encrypting a Message

#adds + 1 to the code point vale of capital letters only EXCEPT Z
    # 'Z' is changed to 'A'

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
