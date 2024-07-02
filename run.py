from random import randint

user = []
user_guesses = []
comp = []

def make_board(board):
    """
    This is to make the initial 5 by 5 board,
    consisting of 5 rows and 5 lists of " O "
    """
    for i in range(5):
        board.append([" O "]*5)
    return board

def print_board(board):
    """
    This is to print the board, removing list
    format and adding spaces to make it clearer
    """
    for ind in board:
        print(" ".join(ind))

def random_num(board):
    """
    This is to generate a random number that will
    be used to guess on the board size
    """
    return randint(0, len(board)-1)

def generate_ship(board):
    """
    This loop places 4 " X "(ships) randomly on the board 
    """
    ship_num = 0
    while ship_num < 4:
        ship_num = 0
        ship_col = random_num(board)
        ship_row = random_num(board)
        board[ship_row][ship_col] = " X "
        for row in board:
            ship_num += row.count(" X ")

def welcome_to_game():
    """
    Message to be displayed at the start of the game 
    for the user
    """
    print("Welcome To Battleships!")
    name = input("Type your name and press enter: \n")
    print(f'Hi {name}! We will generate your ships locations now.\n')
    print('O are empty locations, * are hits and # are missed shots\n')
    print('Top left corner is row: 0, col: 0')

def generate_board():
    """
    This is to create the boards ready to play, 
    with the computer boards ships not visable
    """
    make_board(user)
    make_board(comp)
    make_board(user_guesses)
    generate_ship(user)
    generate_ship(comp)