#4.6.1.1 Sequence types and mutability

# sequence types
    #sequence type is a type of data in Python which is able to store more than one value
    #(or less than one, as a sequence may be empty), and these values can be sequentially browsed, element by element.
    #a sequence is data which can be scanned by the for loop
    #A list is a classic example of a Python sequence
#mutability
    #property of any of Python's data that dexribes its readiness to be freely changed during program execution
    #Two kinds of python data:
        #mutable and immutable
            #mutable data can be freely updated at any time (we call such an operation in situ)
            #immutable data cannot be modified in this way
#Tuple
    #tuple is an immutable sequence type
    #can behave like a list, but it mustn't be modified in situ
    #NOTE: tuples prefer to use parenthesis vs. lists like to see brackets
    #possible to create a tuple just from a set of values separated by commas
    #example:

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

#NOTE: each tuple element may be of a different type 
#(floating-point, integer, or any other not-as-yet introduced kind of data)

empty_tuple = ()

one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
