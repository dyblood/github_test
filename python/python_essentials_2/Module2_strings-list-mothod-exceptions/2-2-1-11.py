#2.2.1.11 - Operations on strings: min()
# min() function => finds the minimum element of the sequence passed as an argument
  #one condition => the sequence (string, list, it doesn't matter) cannot be empty 
                #=> if empty you will get a ValueError exception

#Example 1:
print(min("aAbByYzZ")) #value is A => code point value is lower for uppercase letters (ASCII table)

#Example 2 & 3
t = 'The Knights Who say "Ni!"'
print('[' + min(t) + ']') #space value is 32 which is lower than any letter

t = [0, 1, 2]
print(min(t))
