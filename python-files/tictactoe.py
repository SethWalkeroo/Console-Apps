from itertools import cycle
from string import ascii_uppercase
from colored import fg, bg, attr
from welcome import title_card, loading_animation
from time import sleep
from os import system




def toe_main():

    # color of x
    x_color = fg('red')
    # color of o
    o_color = fg('yellow')
    # resets the colors of the terminal
    reset = attr('reset')
    # This dictionary converts the x coordinate, which is a letter, to a number the program can use to place the move on the board
    play_conversion = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                       'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10}
    # This creates a list from all of the uppercase letters in ascii_uppercase from the string module.
    alphabet = [letter for letter in ascii_uppercase]

    # welcome animation thing from the welcome.py file

    def welcome_message(message):
        try:
            title_card()
        except NameError:
            print('Wecome to tic tac toe')

    def main():
        welcome_message('WELCOME TO TIC TAC TOE!')

        # try-catch statement to prevent invalid inputs for the board size.
        while True:
            try:
                size = int(input('Enter size of the tic tac toe game board: '))
                loading_animation('creating board...', time=1)
                break
            except ValueError:
                loading_animation('ERROR: Please enter an integer value for the board size.', time=1)
                continue

        # loop to make sure that the users don't both have the same name. It breaks the game if they do.
        while True:
            name1 = input('Player 1, enter your name: ')
            loading_animation(time=1)
            name2 = input('Player 2, enter your name: ')
            loading_animation(time=1)
            if name1 != name2:
                break
            else:
                loading_animation('ERROR: Please choose different names...', time=1)

        # player shape dictionary to assign shapes to player 1 and player 2.
        player_shape = {name1: 'X', name2: 'O'}
        print()
        # main game loop that runs as long as again != 'no'
        again = ''
        while again != 'no':
            # players is set to cycle from itertools so we can cycle back and forth between player 1 and player 2 each turn.
            players = cycle([name1, name2])
            # creates a multi dimensional array that is size by size.
            board = [['-' for i in range(size)] for i in range(size)]
            # loop that runs until the game is won and then refreshes the board with the previous loop.
            # A function that prints out the game board array to the console

            def print_board():
                print('  '+' '.join([str(i) for i in range(size)]))
                for count, row in enumerate(board):
                    print(alphabet[count], ' '.join(row))
                print()
            while True:
                print_board()
                # keeps track of the current player using the previous cycled players list.
                current_player = next(players)
                # print whos turn it is
                print('It is {}\'s turn!'.format(current_player))
                print()
                # ask for coordinates and performs the players placement. Currently using many if else statements for specific error checking. Could be improved upon.
                while True:
                    x = input('Please enter the x position: ')
                    try:
                        y = int(input('Please enter the y position: '))
                        break
                    except ValueError:
                        loading_animation('ERROR: please enter an integer value', time=1)

                system('clear')

                # variables for the player shapes so I dont have to repeat them.
                player_x = x_color + player_shape[name1] + reset
                player_o = o_color + player_shape[name2] + reset

                # variable for the player move
                player_move = board[play_conversion[x.upper()]][y]

                # Checks to see if the space already has a shape in it and punishes the player if it does. I need to change this eventually
                if player_move != player_x and player_move != player_o:
                    if current_player == name1:
                        board[play_conversion[x.upper()]][y] = x_color + \
                            player_shape[current_player] + reset
                    else:
                        board[play_conversion[x.upper()]][y] = o_color + \
                            player_shape[current_player] + reset
                else:
                    print(
                        'That space has already been played... as punishment you lose your turn!')
                    print()
                    continue

                # This is a win_check function that holds all the other win functions.
                # It checks the other win functions and sees if they returned True or False
                # and then checks whether it was 'X' or 'O' and prints a message accordingly.
                def win_check(*args):
                    for arg in args:
                        if arg != None:
                            if arg[0]:
                                if arg[1] == 'x':
                                    print_board()
                                    print(
                                        x_color + '{} HAS WON!'.format(name1.upper()) + reset)
                                    print()
                                    return True
                                else:
                                    print_board()
                                    print(
                                        o_color + '{} HAS WON!'.format(name2.upper()) + reset)
                                    print()
                                    return True
                                    # check to see if anyone got three in a row horizontally

                def rows():
                    for row in board:
                        if row.count(player_x) == size or row.count(player_o) == size:
                            if player_x in row:
                                return True, 'x'
                            elif player_o in row:
                                return (True, 'o')

                # Check to see if anyone got three in a row vertically
                def columns():
                    for i in range(size):
                        x_count = 0
                        o_count = 0
                        for row in board:
                            if row[i] == player_x:
                                x_count += 1
                            elif row[i] == player_o:
                                o_count += 1
                        if x_count == size:
                            return (True, 'x')
                        elif o_count == size:
                            return (True, 'o')

                # Checks to see if anyone won the game diagonally
                def diagonals(reverse=False):
                    diagx2_count = 0
                    diago2_count = 0
                    if reverse:
                        for count, i in enumerate(reversed((range(size)))):
                            if board[count][i] == player_x:
                                diagx2_count += 1
                            elif board[count][i] == player_o:
                                diago2_count += 1
                    else:
                        for i in range(size):
                            if board[i][i] == player_x:
                                diagx2_count += 1
                            elif board[i][i] == player_o:
                                diago2_count += 1
                    if diagx2_count == size:
                        return (True, 'x')
                    elif diagx2_count == size:
                        return (True, 'o')

                # check to see if it is a tie game
                def tie_check():
                    row_count = 0
                    for row in board:
                        if '-' not in row:
                            row_count += 1
                    if row_count == 3:
                        print_board()
                        print('CATS GAME!')
                        return True

                # Prints the appropriate message depending on whether win_check or tie_check returns True.
                if win_check(rows(), columns(), diagonals(), diagonals(reverse=True)):
                    again = input('Would you like to play again?: ')
                    loading_animation(time=1)
                    break
                elif tie_check():
                    again = input('Would you like to play again?: ')
                    loading_animation(time=1)
                    break

        try:
            title_card('NOW LEAVING TIC TAC TOE!')
        except NameError:
            print('EXITING SETH\'S TIC TAC TOE GAME!')

        sleep(2)
        loading_animation('Goodbye!', time=1)
    main()


if __name__ == '__main__':
    toe_main()
