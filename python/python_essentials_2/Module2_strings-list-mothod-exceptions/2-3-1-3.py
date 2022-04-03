# 2.3.1.3 endswith() method

# endswith() method:
    # checks if the given string ends with the specified argument and returns True or False
    # NOTE: substring must adhere to the string's last character 
        # cannot be located somewhere near the end of the string.

#example:
if "epsilon".endswith("on"):
    print("Yes")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

