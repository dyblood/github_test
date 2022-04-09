# 2.5.1.10 - LAB: Find a word!

# Task is to write a program which answers the following question:
    # are the characters comprising the first string hidden inside the second string

# For example:
    #first string is "dog"
    # if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
    # if the second string is "vcxzxdcybfdstbywuefsas", the answer is no 
        # (as there are neither the letters "d", "o", or "g", in this order)

#Hints:
    # use the two-argument variants of the pos() functions inside your code
    # don't worry about case sensitivity


str1 = input("Type your first string: ").lower()
str2 = input("Type your second string: ").lower()
start = 0
found = True

for ch in str1:
    pos = str2.find(ch, start)
    if pos < 0:
        found = False
        break
    start = pos + 1

if found:
    print("Yes")
else:
    print("No")

