# Parametrized Functions 2

def message(number):
    print("Enter a number:", number)

##this situation activates a mechanism called *shadowing*##
number = 1234 #variable named number
message(1)#uses parameter not variable
print(number) #uses variable not parameter

#------------------------------------------------------------------