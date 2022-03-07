#for a normall var this would print out 1
#Lists are stored in different ways than ordinary (scalar) variables

###name of an ordinary variable is the name of the content
###****name of list is the name of a memory location where the list is stored***###

list_1 = [1]
list_2 = list_1 #Copies the name of the array not the contents!!!!
#####modifying one of them affects the other, and vice versa#####
list_1[0] = 2
print(list_2)
list_2.append(4)
print(list_1)