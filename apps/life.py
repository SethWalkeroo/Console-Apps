from os import system
from time import sleep
from colored import fg, bg, attr
from welcome import title_card, loading_animation
import random
from itertools import cycle



blinker = [(0, 0), (1, 0), (-1, 0)]

toad = [(0, 0), (0, 1), (0, 2),
		(1, -1), (1, 0), (1, 1)]

glider = [(0, 2),
		(1, 2),
		(2, 2), (2, 1), (1, 0)]

acorn = [(1, 2),
		(2, 4),
		(3, 1), (3, 2), (3, 4), (3, 5), (3, 6)]

light_spaceship = [(0, 3), (0, 4),
				(1, 1), (1, 2), (1, 4), (1, 5),
				(2, 1), (2, 2), (2, 3), (2, 4),
				(3, 2), (3, 3)]

middle_spaceship = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
					(1, 0), (1, 5),
					(2, 0),
					(3, 1), (3, 5),
					(4, 3)]

large_spaceship = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
				(1, 0), (1, 6),
				(2, 0),
				(3, 1), (3, 6),
				(4, 3), (4, 4)]

gosper_glider_gun = [(1, 25),
					(2, 23), (2, 25),
					(3, 13), (3, 14), (3, 21), (3, 22), (3, 35), (3, 36),
					(4, 12), (4, 16), (4, 21), (4, 22), (4, 35), (4, 36),
					(5, 1), (5, 2), (5, 11), (5, 17), (5, 21), (5, 22),
					(6, 1), (6, 2), (6, 11), (6, 15), (6, 17), (6, 18), (6, 23), (6, 25),
					(7, 11), (7, 17), (7, 25),
					(8, 12), (8, 16),
					(9, 13), (9, 14)]

ptrns = [blinker, toad, glider, acorn, light_spaceship,
		middle_spaceship, large_spaceship, gosper_glider_gun,]

ptrns_str = ['blinker', 'toad', 'glider', 'acorn',
			'light spaceship', 'middle_spaceship',
			'large spaceship', 'gosper glider gun',
			'custom pattern']

reset = attr('reset')
pattern_symbol = fg('green') + '◼' + reset
board_pattern = fg(16) + '◻' + reset
patterns = {str(count):ptrn for count, ptrn in enumerate(ptrns, 1)}
colors = cycle([i for i in range(9, 231)])
test_symbols = cycle([fg(next(colors)) + '◼' + reset for i in range(231)])
space = 10
spacing = ' ' * space
grid_size_x = 50
grid_size_y = 50

def adjacent_check(map, gx, gy, x, y, wrap=True):
	adjacent_living = 0
	positions = [(x, y-1), (x, y+1), (x-1, y), (x+1, y), (x-1, y+1),
				(x-1, y-1), (x+1, y-1), (x+1, y+1)]
	for x, y in positions:
		if wrap:
			max_x = gx - 1
			max_y = gy - 1
			if x > max_x:
				x = 0
			elif x < 0:
				x = max_x
			if y > max_y:
				y = 0
			elif y < 0:
				y = max_y
			if map[x][y] == pattern_symbol:
				adjacent_living += 1
		else:
			if x == -1 or y == -1:
				pass
			else:
				try:
					if map[x][y] == pattern_symbol:
						adjacent_living += 1
				except IndexError:
					pass

	return adjacent_living

def starting_cells(map, cell_list, ptrn_symbol, init_x=0, init_y=0):
	for x, y in cell_list:
		adjusted_x = x + init_x
		adjusted_y = y + init_y
		if adjusted_x >= 0 and adjusted_y >= 0:
			if map[adjusted_x][adjusted_y] == pattern_symbol:
				break
			else:
				map[adjusted_x][adjusted_y] = ptrn_symbol
		else:
			break

def life_rules(map, gx, gy, wrap=True):
	dead_cells = []
	birthed_cells = []
	for x_pos in range(gx):
		for y_pos in range(gy):
			if map[x_pos][y_pos] == pattern_symbol:
				if adjacent_check(map, gx, gy, x_pos, y_pos, wrap) >= 4:
					dead_cells.append((x_pos, y_pos))
				elif adjacent_check(map, gx, gy, x_pos, y_pos, wrap) < 2:
					dead_cells.append((x_pos, y_pos))
			elif map[x_pos][y_pos] == board_pattern:
				if adjacent_check(map, gx, gy, x_pos, y_pos,wrap) == 3:
					birthed_cells.append((x_pos, y_pos))

	for x, y in dead_cells:
		map[x][y] = board_pattern
	for x, y in birthed_cells:
		map[x][y] = pattern_symbol


def map_wipe(map, gx, gy, symbol=pattern_symbol, nuke=False):
	for x in range(gx):
		for y in range(gy):
			if map[x][y] == symbol:
				map[x][y] = board_pattern
	if nuke:
		for x in range(gx):
			for y in range(gy):
				if map[x][y] == pattern_symbol:
					map[x][y] = board_pattern

def life_main():

	system('clear')
	title_card('WELCOME TO THE GAME OF LIFE!', thickness=2)
	print()
	print()
	print('Enter the lengths for the x and y axis of the display grid...')
	print()
	print(fg('yellow') + 'WARNING: ' + reset + 'A size >= 38x38 is recommended for all patterns to fit' + reset)
	print()
	print()

	while True:
		try:
			grid_size_x = int(input('How large do you want the x axis to be?: '))
			print()
		except ValueError:
			loading_animation('ERROR: Please enter an integer value...', time=1)
			continue
		try:
			grid_size_y = int(input('How large do yo uwant the y axis to be?: '))
			break
		except ValueError:
			loading_animation('ERROR: Please enter an integer value...', time=1)

	gx = grid_size_x
	gy = grid_size_y

	map = [[board_pattern for i in range(grid_size_x)]for i in range(grid_size_y)]


	def map_display(map, coordinates=True):
		if coordinates:
			print('     ' + spacing + '0' + (' ' * (grid_size_x * 2 - 3)) + str(grid_size_x - 1))
			print('     ' + spacing + ''.join(['-' for i in range(grid_size_x * 2)]))
			for count, line in enumerate(map):
				if count < 10:
					print(spacing + '{}  | {}'.format(count, ' '.join(line) + '|'))
				else:
					print(spacing + '{} | {}'.format(count, ' '.join(line) + '|'))
			print('     ' + spacing + ''.join(['-' for i in range(grid_size_x * 2)]))
		else:
			for line in map:
				print(spacing + ' '.join(line))

	while True:
		system('clear')
		pattern_choice = None
		message = 'ol,{}'.format(','.join(ptrns_str))
		print()
		map_wipe(map, gx, gy, nuke=True)
		display_map = map.copy()
		loading_animation(time=1)
		while pattern_choice != 'f':
			title_card(message)
			pattern_choice = input('Which pattern would you like to add to the grid?: ')
			print()
			# map_display(map)
			# system('clear')
			if pattern_choice == '9':
				pass
			elif pattern_choice in patterns:
				while True:
					try:
						symbol = next(test_symbols)
						system('clear')
						map_display(map)
						print()
						print(spacing + 'Enter starting position for pattern')
						print()
						try:
							init_x = int(input(spacing + 'Enter x coordinate: '))
						except ValueError:
							loading_animation('ERROR: make sure to enter integer value', time=1)
							continue
						print()
						try:
							init_y = int(input(spacing + 'Enter y coordinate: '))
						except ValueError:
							loading_animation('ERROR: make sure to enter integer value', time=1)
							continue
						pattern = patterns[pattern_choice]
						starting_cells(display_map, pattern, symbol, init_x, init_y)
						system('clear')
						map_display(display_map)
						print()
						confirmation = input(spacing + 'Are you sure about this placement? (y/n): ')
						if confirmation == 'y':
							starting_cells(map, pattern, pattern_symbol, init_x, init_y)
							print()
							another = input(spacing + f'would you like to add another pattern {pattern_choice}? (y/n): ')
							print()
							if another == 'y':
								pass
							else:
								print(spacing + ' - Type "f" to see your masterpiece')
								print(spacing + ' - Type "w" to wipe the entire grid')
								print(spacing + ' - Or hit enter to enter another pattern')
								print()
								pattern_choice = input(spacing + 'enter response: ')
								if pattern_choice == 'wipe':
									map_wipe(display_map, gx, gy, symbol, nuke=True)
									loading_animation('wiping entire board', time=1)
								system('clear')
								break
						else:
							map_wipe(display_map, gx, gy, symbol)

					except IndexError:
						loading_animation('** ERROR: Those coordinates either don\'t exist or do not fit the selected patern **', time=3)
						map_wipe(display_map, gx, gy, symbol)
			else:
				loading_animation('Sorry that pattern is not in the patterns list. Try again.', time=2)

		while True:
			try:
				loading_animation(time=1)
				print()
				print()
				length = int(input(spacing + 'How long do you want the simulation to run? (seconds): '))
				print()
				wrap_choice = input(spacing + 'Do you want the cells to wrap past the borders? (y/n): ')
				if wrap_choice == 'y':
					wrap = True
				else:
					wrap = False
				break
			except ValueError:
				print('Please only enter integer values...')

		system('clear')
		for i in range(length * 20):
			map_display(map, coordinates=False)
			life_rules(map, gx, gy, wrap=wrap)
			sleep(.05)
			system('clear')

		loading_animation(spacing + 'ending simulation...', time=1)
		print()
		print()
		repeat = input(spacing + 'Would you like to create another game of life? (y/n): ')
		if repeat == 'y':
			pattern_choice = 'again!'
		else:
			break

	system('clear')
	title_card('THANKS FOR TRYING OUT MY APP!')
	sleep(1)
	loading_animation('Goodbye!', time=1)

def pattern_test():
	pattern_choice = '7'
	pattern = patterns[pattern_choice]
	starting_cells(map, pattern)
	map_display(map)

if __name__ == '__main__':
	system('clear')
	mode = 'main'
	if mode == 'main':
		life_main()
	else:
		pattern_test()
