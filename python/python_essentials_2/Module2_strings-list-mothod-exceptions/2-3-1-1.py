# 2.3.1.1 - capitalize() method
#capitalize() method:
    #creates a new string filled with characters taken from the source string
    #tries to modify in the following way:
        #if the first character inside string is a letter => 
            #character is an element with an index = 0
            #NOTE: not just the first visible character
        #all remaining letters from the string will be converted to lower-case

#example:
print('aBcD'.capitalize())

#NOTE don't forget that:
    #the original string is not changed in any way
    #the modified string is returned as a result

#Example 2:

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

