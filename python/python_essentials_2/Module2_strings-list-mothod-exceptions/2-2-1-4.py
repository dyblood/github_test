#2.2.1.4 - operations on strings: ord()
# If you want a specific character's ASCII/UNICODE code point value:
    #you can use a function named ord()
    #function needs a one-character string as its argument
        #breaching this requirement causes TypeError

#example of ord() function

char_1 = 'α'
char_2 = 'ę' 

print(ord(char_1))
print(ord(char_2))
