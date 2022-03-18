#----------------------------------------------------------------------------
#Functions and scopes

def my_function():
    print("Do I know that variable?", var)

#variable created outside a function has a scope inside the functions' body
var = 1
my_function()
print(var)
print("----------------------------")
#---------------------------------------------------------------------------
#var created inside the function is not the same as when defined outside it
#function varibale shadows the variable coming from the outside world.

def my_function():
    var=2
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)


#NOTE: A variable existing outside a function has a scope inside the functions' bodies, 
# excluding those of them which define a variable of the same name.
print("-------------------------")
#---------------------------------------------------------------------------------
#global keyword

#Special python method which can extend a variable's scope in a way which includes the functions' bodies.
#(if you want the function to read the value, but also modify it)

def my_function():
    global var #using global w/ variable name or multiple variables 
               #forces python not to create a new variable with those names inside the function
    var = 2
    print("Do I know the variable?", var)

var = 1
my_function()
print(var)