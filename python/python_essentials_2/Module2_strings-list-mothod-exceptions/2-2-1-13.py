#2.2.1.13 - Operations on strings: the index() method

#index() method => searches the sequence from the beginning, in order to find the first element of the value specified in its argument
    #NOTE: the element searched for must occur in the sequence
    #NOTE: absence of value will cause a ValueError exception
#method returns the index of the first occurence of the argument

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A")) #will only get the index of the first 'A' => 1
