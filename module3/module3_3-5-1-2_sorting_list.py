#Sorting list (BUBBLE SORT)
#This way of sorting a list is a slow way to sort and often not used
#Sorts the list by comparing two elements at a time
#-----------------------------------------------------------------------------------------#
#This only goes through the list one time so it may not get everything

my_list = [8, 10, 6, 2, 4] # list to sort

for i in range(len(my_list) - 1): #we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]: # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] #swap the elements 
print(my_list)
#-----------------------------------------------------------------------------------------#
#Adding a while loop will allow us to keep running 
#the for loop as long as a sort keeps occuring

my_list = [8, 10, 6, 2, 4] # list to sort
swapped = True #need it to enter the while loop

while swapped: #while true
    swapped = False # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i+1]:
            swapped = True #a swap occurred! this allows to go back through the while loop
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)