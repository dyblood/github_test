# 2.3.1.15 - startswith() & strip() methods

# startswith() method:
    # opposite of endswith() method (2.3.1.3)
    # checks if given string starts with the specified substring
        # returns True or False

# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))

print("---------------")

# strip() method
    # combines the effects caused by rstrip() & lstrip()
    # makes a new string lacking all the leading and trailing whitespaces

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")

