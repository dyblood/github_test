#How the function interacts with its arguments

#changing the parameter value doesn't propagate outside the function
def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)

print("------------------------------------------------------")
#---------------------------------------------------------------------

def my_function(my_list_1): 
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1] #creates a new variable my_list_1
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

print("-----------------------------------------------------")

#------------------------------------------------------------------
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] #doens't change the parameter my_list_1 // it modifies the list identified by it.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)