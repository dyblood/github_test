from cmath import log


#assume every row on a chessboard is a list
row = []

for i in range(8):
    row.append("WHITE_PAWN") #builds a list containing 8 elements 
                           #(representing the second row of the chessboard)
                           #assume WHITE_PAWN is a predefined symbol representing a white pawn

###-----------------------------------------------------------------------------------------####
## List Comprehension ##
## Same effect can be achieved with list comprehension

#*** List comprehension is a list, but 
#created on-the-fly during program execution and is not described statically


row = ["WHITE_PAWN" for i in range(8)]
        #data to be used to fill the list (WHITE_PAWN)
        #clause specifying how many times the data occurs inside the list (for i in range(8))

###other examples

#Example #1
squares = [x ** 2 for x in range(10)] # produces a ten-element list filled with squares of 
                                      # ten integer numbers starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

#Example #2
twos = [2 ** i for i in range(8)] # creates an eight-element array containing the first eight powers of two

#Example #3:
odds = [x for x in squares if x%2 != 0] #makes a list with only the odd elements of the squares list