from colored import bg, fg, attr
from emoji import emojize
from os import system, stat, listdir, path
from time import sleep
import sys
import json

apps_folder = (path.abspath('apps/'))
sys.path.append(path.abspath(apps_folder))
# sys.path.append(path.abspath(entry))

from welcome import title_card, loading_animation
from hangman import Hangman
from tictactoe import toe_main
from dictionary import MyDictionary
from clock import time_main
from vidplayer import video_player_main
from slots import EmojiSlots
from battleship import battleship_main
from compinfo import ComputerInformation
from login import LoginSystem
from life import life_main

# main function for the sake of organizing somewhat.
def main():

    account_path = 'data/user-info.json'
    login = LoginSystem(account_path)
    username, current_tokens = login.account_main()

    #creating an instance of the slots class
    slots = EmojiSlots(tokens=current_tokens, snake=0, eggplant=200,
                    star=500,snail=300,angry=1000)
    # creating instance of the MyDictionary class from dictionary
    dictionary = MyDictionary()
    # creating instance of the Hangman class
    hangman = Hangman()
    #instance of computerinformation class
    computer_info = ComputerInformation()

    # all of my colored variables for ease of use with that module.
    reset = attr('reset')
    fun = fg('dark_green') + bg(16)
    bye_color = fg('white')
    bold = attr('bold')
    token_clr = fg('light_goldenrod_1')

    # variables
    apps = {'1': hangman.main, '2': toe_main, '3': dictionary.main,
            '4': video_player_main, '5': time_main, '6': time_main,
            '7': slots.main, '8': battleship_main, '9': computer_info.main,
            '10': life_main,}

    token_gain = 0

    # function for generating the entire list of applications available in my console applications.
    def app_lst():
        title_card('ol,Hangman,TicTacToe,Dictionary,Video Player,Clock,Clock Screensaver,Slots,Battleship,PC Specs and Info,Conway\'s Game of Life',
                    msg_color='white', msg_bg_color=16, thickness=2)

    def token_update(value):
        path = account_path
        with open(path, 'r') as user_info:
            data = json.load(user_info)
        with open(path, 'w') as user_info:
            data['users'][username]['tokens'] = str(current_tokens + value)
            json.dump(data, user_info)
        return value

    def api_key_check():
        if stat('data/api-key.txt').st_size == 0:
            print('It looks like you haven\'t added your youtube api key.')
            print('The youtube api key is required for the video player app.')
            print()
            add_key = input('Would you like to add your key? (yes/no): ')
            if add_key == 'yes':
                loading_animation(time=1)
                api_key = input('Enter key here: ')
                with open('data/api-key.txt', 'w') as f:
                    f.write(api_key)
                return True
            else:
                return False
        else:
            return True

    # printing a welcome message using the title_card function from the welcome.py script as well as some emojis from the emoji module.
    # welcome message with list of apps
    def welcome_card_message():
        print()
        title_card(f'Welcome {username}!',
                    msg_color='white', msg_bg_color=16, ptrn_color='white', thickness=1)
        print(emojize(f'Here is a list of all my {fun +"python console applications :snake:" + reset} to choose from! Type the application number to launch! :rocket:'))
        print()

    welcome_card_message()
    # This is the main loop that will launch all of the python console scripts.
    while True:
        current_tokens_str = token_clr + bold + str(current_tokens) + reset
        token_gain_str = token_clr + str(token_gain) + reset
        if token_gain > 0:
            print(f"** You earned {token_gain_str} tokens! **")
        elif token_gain < 0:
            print(f'** You lost {token_gain_str} tokens! **')
        print()
        app_lst()
        print()
        print('You have {} tokens in your token vault'.format(current_tokens_str))
        print()
        print()
        print('Type "exit" to exit')
        print()
        try:
            app_choice = input('Choose an application: ')
        except:
            print("That command doesn't exist...")
            continue
        print()
        if app_choice in apps:
            system('clear')
            if app_choice == '6':
                length = int(input('How many seconds would you like to set the screensaver for?: '))
                apps[app_choice](length=length, screensaver=True)
            elif app_choice == '5':
                apps[app_choice]()
            elif app_choice == '4':
                loading_animation(time=1)
                if api_key_check():
                    loading_animation('Youtube api key detected. Enjoy the video player!', time=1)
                    apps[app_choice]()
                    token_gain = token_update(150)
                    current_tokens += token_gain
                else:
                    loading_animation('Returning to menu...', time=1)
            elif app_choice == '7' and current_tokens <= 0:
                loading_animation(f"Sorry, you need at least 100 tokens to play slots. You have {current_tokens} tokens. Launch apps to earn more tokens.", time=3)
            elif app_choice == '7':
                token_gain = token_update(apps[app_choice]())
                current_tokens += token_gain
            else:
                apps[app_choice]()
                token_gain = token_update(150)
                current_tokens += token_gain
            system('clear')
        elif app_choice == 'exit':
            break
        elif app_choice == 'restart':
            system('python3 master.py')
        else:
            system('clear')
            print()
            loading_animation(emojize('Oh no! :fearful: that app must not be in the list Try something else.', use_aliases=True), time=2)
    system('clear')
    title_card(f'Exiting console applications!',
        msg_color='white', msg_bg_color=16, ptrn_color='white', thickness=1)
    sleep(.75)
    loading_animation((emojize(bye_color + f'Goodbye {username}! :wave:' +
                    reset, use_aliases=True)), time=2)


if __name__ == '__main__':
    main()
