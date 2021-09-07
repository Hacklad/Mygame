import random

start_game = input('***** Would you like to start Number Guessers? 1) Start 2) Exit ***** ')
if start_game.isdigit():
	start_game = int(start_game)
	if start_game == 1:
		print('. (Opening...........................). ')
	elif start_game == 2: 
		exit()
else:
	print('Enter a number greater than zero next time')
	exit()

guesses = 0

print(' -------------> Welcome to the Number Island <---------------')
your_range = input('Enter the max nummber you would like to guess from 1? ')
if your_range.isdigit():	
	your_range = int(your_range)
	if your_range > 1:
		correct_number = random.randrange(1, your_range)
	else:
		print('=== Enter a number above zero and one next time ===')
		exit()

while True:
	guesses += 1
	your_guess = input('Now guess the number in my mind? ')
	if your_guess.isdigit():
			your_guess = int(your_guess)
	else:
		print('Type a number next time!')
		continue
	
	if correct_number == your_guess:
		print('You got the right answer in ', guesses, 'guesses')
		break
	elif correct_number < your_guess:
		print('Opps, that number is larger than my Number. Try again!')
	else:
		print('Ooops, That number is smaller than my Number, Try again!')
print('========== Grats!!! Nice one, You are the real MVP. =========')
	