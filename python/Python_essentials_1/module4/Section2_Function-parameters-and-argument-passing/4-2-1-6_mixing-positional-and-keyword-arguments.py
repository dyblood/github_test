# Mixing Positional and Keyword Arguments

#NOTE: one unbreakable rule:
    #you have to put positional arguments before keyword arguments

#Example:
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c) 

adding(1, 2, 3) #only positional arguments

adding(c=1, a=2, b=3) #invocation with keyword variant

adding(3, c=1, b=2) #combination of keyword and positional

#NOTE: adding(3, a= 3, b = 3) - this is not allowed because a is already defined
#by the positional argument

###adding(c=1, 3, 4) #NOTE: keyword argument CAN NOT go before positional arguments
                     # The one unbreakable rule
