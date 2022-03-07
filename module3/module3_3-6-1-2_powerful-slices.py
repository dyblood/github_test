#Powerful Slices
#[:] is a slice which copies the elements in the list
## not the array name
#one of the most general forms is my_list[start:end]
#note not to end but end-1
#or you can specify which elements you want to copy my_list[1:3]

# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[0:len(my_list)] #len(my_list) = 5 (shows start:end-1)
print(new_list)

new_list2 = my_list[0:] #more compact way of doing [0:len(my_list)]
print(new_list2)
#------------------------------------------------------------------------------------------
# start = index of the first element included in the slice
#end is the index of the first element not included in the slice

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)