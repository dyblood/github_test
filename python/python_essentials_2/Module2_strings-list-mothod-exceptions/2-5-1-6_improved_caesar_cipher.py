# 2.5.1.6 - Improved Caesar Cipher

# Original Caesar cipher transforms letters 1 letter to the right based on code point
# Improving the Ceasar cipher to allow the shifted value to come from the range 1..25 inclusive

# Also, let the code preserve the letters' case (lower-case letters will remain lower-case) 
# All non-alphabetical characters should remain untouched

# Task - to write a program which:
    # asks the user for one line of text to encrypt;
    # asks the user for a shift value 
        # (an integer number from the range 1..25)
        # NOTE: you should force the user to enter a valid shift value
    #prints out the encoded text

user_str = input("Enter a string you want to be encrypted: ")
shift_value = int(input("Enter a shift value from 1 - 25: "))
cipher = ""

for ch in user_str:
    if not ch.isalpha():
        cipher += ch
    code = ord(ch) + shift_value
    if ch.isupper():
        if code > ord('Z'):
            code = code - ord('Z') + 64
            cipher += chr(code)
        else:
            cipher += chr(code)
    if ch.islower():
        if code > ord('z'):
            code = code - ord('z') + 96
            cipher += chr(code)
        else:
            cipher += chr(code)

print(cipher)
