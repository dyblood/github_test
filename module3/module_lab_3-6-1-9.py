##write a program that removes all the number repititions

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)
my_list = new_list[0:]
    
print("The list with unique elements only:")
print(my_list)