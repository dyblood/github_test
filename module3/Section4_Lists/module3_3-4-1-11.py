#swap var values

var1 = 1
var2 = 2
print(var1, var2, sep=", ")

var1, var2 = var2, var1 #swaps variable values
print(var1, var2, sep=", ")

#-----------------------------------------------------------------------------
#applying this principle to reverse the order of a list

my_list = [10, 1, 8, 3, 5]
length = len(my_list)
print("List originally: ", my_list) 

for i in range(length // 2):
    print(i, sep="", end=", ") #just to show what i is doing while going through loop
    print(length-i-1) #just to show the index value while going through the loop
    my_list[i], my_list[length -i - 1] = my_list[length - i - 1], my_list[i]

print("List in reverse order:", my_list)