numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)

numbers[0] = 111
print("\nNew list content: ", numbers)

numbers[1] = numbers[4]
print("\nNew list content:", numbers, "\n")

print(numbers[0], "\n")

print("The length of the lis is:", len(numbers)) #print the length of the list

del numbers[1] #deletes list element with index of 1
print("The length of the new list is:", len(numbers)) #prints the new list length
print("The list now consist of: ", numbers)

# Negative indices are legal

print("The last item on the list is: ", numbers[-1]) #lists the last element on the list (same as numbers[3])
print("The second to last item on the list is: ", numbers[-2]) #prints the second to last element on the list


