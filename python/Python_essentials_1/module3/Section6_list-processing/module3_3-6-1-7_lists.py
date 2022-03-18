#--------------------------------------------------------------------------------
#two ways to find which number is the biggest number

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#second way to find largest number using slicing

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)
#-------------------------------------------------------------
#find the location of a given element inside a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5 # target value
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find #changes value of found to true if my_list[i] == target value
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

### find how many values of one list are in another list

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets: # copies the element to number
    if number in drawn: #compares number to drawn list
        hits += 1 #if a number from bets list matches a element in the drawn list add 1

print(hits)