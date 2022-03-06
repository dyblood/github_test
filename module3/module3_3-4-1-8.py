numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###--------------------------------------------------------------------------------------
#append() method add an element to the end of the list

numbers.append(4) #adds the element 4 to the end of the list
print(len(numbers))
print(numbers)

###--------------------------------------------------------------------------------------
#insert() method can add a new element at any place in the list

numbers.insert(0, 222) #inserts the element at index [0] (the begining of the list)
print(len(numbers))
print(numbers)

###--------------------------------------------------------------------------------------

numbers.insert(1, 333) #inserts element to index[1] (the second item in the list)
print(len(numbers))
print(numbers)

