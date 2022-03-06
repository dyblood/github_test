my_list = [10, 1, 8, 3, 5]
total = 0

# using range(len(my_list)) gets the length of the list to use for i
# i would be 0,1,2,3,4 (i becomes the index value)
for i in range(len(my_list)):
    print(i, ", ", sep="", end="")
    total += my_list[i]
print()
print(total)

#-----------------------------------------------------------------------
my_list2 = [10, 1, 8, 3, 5]
total = 0

#using i in my_list2 turns i into the element (not the index)
for i in my_list2:
    print(i,", ",sep="", end="")
    total += i
print()
print(total)