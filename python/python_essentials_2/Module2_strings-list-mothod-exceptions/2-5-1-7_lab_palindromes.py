# 2.5.1.7 - LAB: Palindromes

# Task is to write a program that:
    # asks the user for some text;
    # checks whether the entered text is a palindrome, and prints result

#NOTE:
    # assume that an empty string isn't a palindrome;
    # treat upper-case and lower-case letters as equal;
    # spaces are not taken into account during the check - treat them as non-existent
    # there are more than a few correct solutions - try to find more than one

user_str = input("Please enter text that you want to test is a palindrome: ")
test_str1 = ""
test_str2 = ""
count = 0

#make user_str all lowercase letters with no spaces for testing
for ch in user_str.lower():
    if not ch.isalpha():
        continue
    else:
        test_str1 += ch
    count += 1

#make user_str all lowercase letters with no spaces for testing
for ch in user_str.lower():
    if not ch.isalpha():
        continue
    else:
        test_str2 = ch + test_str2
if count > 0:
    if test_str1 == test_str2:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
else:
    print("You did not enter anything.")

