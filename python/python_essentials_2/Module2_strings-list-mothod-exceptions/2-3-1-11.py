# 2.3.1.11 - replace() method

#two-parameter replace() method:
    # returns a copy of the original string in which all occurrences of the first
    # argument have been replaced by the second argument

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# three-parameter replace() variant:
    #third argument limits the number of replacements

print("This is it!".replace("is", "are", 1)) 
print("This is it!".replace(" is ", " are ", 1)) #this statement will only replace the word 'is' because the whitespace is included
print("This is it!".replace("is", "are", 2))
