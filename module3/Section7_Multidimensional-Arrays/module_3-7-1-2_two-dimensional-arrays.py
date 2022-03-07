#two-dimensional arrays

#assume that a predifined symbol named "EMPTY" designates an empty field on the chessboard

#create a list of lists representing the whole chessboard:

board = []
## This makes board into a two-dimensional array
for i in range(8):#creates 8 lists => each list consists of another list containing 8 elements
    row = ["EMPTY" for i in range(8)] #creates a list consisting of 8 empty predifined symbols
    board.append(row)


# for i in range(len(board)):
    # print(board[i])

#### two-dimensional array's can also be shortend 
#### because list comprehensions can be nested

board = [["EMPTY" for i in range(8)] for j in range(8)] #inner part creates a row [for i in range(8)]
                                                        #outer part builds a list of rows [[] for j in range(8)]
# for i in range(len(board)):
    # print(board[i])


#-----------------------------------------------------------------------
#two-dimensional arrays coninued 

EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

# print(board)

##-------------------------------------------------------------------------
EMPTY = "-"
ROOK = "ROOK"


board = [[EMPTY for i in range(8)] for j in range(8)] #makes two-dimentional array (i = columns)(j = rows)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

for i in range(len(board)):
    print(board[i])
