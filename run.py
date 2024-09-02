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

def user_guess():
    """
    This gets the user guess and checks if it 
    is a valid guess, if the guess has already been made,
    check whether its a hit or miss and show the result.
    """
    print_board(user_guesses)
    repeat = True
    while repeat:
        while True:
            guess_col = input("Guess a column:\n")
            if validate_data(guess_col):
                break
        while True:
            guess_row = input("Guess a row:\n")
            if validate_data(guess_row):
                break

        guess_col = int(guess_col)-1
        guess_row = int(guess_row)-1


        # Check if the user has already chosen that spot
        if (user_guesses[guess_col][guess_row] == " # " or user_guesses[guess_col][guess_row] == " * "):
            print("You've already guessed there, try again!")
        else:
            repeat = False
        # Check if its a hit or not and display result
        if comp[guess_col][guess_row] == " X ":
            user_guesses[guess_col][guess_row] = " * "
            print("Nice shot!!")
        else:
            user_guesses[guess_col][guess_row] = " # "
            print("Unlucky! You missed")

def comp_guess():
    """
    This allows the computer to guess at the users board using
    randomly generated points
    """
    print_board(comp_guess)
    repeat = True
    guess_col = random_num(comp)
    guess_row = random_num(comp)
    # Check if spot already guessed
    while repeat:
        if (user[guess_col][guess_row] == " # " or user[guess_col][guess_row] == " * "):
            guess_col = random_num(comp)
            guess_row = random_num(comp)
        else:
            repeat = False
    # Tell the user what the computer chose
    print(f"Computer chose {guess_col + 1}, {guess_row + 1}")
    if user[guess_col][guess_row] == " X ":
        user[guess_col][guess_row] == " * "
        print("It's a hit!")
    else:
        user[guess_col][guess_row] = " # "
        print("Computer misses!")
        
def play_game():
    """
    This is to start the game with welcome message and create the boards 
    """
    generate_board()
    welcome_to_game()
    i = 0
    while i < 10:
        print(f"\nThis is turn {i +1}/10 \n")
        user_guess()
        print_board(user_guesses)
        input("\nPress enter to continue :)")
        comp_guess()
        print("\nHere is your board: ")
        print_board(user)
        input("\npress enter to continue")
        i =+ 1
        if check_winner(user) == 4:
            i = 10
        elif check_winner(user guesses) == 4:
            i = 10
    check_winner_final()
    

def validate_data(value):
    """
    This is to check if the values given are within the boards perimiters, if not a message will be displayewd stating that.
    """
    try:
        if int(value) > 5 or int(value) <1:
            raise ValueError("Out of bounds, choose a number between 1 and 5!")
    except ValueError as e:
        print(f"Invalid data {e}, Please try again.")
        print("Please enter an interger between 1 and 5")
        return False
    return True

def check_winner(board):
    """
    Check for a winner after 10 goes
    """
    user_result = check_winner(user_guesses)
    comp_result = check_winner(user)
    if user_result > comp_result:
        print("Congratulations you are a winner!!")
    elif user_result < comp_result:
        print("Unlucky, the computer wins this one")
    else:
        print("It's a draw!")
    

play_game()
    