# 2.3.1.18 - LAB: Making a 'split()' method

# TASK: write your own function, which behaves almost exactly 
#       like the original split() method i.e.:
    # It should accept exactly one argument - a string;
    # It should return a list of words created from the string, divided in the places where the string contains whitespaces;
    # if the string is empty, the function should return an empty list;
    # its name should be mysplit()

#mysplit function only uses a space as a delimiter (" ")
def mysplit(strng):
   var = ""
   new_list = []
   for ch in strng:
       if ch.isspace() == False: 
           var += ch # if ch is not whitespace it is added to var
       elif ch.isspace() == True:
           if len(var) > 0 and var != " ": #checks if var has a length greater than 0 and is not a space
                new_list.append(var) # if there is whitespace var gets appended to new list
                var = "" # clears var
           else:
                var = ""
   return new_list



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
