# Console-Apps
A collection of my python console apps that I have made. You can launch all of them through the --> **manage.py file** <--

**NOTE:** I just want to mention that the best way to experience all of the apps is through the manage.py file because it delivers an interface for launching all the applications. Not only that, but there is also a currency system that launches through manage.py and sort of gameifies the whole experience. You earn tokens by playing games and you can gamble your tokens at the slot machine. I hope to add more gambling features like Blackjack in the future, but slots is the only thing for now. 

**REQURIED:** I highly recommedn that you create a virtual environment within the venv folder to install all of the dependencies. There is already a requirements.txt file inside and a readme that will walk you through the process if you don't know how. I also recommend that you get your own youtube api key from console.developers.google.com and paste it in api-key.txt inside the data folder. You cannot launch the video player app without doing this.

# Applications

**manage.py:** The central hub for launching all of the python applications. Just launch this file through the terminal and it will create an ascii gui that lists and launches all of the console apps. 

**battleship.py:** A single player battlehsip game. The board is randomally generated and you must destroy all 5 of the enemy ships before you run out of ammo. The size is variable and so are the ship sizes. I recommend sticking to the 10 by 10 board or under because the x axis doesn't match up quite right after 10. 

**clock.py:** A really simple clock application that displays the time in cool ascii art characters using the art module and audibally says the time with tts. You can toggle the tts on and off by ediitng the manage.py file and setting the tts argument to False in the time_main function. There is also a clock screensaver mode where you set the number of seconds that you want the time to be displayed. If you set the length argument to 'infinite' in time_main the clock screensaver will go forever.

**dictionary.py:** A simple dictionary application that uses the PyDictionary module. Just look up a word and the dictionary will give you a formatted list of definitions.

**hangman.py:** A single player hangman game that uses a list of 18000+ randomally selected english words for the english_words module. If you do not know the word by the end of the game, the application wil ask if you want to see a definition, and then use the PyDictionary module to retrieve a definition for said word. The art for hangman.py is grabbed for the **hangmanimage.py** file and the words are grabbed from the **words.txt** file in **data** folder. This game is a personal favorite because it is fun and educational.

**slots.py:** A very simple slot machine for spending your tokens. It uses the emoji module for the matching patterns and the only way to win is to get three emojis in a row. You can edit which emojis you want to use by editing the EmojiSlots constructor arguments in manage.py.

**tictactoe.py:** A two player tictactoe game. Like battleship, the board is variable. It is simply a coordinate based tic tac toe game for two players.

**vidplayer.py** This application **REQUIRES** that you have your own youtube api key from console.developers.google.com. An application that uses youtube's api and the vlc media player to link, search, and/or download youtube videos. You can also play videos stored locally on your machine. If you choose to download a video, the program will ask you to name the file and it will be saved inside the videos folder for future use. 

# Other files

**hangmanimage.py:** A file that simply holds an array of ascii art for **hangman.py**.

**youtube.py:** Contains the youtube_search function that is used in **vidplayer.py**. This function is what uses youtube's api to query and create a dictionary of videos with their related video ids.

**welcome.py:** Contains all of the title cards and loading animations used throughout all of the scripts. These cards are customizable and you can change the patterns, message, and colors associated with them. 
 

