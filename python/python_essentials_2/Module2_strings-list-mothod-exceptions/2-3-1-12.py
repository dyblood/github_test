#2.3.1.12 - rfind() method

#three-parameter method rfind():
    # does nearly the same thing as find, however;
    # rfind() starts the search from the end of the string (r => right)
    # 2nd argument => index to start the search
    # 3rd argument => index to end search
  ## Finds the last occurance of the string 
# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 0, 10))