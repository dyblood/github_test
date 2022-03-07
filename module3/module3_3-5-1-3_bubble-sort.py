#bubble sort (Finale Interactive Version)

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
#---------------------------------------------------------------------------------------------------------
#Python also has a sorting mechanism
#Sorts a list much faster

my_list = [8, 10, 6, 2, 4]
my_list.sort() #sorts items from lowest to highest
print(my_list)

#another sorting method in python is reverse()

my_list.reverse() #sorts items in reverse (highest to lowest)
print(my_list)
