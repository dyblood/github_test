#2.2.1.14 - Operations on strings: the list() function

#list() function
    #takes its argument and creates a new list containing all the string's characters, one per list element
    #NOTE: not strictly a string function - list() is able to create a new list from many other entities (e.g. tuples and dictionaries)

#Example list() function:
print(list("abcabc"))

#Example count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))