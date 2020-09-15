from PyDictionary import PyDictionary
from emoji import emojize
from itertools import cycle
from time import sleep
from colored import fg, bg, attr
from welcome import title_card
from os import system
from time import sleep


class MyDictionary:

	#creating instance of the PyDictionary class
	dictionary = PyDictionary()

	#color variables for easier use of the colored module
	red = fg('red_3a')
	cyan = fg('blue')
	gold = fg('light_goldenrod_1')
	key_color = bg('black') + fg('white')
	reset = attr('reset')
	bold = attr('bold')

	#a function created to clear the console with the os.system() function
	def clear(self):
		system('clear')

	def help_commands(self):
		print()
		print('q - quits the dictionary')
		print('cls - clears the console')

	#welcome message generated using the title_card function from the welcome.py script
	def welcome_card(self, message):
		try:
			title_card(message, msg_color='white', msg_bg_color=16, ptrn_color='light_goldenrod_1', thickness=2)
		except NameError:
			print(message)

	def exit_card(self, message):
		try:
			title_card(message, msg_color='white', msg_bg_color=16, ptrn_color='light_goldenrod_1', thickness=2)
			sleep(2)
		except NameError:
			print(message)
			sleep(1)

	#main dictionary loop
	def main(self):

		#call to the welcome_card function
		self.welcome_card('WELCOME TO SETH\'S HOLY DICTIONARY!')

		#main loop for finding definitions.
		#this initial part is for accepting certain commands or entering a word.
		word = ''
		while word.strip() != 'q':
			print()
			word = input(self.gold + 'Type the word you want to know (type "help" for commands): ' + self.reset)
			if word == 'dev_quit':
				break
			elif word == 'cls':
				self.clear()
				continue
			elif word == 'help':
				self.help_commands()
				continue
			print()
			print()

			#the != 'q' part makes sure that the program doesn't try to find the definition of 'q'
			#the try and except statement usese the PyDictionary module to find a definition for the word and then displays a formatted string with said defintions.
			if word.strip() != 'q':
			    try:
			        for key, value in self.dictionary.meaning(word, disable_errors=True).items():
			            print('* --> {}: {}\n'.format(self.key_color +self.bold + key + self.reset, self.key_color + ' '.join(value) + self.reset))
			    except:
			        print(self.cyan + self.bold + emojize('Oh no! :fearful: that word is not in my dictionary! Try googling it instead?', use_aliases=True) + self.reset)
			        print()

		#call to the exit_card function
		self.exit_card('EXITING SETH\'S HOLY DICTIONARY!')


if __name__ == '__main__':
	mydictionary = MyDictionary()
	mydictionary.main()
