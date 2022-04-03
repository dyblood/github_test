#2.3.1.2 - center() method

#center() method
    #one-parameter variant of the center() method makes a copy of the original string, 
    # trying to center it inside a field of a specified width
    #centering is done by adding some spaces before and after the string

#Example of center() method
print('[' + 'alpha'.center(10) + ']')

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4, '*') + ']') #note the width is not longer than the word so nothing changes 
print('[' + 'Beta'.center(6) + ']')

print('[' + 'gamma'.center(20, '*') + ']') #uses '*' to center instead of spaces

print("+" + "Gamma".center(78, '-') + "+")
print(("|" + "".center(78) + "|\n") * 7, end="")
print("|" + "Am I centered?".center(78) + "|")
print(("|" + "".center(78) + "|\n") * 7, end="")
print("+" + "".center(78, '-') + "+")