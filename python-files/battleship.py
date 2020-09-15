from string import ascii_uppercase
import random
from welcome import title_card, loading_animation
from colored import fg, attr, bg
from time import sleep
from os import system

#colors for testing
clr = fg('pale_green_1a')
clr2 = fg('red')
clr3 = fg('blue')
clr4 = fg('violet')
clr5 = fg('dark_green')
reset = attr('reset')

#color for hit
space = 8 * ' '
hit_color = fg('red')
hit_symbol = hit_color + 'X' + reset
hit_message = hit_color + (space + '** HIT **') + reset
#color for miss
miss_color = fg(243)
miss_symbol = miss_color + 'X' + reset
highlighted_miss_symbol = fg('black') + bg('orange_red_1') + 'X' + reset
miss_message = miss_color + (space + '** MISS **') + reset
#color for sink
sink_color = fg(46)
#ammo color
ammo_color = fg('orange_red_1')
#border color
border_color = fg('red')
#error color
error_color = fg('red')

carrier_symbol = clr + 'A' + reset
battleship_symbol = clr2 + 'B' + reset
cruiser_symbol = clr3 + 'C' + reset
submarine_symbol = clr4 + 'D' + reset
destroyer_symbol = clr5 + 'E' + reset
board_symbol = 'O'
board_size = 10

used_spaces = [hit_symbol, miss_symbol]
letters = [letter for letter in ascii_uppercase]
directions = ['vertical', 'horizontal']


def display_board(board):
	print('    ' + ' '.join([str(i) for i in range(board_size)]))
	print(border_color + '   ' + '-' * (board_size * 2) + reset)
	for count, row in enumerate(board):
		print('{} {} {}'.format(letters[count], border_color + '|' + reset, ' '.join(row)))


def generate_ship(game_board, size, symbol, direction='horizontal'):

	if direction == 'horizontal':

		while True:
			row = random.randint(0, board_size - 1)
			col_start = random.randint(0, board_size - size)
			if game_board[row][col_start:col_start + size].count(board_symbol) == size:
				break

		for i in range(size):
			game_board[row][i + col_start] = symbol

	elif direction == 'vertical':

		while True:
			row_start = random.randint(0, board_size - size)
			col = random.randint(0, board_size - 1)
			spaces_chosen = [game_board[i + row_start][col] for i in range(size)]
			if spaces_chosen.count(board_symbol) == size:
				break

		for i in range(size):
			game_board[i + row_start][col] = symbol
	else:
		raise Exception(error_color + 'ERROR:' + reset, 'Please choose either "vertical" or "horizontal" for the ship directions')


def hit_check(game_board, user_board, user_row, user_col):
	converted_x = letters.index(user_row.upper())

	if game_board[converted_x][user_col] not in used_spaces and game_board[converted_x][user_col] != board_symbol:
		user_board[converted_x][user_col] = hit_symbol
		game_board[converted_x][user_col] = hit_symbol
		print(hit_message)
	elif game_board[converted_x][user_col] in used_spaces:
		user_board[converted_x][user_col] = highlighted_miss_symbol
		#for testing purposes
		game_board[converted_x][user_col] = highlighted_miss_symbol
		print(ammo_color + '** YOU HAVE ALREADY FIRED ON THAT POSITION! **' + reset)
	else:
		user_board[converted_x][user_col] = miss_symbol
		#for testing purposes
		game_board[converted_x][user_col] = miss_symbol
		print(miss_message)


def sink_check(game_board, ship_list):
	for ship in ship_list.copy():
		for row in game_board:
			if ship in row:
				break
		else:
			print()
			print(sink_color + f'** You sunk the enemy\'s {ship_list[ship]}! {len(ship_list) - 1} ships remaining! **' + reset)
			ship_list.pop(ship)

	if not ship_list:
		return True



def battleship_main():
	title_card('WELCOME TO BATTLESHIP!')
	sleep(1)
	loading_animation('Setting up board...', time=1)
	restart = ''
	while restart != 'no':

		user_board = [[board_symbol for i in range(board_size)]for i in range(board_size)]
		game_board = [[board_symbol for i in range(board_size)]for i in range(board_size)]

		ship_symbol_list = {carrier_symbol: 'carrier', battleship_symbol: 'battleship',
                      cruiser_symbol: 'cruiser', submarine_symbol: 'submarine',
                      destroyer_symbol: 'destroyer'}

		ammo = 35

		generate_ship(game_board, 1, carrier_symbol, random.choice(directions))
		generate_ship(game_board, 4, battleship_symbol, random.choice(directions))
		generate_ship(game_board, 3, cruiser_symbol, random.choice(directions))
		generate_ship(game_board, 3, submarine_symbol, random.choice(directions))
		generate_ship(game_board, 2, destroyer_symbol, random.choice(directions))
		

		game_won = False
		game_lost = False
		while game_won != True and game_lost != True:

			display_board(user_board)
			print()
			print(f'Preparing to fire! {ammo_color + str(ammo) + reset} shot(s) remaining!')
			print()

			try:
				user_row = input('Fire at x coordinate: ')
				user_col = int(input('Fire at y coordinate: '))
				loading_animation(ammo_color + 'FIRE!' + reset, time=1)
				hit_check(game_board, user_board, user_row, user_col)
				game_won = sink_check(game_board, ship_symbol_list)
				ammo -= 1
				if not game_won and ammo == 0:
					game_lost = True
			except IndexError:
				loading_animation(error_color + 'ERROR:' + reset + ' make sure you enter a position that exists on the game board...', time=2)
			except ValueError:
				loading_animation(error_color + 'ERROR:' + reset + ' make sure you enter your coordinates correctly...', time=2)
			sleep(.3)
			print()
		
		if game_lost:
			print(hit_color + '** YOU HAVE RUN OUT OF AMMO! **' + reset)
			print()
		else:
			print(sink_color + '** YOU HAVE SUNK ALL THE BATTLESHIPS! **' + reset)
			print()
		
		display_board(game_board)
		
		restart = input('Would you like to play again? (yes/no): ')

		if restart != 'no':
			loading_animation('resetting the board...', time=1)

	print()
	title_card('LEAVING BATTLESHIP!')
	sleep(1)
	loading_animation('Thanks for playing!', time=2)

if __name__ == '__main__':
	battleship_main()
   
