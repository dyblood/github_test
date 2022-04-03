#2.3.1.13 - rstrip() method

# rstrip() method:
    # two variants of the rstrip() method do nearly the same thing as lstrip
    # NOTE: affect the opposite side of the string (r => right)

# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com")) #all combinations of '.com' are stripped => why 'cisco.com' returns 'cis'
print("mississippi".rstrip("ipz")) #another example of how it strips all combinations of the argument
