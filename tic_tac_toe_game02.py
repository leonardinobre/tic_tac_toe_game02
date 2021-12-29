from time import sleep
from random import choice



def get_natural_num(msg):

    """
    Get a valid natural number from the user!

       :param msg: message asking for a natural number
       :return: a positive integer converted from the user enter.
       """

    valid_enter = False

    while not valid_enter:

        given_number = input(msg).strip()

        if given_number.isdigit():
            num = int(given_number)
            valid_enter = True
            return num


msg = """

A TIC TAC TOE GAME

This is a tic tac toe game!
The board has 9 positions, from 1 to 9.

You have to choose a position in the board not covered yet;
and it will put your mark on that position!

If you choose a position, not on the board, or if you choose a position already gone,
you may choose another position.

Let's play!
"""

print(msg)


while True:

    again = 'r'

    while again not in 'Y/N':

        again = str(input("Let's play again? Y/N:  ")).strip().upper()
        print()

    if again in 'N':
        break

    # ----Global Variables----

    # the initial board
    board = ['-', '-', '-'
            ,'-', '-', '-'
            ,'-', '-', '-']

    # game is still going
    game_still_going = True

    # Who won? or Tie?
    winner = None

    # positions to start with
    positions = [1 , 2, 3, 4, 5, 6, 7, 8, 9]

    # current player
    current_player = 'X'

    # initial guess
    guess = 0


    def play_game():

        flip_player()

        pick_up_the_position()

        display_board()

        check_winner()


    def display_board():

        print(board[0], "|", board[1], "|", board[2])
        print(board[3], "|", board[4], "|", board[5])
        print(board[6], "|", board[7], "|", board[8])

        print()


    def flip_player():

        global current_player

        if current_player == 'X':
            current_player = 'O'
            computer_turn()

        elif current_player == 'O':
            current_player = 'X'
            user_turn()


    def computer_turn():

        global guess

        guess = choice(positions)


    def user_turn():

        global guess

        while guess not in positions:

            guess =get_natural_num("Choose a position from 1-9:  ")
            print()


    def pick_up_the_position():

        global guess

        position_index = guess - 1
        positions.remove(guess)

        board[position_index] = current_player

        sleep(1)


    def check_winner():

        global game_still_going

        check_rows()
        check_columns()
        check_diagonals()

        if winner == 'X' or winner == 'O':
            print(f'{winner} won!\n')
            game_still_going = False

        elif "-" not in board:
            print("Tie!\n")
            game_still_going = False


    def check_rows():

        global winner

        row_1 = board[0] == board[1] == board[2] != '-'
        row_2 = board[3] == board[4] == board[5] != '-'
        row_3 = board[6] == board[7] == board[8] != '-'

        if row_1:
            row_winner = board[0]
        elif row_2:
            row_winner = board[3]
        elif row_3:
            row_winner = board[6]

        if row_1 or row_2 or row_3:
           winner = row_winner


    def check_columns():

        global winner

        column_1 = board[0] == board[3] == board[6] != '-'
        column_2 = board[1] == board[4] == board[7] != '-'
        column_3 = board[2] == board[5] == board[8] != '-'

        if column_1:
            column_winner = board[0]
        elif column_2:
            column_winner = board[1]
        elif column_3:
            column_winner = board[2]

        if column_1 or column_2 or column_3:
           winner = column_winner


    def check_diagonals():

        global winner

        diagonal_1 = board[0] == board[4] == board[8] != '-'
        diagonal_2 = board[2] == board[4] == board[6] != '-'

        if diagonal_1:
            diagonal_winner = board[0]
        elif diagonal_2:
            diagonal_winner = board[2]

        if diagonal_1 or diagonal_2:
           winner = diagonal_winner


    while game_still_going:
        play_game()

    else:

        print('GAME OVER!')
        print('Visit on github: leonardinobre')
        print()

    sleep(5)

