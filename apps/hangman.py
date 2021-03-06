from english_words import english_words_alpha_set
from random import choice
from itertools import cycle
from colored import fg, bg, attr
from PyDictionary import PyDictionary
from welcome import title_card, loading_animation
from os import system
from time import sleep
from hangmanimage import man


#actual code begins here. Declaring the again variable for use later in te program.
class Hangman:

		#creating an instance of PyDictionary for getting definitions at the end of the game loop.
		dictionary = PyDictionary()


		#colored reset attribute I have up here for some stupid reason.
		reset = attr('reset')
		yellow = fg('light_goldenrod_1')
		bold = attr('bold')
		red = fg('red_3a')
		cyan = fg('cyan')
		definition_color = bg('black') + fg('white')

		#variables
		wrong = 0
		guess = ''
		guessed_chars = []

		#choosing a random word in the word_list
		word_choice = ''
		#setting that word to a list of lowercase charactaers
		word = ''
		#creating an underscore character for each letter in word
		word_spaces = ''
		
		def __init__(self, managed=True):
			self.managed = managed


		#function for clearing the console
		def clear(self):
			system('clear')

		#A word list generated by splitting each line in word.txt by space and then appending them to this python list for use in the program.
		def word_list_create(self, managed):
			word_list = []
			if managed:
				with open('data/words.txt', 'r') as words_txt:
					for line in words_txt:
						for word in line.split():
							word_list.append(word)
			else:
				with open('../data/words.txt', 'r') as words_txt:
					for line in words_txt:
						for word in line.split():
							word_list.append(word)
							
			return word_list

		#code to search for an item through the dictionary
		def my_dict(self, response):
			if response == 'yes':
			    try:
			        for key, value in self.dictionary.meaning(''.join(self.word)).items():
			            print('* --> {}: {}\n'.format(self.definition_color + key + self.reset, self.definition_color + ' '.join(value) + self.reset))
			    except:
			        print('Sorry my dictionary couldn\'t find this word. Try google instead.')


		#welcome message from the welcome script
		def welcome_card(self, message):
			try:
				title_card(message)
			except NameError:
			  print(message)


		def exit_card(self, message):
			title_card(message, msg_color='white', ptrn_color='white')
			sleep(2)
			self.clear()


		def hangman_display(self):
			print()
			print(self.cyan + self.bold + man[self.wrong] + self.reset)
			print()
			print('Guessed characters:', self.bold + ', '.join(self.guessed_chars))
			print()
			print(self.cyan + ' '.join(self.word_spaces) + self.reset)
			print()


		def win_check(self, guess, empty_spaces):
			if '_' not in empty_spaces or guess == ''.join(self.word):
				print(self.yellow + self.bold + 'YOU WIN! You guessed the word "{}" in exactly {} tries!'.format(''.join(self.word), self.wrong) + self.reset)
				print()
				return True
			elif self.wrong == len(man):
				print(self.red + 'YOU LOST! You didn\'t guess the word {} in {} tries!'.format(self.red + self.bold + '"' + ''.join(self.word) + '"' + self.reset + self.red, self.wrong))
				print(self.reset)
				return True


		def main(self):

			self.welcome_card('WELCOME TO HANGMAN!')
			sleep(1)
			loading_animation('Starting game...', time=1)
			#main game loop
			again = ''
			while again != 'no':

				#a list for storing all of the guessed characters during runtime
				self.word_choice = choice([i for i in self.word_list_create(self.managed)])
				self.word = [i.lower() for i in self.word_choice]
				self.word_spaces = ['_' for i in self.word]
				self.guessed_chars = []
				self.wrong = 0
				#loop that runs until the game is won.
				game_won = False

				while game_won != True:


					self.hangman_display()

					self.guess = input('guess a letter in the word: ')
					self.clear()
					print()

				    #returns the user to the beginning fo the loop if the character has already been guessed
					if self.guess in self.guessed_chars:
						print(self.red + 'YOU HAVE ALREADY GUESSED THAT CHARACTER! SELECT ANOTHER!' + self.reset)
						continue

					#checks to see if the guess is not a number or special character and then either checks the word or returns you to the beginning of the loop.
					if self.guess.isalpha():
						for count, char in enumerate(self.word):
							if char == self.guess:
								self.word_spaces[count] = self.guess
							else:
								continue

					#if the character is not in the word add 1 to wrong
					if self.guess not in self.word:
						self.wrong += 1

					#always append the guessed char to the guessed char list
					self.guessed_chars.append(self.guess)


					if self.win_check(self.guess, self.word_spaces):
						definition = input('Would you like to know the definition of the word?: ')
						print()
						self.my_dict(definition)
						print()
						again = input('Would you like to play again? (yes/no): ')
						loading_animation(time=1)
						game_won = True
						print()



			#exit message generated from my welcome script.
			self.exit_card('EXITING HANGMAN!')
			sleep(1)
			loading_animation('Goodbye!', time=1)

if __name__ == '__main__':
	hangman = Hangman(managed=False)
	hangman.main()
