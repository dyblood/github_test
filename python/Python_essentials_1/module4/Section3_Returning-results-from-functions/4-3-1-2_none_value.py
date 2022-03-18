#none value
#Two circumstances when None can be safely used:
    #1. when you assign it to a variable (or return it as a function's result)
    #2. when you compare it with a variable to diagnose its internal state

#Example:

value = None
if value is None:
    print("Sorry, you don't carry any value")

#NOTE: if a function doesn't return a certain value using a return expression clause,
# it assumed that it implicitly returns None.

def strange_function(n):
    if(n%2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))
