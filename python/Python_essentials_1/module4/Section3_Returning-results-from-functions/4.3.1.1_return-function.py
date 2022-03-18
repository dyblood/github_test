#return instruction

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return #causes immidiate termination of function. 
               #instant return to the point of invocation

    print("Happy New Year!")

happy_new_year()

#-------------------------------------------------------
#return with an expression
#1. immediate termination of the function's execution (same as with no expression)
#2. evaluate's the expression's value and will return it as the function's result

def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)
