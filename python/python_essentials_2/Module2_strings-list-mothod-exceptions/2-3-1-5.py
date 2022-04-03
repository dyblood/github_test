# 2.3.1.5 - isalnum() method

#isalnum() method (parameterless):
    #checks if the string contains only digits or alphabetical charcters(letters), and returns True or False
##NOTE: any string element that is not a digit or a letter causes the method to return False (including an empty string)

# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum()) #empty string so it returns False

print("-------")

t = 'Six lambdas' #space is not a digit or letter so it returns False
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())


