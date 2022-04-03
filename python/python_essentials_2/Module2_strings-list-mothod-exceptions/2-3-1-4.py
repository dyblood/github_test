# 2.3.1.4 - find() method

# find() method:
    # similar to index()
    #looks for a substring and returns the index of the first occurence of this substring but:
        #It's safer => doesn't print an error for an argument containing a non-existent substring
            #(returns -1 if substring is not there)
        # It works with STRINGS only
    
#Example:
print("Eta".find("ta"))
print("Eta".find("mma"))

print("--------")

###NOTE: don't use find() if you only want to check if a single character occurs within a string.
    # the in operator will be significantly faster.

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print("--------")

print('kappa'.find('a', 2)) #second argument ('2') specifies the index where the search will be started

print("--------")

# Using the find() method to search for all substring's occurrences:

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1) # e/ time an index is found it changes the second argument to start +1 of that index to find the next index

print("--------")

# find() method using three parameters
    #third argument points to the first index which won't be taken into consideration (upper limit of the search)

print('kappa'.find('a', 1, 4)) #start at index 1, don't take index 4 into consideration
print('kappa'.find('a', 2, 4))



