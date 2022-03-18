my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1) #adding 1 so the list does not start at zero

print(my_list)

##
my_list2 = []

for i in range(5):
    my_list2.insert(0, i + 1) #adds element to the begining of the list each time
#                             #sorts the list in the opposite order
print(my_list2)

##
my_list3 = []

for i in range(5):
    my_list3.insert(-1, i+1)

print(my_list3)