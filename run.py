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

