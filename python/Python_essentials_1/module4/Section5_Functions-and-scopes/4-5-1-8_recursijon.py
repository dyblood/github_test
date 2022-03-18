#4.5.1.8 recursion
#recusion in reference to computer programming:
    #recursion is a technique where a function invokes itself.
        #when a function calls itself, this situation is known as recursion,
        #and the function which calls itself and contains a specified termination condition is called a recursive function

#recursive functions write cleaner, more elegant code, and divide it into smaller, organized chunks
#NOTE: easy to make a mistake and create a function which never terminates
#NOTE: recursive calls consume a lot of memory and may sometimes be inefficient

#---------------------------------------------------------------------
#shorter way to write the fib() function

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    return fib(n-1) + fib(n-2) #recalling what fib(n-1) and fib(n-2) were equal to and adding them together
    #example if n = 8:
        # fib(8-1) + fib(n-2) = 13 + 8
#-------------------------------------------------------------------
#shorter way to write the factoral function
def factorial_function(n):
    #without the two if statements there is no termination to the recursion
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1) #recalling what factorial_function(n-1) was equal to and multiplying it by n
#-------------------------------------------------------------------
for n in range(1, 10):
    print(n, "->", fib(n))

for n in range(1, 6):  # testing
    print(n, factorial_function(n))
print(factorial_function(4))