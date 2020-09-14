from colored import bg, fg, attr
from emoji import emojize
from os import system
from time import sleep
from welcome import title_card, loading_animation
from hangman import Hangman
from tictactoe import toe_main
from dictionary import MyDictionary
from clock import time_main
from vidplayer import video_player_main
from slots import EmojiSlots
from battleship import battleship_main


class Master:

    with open('../data/tokens.txt', 'r') as tokens_txt:
        try:
            current_tokens = int(tokens_txt.read().splitlines()[0])
        except IndexError:
            print()
            print(fg('red') + '** ERROR: Python was unable to retrieve your tokens. Check your "tokens.txt" file and make sure a value exists **' + attr('reset'))
            current_tokens = 0
    #creating an instance of the slots class
    slots = EmojiSlots(tokens=current_tokens, snake=0, eggplant=200,
                    star=500,snail=300,angry=1000)
    # creating instance of the MyDictionary class from dictionary
    dictionary = MyDictionary()
    # creating instance of the Hangman class
    hangman = Hangman()

    # all of my colored variables for ease of use with that module.
    reset = attr('reset')
    fun = fg('dark_green') + bg(16)
    heart = fg('red_3a')
    bold = attr('bold')

    # variables
    apps = {'1': hangman.main, '2': toe_main, '3': dictionary.main,
            '4': video_player_main, '5': time_main, '6': time_main,
            '7':slots.main, '8':battleship_main}

    # function for generating the entire list of applications available in my console applications.
    def app_lst(self):
        title_card('ol/|Hangman/|TicTacToe/|Dictionary/|Video Player/|Clock/|Clock Screensaver/|Slots/|Battleship',
                   msg_color='white', msg_bg_color=16, thickness=2)

    # printing a welcome message using the title_card function from the welcome.py script as well as some emojis from the emoji module.
    # welcome message with list of apps
    def welcome_card_message(self):
        print()
        title_card('Welcome to my Python application suite!',
                   msg_color='white', msg_bg_color=16, ptrn_color='white', thickness=1)
        print(emojize(f'Here is a list of all my {self.fun +"python console applications :snake:" + self.reset} to choose from! Type the application number to launch! :rocket:'))
        print()

    # main function for the sake of organizing somewhat.
    def main(self):
        self.welcome_card_message()
        # This is the main loop that will launch all of the python console scripts.
        while True:
            self.app_lst()
            print()
            print('You have {} tokens in your piggy bank'.format(fg('light_goldenrod_1') + str(self.current_tokens) + attr('reset')))
            # input that chooses which function to run based off user input.
            print()
            print('Type "exit" to exit')
            print()
            try:
                app_choice = input('Choose an application: ')
            except:
                print("That command doesn't exist...")
                continue
            print()
            if app_choice in self.apps:
                system('clear')
                if app_choice == '6':
                    length = int(
                        input('How many seconds would you like to set the screensaver for?: '))
                    self.apps[app_choice](length=length, screensaver=True)
                elif app_choice == '7' and self.current_tokens <= 0:
                    loading_animation(f"Sorry, you need at least 100 tokens to play slots. You have {self.current_tokens} tokens.", time=3)
                elif app_choice == '7':
                    self.current_tokens += self.apps[app_choice]()
                    with open('../Text_files/tokens.txt', 'w') as tokens_txt:
                        tokens_txt.write(str(self.current_tokens))
                else:
                    self.apps[app_choice]()
                system('clear')
            elif app_choice == 'exit':
                break
            elif app_choice == 'restart':
                system('python3 master.py')
            else:
                system('clear')
                print()
                print(emojize(
                    'Oh no! :fearful: that app must not be in the list Try something else.', use_aliases=True))
                print()
                sleep(1.4)
        title_card('Exiting Python application suite!',
            msg_color='white', msg_bg_color=16, ptrn_color='white', thickness=1)
        sleep(1)
        loading_animation((emojize(self.heart + 'goodbye... :broken_heart: :pensive:' +
                      self.reset, use_aliases=True)), time=2)



master = Master()
master.main()
