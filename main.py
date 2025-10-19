def create_board():
    # The main function to run the game loop and manage turns between the user and the computer.
    # [['', '', ''], ['', '', ''], ['', '', '']]
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    return board


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    display = f"""
    +===========+
    | {board[0][0]} | {board[0][1]} | {board[0][2]} |
    +-----------+
    | {board[1][0]} | {board[1][1]} | {board[1][2]} |
    +-----------+
    | {board[2][0]} | {board[2][1]} | {board[2][2]} |
    +===========+
    """
    print(display)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    free_moves = make_list_of_free_fields(board)
    print("Your turn! Enter the number of the field where you want to place your 'O': ")
    
    location = input()
    position = get_board_position(location)
    if position and position in free_moves:
        board[position[0]][position[1]] = 'O'
    else:
        print("Invalid move. Try again.")
        enter_move(board)
    

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['O', 'X']:
                free_moves.append((i, j))
    return free_moves
                

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    # check rows 
    for row in board:
        if all(s == sign for s in row):
            return True
        
    # check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
        
    # check diagonals
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

def draw_move(board):
    # The function draws the computer's move and updates the board.
    import random as rnd
    random_move = rnd.choice(make_list_of_free_fields(board))
    board[random_move[0]][random_move[1]] = 'X'
    print("Computer placed an 'X'.")
    display_board(board)
    
def get_board_position(move):
    # The function converts the user's input (a number from 1 to 9) 
    # into the corresponding row and column numbers.
    move_map = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2)
    }
    return move_map.get(move, None)


def main():
    board = create_board()
    
    while (True):
        
        display_board(board)
        enter_move(board)
        
        if victory_for(board, 'O'):
            display_board(board)
            print("Congratulations! You win!")
            return
        
        if len(make_list_of_free_fields(board)) == 0:
            print("It's a tie!")
            return
        
        draw_move(board)
        
        if victory_for(board, 'X'):
            display_board(board)
            print("Computer wins! Better luck next time.")
            return

if __name__ == "__main__":
    main()