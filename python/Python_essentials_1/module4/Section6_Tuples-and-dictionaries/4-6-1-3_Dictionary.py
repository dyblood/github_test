#4.6.1.4 Dictionary
#----------------------------------------------------------------------------------------------------
#NOTE: in Python 3.6x dictionaries became ordered by default. Earlier versions may not be in order.
#examples of dictionaries:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
words = ['cat', 'lion', 'horse']
empty_dictionary = {}
#-----------------------------------------------------------------------------------------------------
print(dictionary)
print(phone_numbers)
print(empty_dictionary)
print("----------------------------")


print(dictionary['cat'])
print(phone_numbers['Suzy']) #keys are case-sensitive 'suzy' will get an error
print("----------------------------")

for word in words: #way to get arround error if key does not exist
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
print("-----------------------------")
#---------------------------------------------------------------------------------------------------------
#**NOTE: when you write a big or lengthy expression, it may be a good idea to keep it vertically aligned.

# Example 1:
# dictionary = {
#               "cat": "chat",
#               "dog": "chien",
#               "horse": "cheval"
#               }

# # Example 2:
# phone_numbers = {'boss': 5551234567,
#                  'Suzy': 22657854310
#                  }
#---------------------------------------------------------------------------------------------------------
#NOTE: to run a dictionary through the for loop tools are needed

#keys() method
for key in dictionary.keys(): #note the keys() method
    print(key, "->", dictionary[key])
print("------------------------------")

# items() method
for english, french in dictionary.items(): #note the way in which the tuple has been used as a for loop variable
    print(english, "->", french)
print("------------------------------")

for french in dictionary.values():
    print(french)
print("------------------------------")

# sorted() function
for key in sorted(dictionary.keys()): #now the keys list will be in alphabitical order
    print(key, "->", dictionary[key])

