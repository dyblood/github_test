#2.2.1.8 - the in and not in operators

# in operator - checks if its left argument (a string) can be found anywhere within the right argument (another string)
    # result => True or False

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

# not in operator does the opposite
print("----------------")
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)