hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.

number = int(input("Enter a number any number: "))
hat_list[-3] = number #replaces the middle element with the number the user chose
del hat_list[-1] #deletes the last element of the list
print("The list length is now:",len(hat_list))

print(hat_list)