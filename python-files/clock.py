from datetime import datetime
from time import strftime, sleep
from os import system
import pyttsx3
from art import text2art, tprint

def mega_print(value):
	for _ in range(value):
		print()


def time_main(length=1, language='english', speed=150, vol=1.4, screensaver=False, normal_txt=True):

	if not screensaver:
		#creating an instance of the pyttsx3 object as engine.
		engine = pyttsx3.init()
		#getting the rate property from the engine object. This will let us change the playback speed of tts.
		#rate = engine.getProperty('rate')
		engine.setProperty('rate', speed)
		voices = engine.getProperty('voices')

		def language_change(language):
			engine.setProperty('voice', voices[language].id)

		if language.lower() == 'english':
			language_change(14)
		elif language.lower() == 'french':
			language_change(30)
		elif language.lower() == 'spanish':
			language_change(20)

		volume = engine.getProperty('volume')
		engine.setProperty('volume', volume-vol)

		for _ in range(length):
			text = strftime('%I:%M:%S %p')
			if normal_txt:
				print(text2art(text))
			else:
				tprint(text, font='rnd=xlarge')
			engine.say(text)
			engine.runAndWait()

	else:
		for _ in range(length):
			text = strftime('%I:%M:%S %p')
			mega_print(20)
			if normal_txt:
				print(text2art(text))
			else:
				tprint(text, font='rnd-xlarge')
			sleep(1)
			system('clear')


if __name__ == '__main__':
	time_main(1, language='english', speed=200)
