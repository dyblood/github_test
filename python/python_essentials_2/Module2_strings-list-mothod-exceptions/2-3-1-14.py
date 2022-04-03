# 2.3.1.14 - split() method

# split() method:
    #splits the string and builds a list of all detected substrings
    #NOTE: method assumes that the substrings are delimited by whitespaces
        #delimiter (default whitespaces) => not coppied into the resulting list

# Demonstrating the split() method:
print("phi       chi\npsi".split()) # '\n' is considered a whitespace

print("phi;chi;psi".split(";")) # argument changes delimiter to ';'
print("phi ; chi ; psi".split(";")) #NOTE how spaces are carried into the elements values
print("phi ; chi ; psi".split(" ; "))