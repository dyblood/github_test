# Parameterizerd Functions

#parameter is a variable, but there 
#are two important factors that make parameters different and special:
    #1.parameters exist only inside functions in which they have been defined
        #can only be defined in () for def statement => def my_function(parameter):
    #2.assigning a value to the parameter is done at the time of the function's invocation
        #by specifying the corresponding argument
    
#parameters live inside functions
#arguments exist outside functions

def message(number):
    print("Enter a number:", number)#value is assigned at function's invocation

message(int(input()))
message(3)