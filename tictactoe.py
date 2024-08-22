# displays the board
def display_board(board):
    print('\n' * 100)

    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

# choose markers
def player_input():
    marker = '' 
    while not (marker == 'X' or marker == 'O'):
        marker = input('Choose your marker (Enter "X" or "O") >>> ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
# place marker on board
def place_marker(board, marker, position):
    board[position] = marker

# check if game won
def win_check(board, mark):
    return (
        board[1] == mark and board[5] == mark and board[9] == mark or
        board[3] == mark and board[5] == mark and board[7] == mark or
        board[3] == mark and board[6] == mark and board[9] == mark or
        board[2] == mark and board[5] == mark and board[8] == mark or
        board[1] == mark and board[4] == mark and board[7] == mark or
        board[7] == mark and board[8] == mark and board[9] == mark or
        board[4] == mark and board[5] == mark and board[6] == mark or
        board[1] == mark and board[2] == mark and board[3] == mark
    )

# choose who will go first
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
# check if board position is empty
def space_check(board, position):
    return board[position] == ' '

# check if board is full
def full_board_check(board):
    for position in range(1, 10):
        if space_check(board, position):
            return False
    return True

# choose next position
def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input('Choose your next position (Enter a number 1-9) >>> '))
        except ValueError:
            print("Please enter a valid number!")
    return position

# choose to play again
def replay():
    choice = ''
    while not (choice == 'yes' or choice == 'no'):
         choice = input('Play again? (Enter "Yes" or "No") >>> ').lower()
    if choice == 'yes':
         return True
    else: 
         return False

# main game
print('Welcome to Tic Tac Toe!')

while True:
    # set up the game (board and turn)
    game_board = [' '] * 10
    player_one_marker, player_two_marker = player_input()
    turn = choose_first()
    print(turn, 'is going first!')

    # choose if ready to play
    ready = ''
    while not (ready == 'yes' or ready == 'no'):
        ready = input('Ready to play? (Enter "Yes" or "No") >>> ').lower()
    if ready == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        # player one's turn
        if turn == 'Player 1':
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player_one_marker, position)
            if win_check(game_board, player_one_marker):
                display_board(game_board)
                print("Player one wins!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("It is a draw!")
                    game_on = False
                else:
                    turn = 'Player 2'
        # player two's turn
        else:
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player_two_marker, position)
            if win_check(game_board, player_two_marker):
                display_board(game_board)
                print("Player two wins!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("It is a draw!")
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break