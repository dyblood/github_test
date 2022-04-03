# 2.4.1.3 - Sorting: sorted() function & sort() method

#Sorting is a sophisticated case of comparing
#Two possible ways to sort lists containing strings:

# sorted() function
    # takes a list and returns a new list
    # original list remains untouched 

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print("---------------------")
# sort() method
    # affects the list itself
    # no new list is created
    
# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)
