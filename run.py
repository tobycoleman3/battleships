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