# Write a program to create a classic Tic Tac Toe game. Two players take turns
# marking Xs and Os on a 3x3 grid. The first player to align three of their marks
# either vertically, horizontally, or diagonally wins the game.
# The board is printed after each move, with colored marks to distinguish between
# the players. The game checks for a winner after each move and ends when a
# player wins or when the board is full, resulting in a draw.

# Optional Enhancements
# • Add a scoring system that tracks the number of games won by each player
# across multiple rounds.
# • Allow players to start a new game without restarting the program.

def turn(board):

    while True:

        try:
            row = int(input("Enter row (0-2):"))
            column = int(input("Enter Column (0-2):"))
        except ValueError:
            print("Please enter numbers only.")
            continue         
        if row > 2 or row < 0:
            print("only 0,1,2 are allowed in row")

        elif column > 2 or column < 0:
            print("only 0,1,2 are allowed in column") 

        elif board[row][column] != "":
            print(row,column,"position is alreay taken")
          
        else:
            return row,column


def player_turn(board, symbol): 
    print(f"Player {symbol}'s Turn")
    row,column = turn(board)
    board[row][column] = symbol


def print_board(board):
    for row in board:
        print("---+---+---")
        for column in range(len(row)):
            print(f" {row[column] if row[column] else ' '} ", end="")
            if column < len(row) - 1:
                print("|",end="")
        print()
    print("---+---+---")

def board_check(board):
    #Horizontal check
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col] 

    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]    
     
def check_board_full(board):
    for row in board:
        for cell in row:
            if cell == '':
                return False  
    return True  
            
def tic_tac_toe(board,score_O,score_X):
    while True:
        player_turn(board,'O')
        print_board(board)
        rtn  = board_check(board)
        if rtn == 'X':
            print(" Player X wins ")
            score_X = score_X + 1
            break
        elif rtn == 'O':  
            print("Player O wins")
            score_O = score_O + 1
            break
        rtn2 = check_board_full(board)
        if rtn2 == True:
            print("Game is a Draw")
            break
        player_turn(board,'X')
        print_board(board)
        rtn  = board_check(board)
        if rtn == 'X':
            print(" Player X wins ")
            score_X = score_X + 1
            break
        elif rtn == 'O':
            print("Player O wins")
            score_O = score_O + 1
            break
        rtn2 = check_board_full(board)
        if rtn2 == True:
            print("Game is a Draw")
            break 
    return score_O,score_X




def main():
    board = [['','',''],
            ['','',''],
            ['','','']]
    score_O = 0
    score_X=  0
    print("------------------ Tic Tac Toe Game ------------------")
    print()

    score_O,score_X = tic_tac_toe(board,score_O,score_X)
    print("Score of Player O :", score_O)
    print("Score of Player X :", score_X)
    while True: 
        print("Do you want to play more (y/n): " ,end ="")
        ans = input().lower()
        if ans == 'y':
            for i in board:
                for j in range(len(i)):
                    i[j] = ""
            score_O,score_X = tic_tac_toe(board,score_O,score_X)
            print("Score of Player O :", score_O)
            print("Score of Player X :", score_X)
        else:
            break


main()