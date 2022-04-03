# 2.5.1.8 - LAB: Anagrams

# task - write a program which:
    # asks the user for two separate texts;
    # checks whether, the entered texts are anagrams and prints the result.

# Note:
    # assume that two empty strings are not anagrams;
    # treat upper- and lower-case letters as equal;
    # spaces are not taken into account during the check - treat them as non-existent

str1 = input("Enter 1st text to check if it is an anagram: ")
str2 = input("Enter 2nd text to check if it is an anagram: ")
test1 = [] #need to put the str into a list in order to sort
test2 = [] #need to put the str into a list in order to sort
c1 = 0
c2 = 0 

for ch in str1.lower():
    if not ch.isalpha():
        continue
    else:
        test1.append(ch)
    c1 += 1
    
for ch in str2.lower():
    if not ch.isalpha():
        continue
    else:
        test2.append(ch)
    c2 += 1

test1.sort()
test2.sort()

if c1 > 0 and c2 > 0 and test1 == test2:
    print("Anagrams")
else:
    print("Not anagrams")
