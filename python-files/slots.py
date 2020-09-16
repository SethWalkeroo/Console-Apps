from welcome import title_card, loading_animation
from emoji import emojize
from random import choices
from os import system
from itertools import cycle
from time import sleep
from welcome import title_card


class EmojiSlots:

    def __init__(self, tokens, **emojis):
        self.emoji_values = {f':{str(emoji)}:':value for emoji, value in emojis.items()}
        self.tokens = tokens

    def slot_machine(self, time=30, width=3):
        result = choices([key for key in self.emoji_values], k=3)
        frames = cycle(['|', '/', '-', '\\'])
        for _ in range(time):
            print((next(frames) + ' ') * width)
            sleep(.1)
            system('clear')
        print(emojize('{}'.format(''.join(result)), use_aliases=True))
        return result

    def slot_win(self, result):
        for emoji in result:
            if result.count(emoji) == 3:
                return True, emoji
            else:
                return False, ':sad:'

    def whitespace(self, space):
        for _ in range(space):
            print()

    def main(self):

        title_card('WELCOME TO SLOTS!')
        total_losings = 0
        tokens = self.tokens
        print(f'You currently have {tokens} tokens! Happy gambling!')
        self.whitespace(2)

        print('----- each pull costs 100 tokens -----')
        print()
        command = input('Ready to play? (yes/no): ')
        loading_animation('starting up the slot machine...', time=1)
        if command == 'yes':
            while command != 'no':

                tokens -= 100
                total_losings -= 100
                self.whitespace(2)
                win, winning_emoji = self.slot_win(self.slot_machine())

                if win:
                    winnings = self.emoji_values[winning_emoji]
                    print(f'Holy heck! You won {winnings} tokens!')
                    tokens += winnings
                    total_losings += winnings

                self.whitespace(2)
                print(f'Tokens: {tokens}')
                print()
                command = input('Would you like to give it another whirl? (yes/no): ')
                if command == 'tokens':
                    print(tokens)
                    sleep(2)

                self.whitespace(2)
                system('clear')
        
        if total_losings < 0:
            print(f'Unlucky! Today you lost {total_losings} tokens playing slots! Better luck next time.')
        elif total_losings > 0:
            print(f'Lucky day! Today you won a total of {total_losings} tokens playing slots! See you soon!')
        else:
            print(f'Wow! You broke even playing slots! That\'s not half bad.')
        
        sleep(2)
        title_card('NOW LEAVING SLOTS!')
        sleep(1)
        loading_animation(time=1)

        return total_losings


if __name__ == '__main__':
    #Enter your own emojis and values
    slots = EmojiSlots(tokens=10000, snake=500, eggplant=1000,
                       star=1500,snail=300,angry=200)
    slots.main()
