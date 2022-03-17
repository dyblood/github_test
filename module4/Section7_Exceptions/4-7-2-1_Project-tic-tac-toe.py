#4.7.2.1 Tic-Tac-Toe Project

#----------------------------------------------------------------------------------------------------------#
#Instructions:
    #1.) the computer (i.e., your program) should play the game using 'X's;
    #2.) the user (e.g., you) should play the game using 'O's;
    #3.) the first move belongs to the computer − 
         # it always puts its first 'X' in the middle of the board;
    #4.) all the squares are numbered row by row starting with 1 
         # (see the example session below for reference)
    #5.) the user inputs their move by entering the number of the square they choose − 
         # the number must be valid, i.e., it must be an integer, 
         # it must be greater than 0 and less than 10, and it cannot point 
         # to a field which is already occupied;
    #6.) the program checks if the game is over − there are four possible verdicts: 
         # the game should continue, the game ends with a tie, you win, or the computer wins;
    #7.) the computer responds with its move and the check is repeated;
    #8.) don't implement any form of artificial intelligence − a random field choice made 
         # by the computer is good enough for the game.

# +-------+-------+-------+ ##board_frame_1
# |       |       |       | ##board_frame_2
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
#----------------------------------------------------------------------------------------------------------#
from random import randrange

# board_frame_1 = (("+" + 7*"-")*3 + "+") #
# board_frame_2 = (("|" + 7*" ")*3 +  "|")
# board = [["-" for column in range(3)]for row in range(3)]

# #setting the starting values of the board to 1-9
# counter = 1
# for i in range(3):
#     for j in range(3):
#         board[i][j] = counter 
#         counter+=1
# board[1][1] = "X" #Computer always goes first and first move is always in the middle

def init_board():
    global board_frame_1, board_frame_2, board
    board_frame_1 = (("+" + 7*"-")*3 + "+") #see diagram above
    board_frame_2 = (("|" + 7*" ")*3 +  "|")
    board = [["-" for column in range(3)]for row in range(3)]

    #setting the starting values of the board to 1-9
    counter = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = counter 
            counter+=1
    board[1][1] = "X" #Computer always goes first and first move is always in the middle

def display_board(board):
        # The function accepts one parameter containing the board's current status
        # and prints it out to the console.
    
    for i in range(len(board)):
        print(" "*41, board_frame_1, "\n", " "*41, board_frame_2, sep="")
        print(" "*40,"|  ", board[i][0], "  |  ", board[i][1], "  |  ", board[i][2], "  |")
        print(" "*40, board_frame_2)
    print(" "*40, board_frame_1)  #bottom frame of the board
    
    return board


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    global game_finished
    player = "O"
    move = False
    while move == False:
        try:
            make_list_of_free_fields(board)
            print(" "*38 +"Your available choices are: ", free_fields)
            choice = int(input(" "*23 + "Please input an available choice, or enter '000' if you give up: "))
        except:
            print("You did not enter a number, please try again.")
            continue
       
        if choice in free_fields:
            for i in range(3):
                for j in range(3):
                    if choice == board[i][j]:
                        board[i][j] = player
            break
       
        if choice == 000: #if player wants to quit
            game_finished = True
            break
        
        else:
            print(" "*30 + choice, "is not an available option please try agian.")
            continue
    
    return choice


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    n = "X" and "O"
    global free_fields
    free_fields = []
    for i in range(3):
        for j in range(3):
            if "X" != board[i][j] and "O" != board[i][j]:
                free_fields.append(board[i][j])
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if sign == "X":
        winner = "computer"
    if sign == "O":
        winner = "me"
    cross1 = cross2 = True

    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] ==sign: #check columns
            return winner
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign: #check rows
            return winner
        
        if board[i][i] != sign: #check cross patter \ (cross1)
            cross1 = False
        if board[i][3 - 1 - i] != sign: #check cross pattern / (cross2)
            cross2 = False

    if cross1 or cross2 == True:
        return winner
    
    return False

def draw_move(board):
    computer = "X"
    make_list_of_free_fields(board)
    n = randrange(len(free_fields))
    choice = free_fields[n]
    print(" "*45+"Computer chose: ", choice)

    for i in range(3):
        for j in range(3):
            if choice == board[i][j]:
                board[i][j] = computer
    make_list_of_free_fields(board)

def main():
    global game_finished, free_fields
    init_board()
    print("""                     
                                    + -----------------------------------+
                                    |             Welcome!!!             |
                                    |         Tic-Tac-Toe Game           |
                                    |       Written By: Mr_BadDev        |
                                    |         Date: 16 MAR 2022          |
                                    |         I hope you Enjoy!!         |
                                    +------------------------------------+
          """)

    game_finished = input("""
                                        
                                        The game is about to begin! 
                                    If you do not want to play enter "n":
                        """)

    if game_finished == "n":
        game_finished = True
    else:
        game_finished = False

    while game_finished == False:
        display_board(board)
        enter_move(board) #player turn
        if  game_finished == True:
            break

        if victory_for(board, "O") == "me": #Check to see if player won after each turn
            display_board(board)
            print("""
                               +----------------------------------------------+   
                               |                                              |
                               |    Congradulations! You are the winner!!!    |
                               |                                              |
                               +----------------------------------------------+
            
            """)
            break
        
        draw_move(board) #Computer turn
        if victory_for(board, "X") == "computer": #Check if computer won
            display_board(board)
            print("""
                               +----------------------------------------------+   
                               |                                              |
                               |          Unfortunatly, you lost...           |
                               |           Better luck next time!             |
                               |                   :(                         |
                               +----------------------------------------------+
            
                  """)
            break
        
        if free_fields == []:
            display_board(board)
            print("""
                               +----------------------------------------------+   
                               |                                              |
                               |               It's a tie!!!!!                |
                               |                                              |
                               +----------------------------------------------+
            
                  """)
            break
        
while True:
    main()
    
    play_again = input(" "*36+"Would you like to play again?[y/n]:")

    if play_again == "n":
        print(" "*41 + "Thank You for playing!!!")
        break

