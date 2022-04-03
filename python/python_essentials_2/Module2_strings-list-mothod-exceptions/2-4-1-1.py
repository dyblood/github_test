# 2.4.1.1 Comparing Strings

# Strings can be compared using the same set of operators:
    # ==
    # !=
    # >
    # >=
    # <
    # <=
#NOTE: Python compares code point values

print("alpha" == "Alpha")
print("alpha" != "Alpha") 

print("alpha" < "alphabet") #goes by length because 'alpha' is the same as the beginning part of 'alphabet'
print("alpha" < "ALPHABET")
print("beta" > "Beta")
