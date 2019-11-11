# This program asks a user to state their name and then guess a random number 1-20 in 5 tries
import random

# This section asks for the users name
print('Hi what is your name?')
userName = input()

# This section explains the game to the user
print('Hi ' + userName + '. I am thinking of a number 1 through 20. Can you guess it?')

# This section generates the random number and lets the user guess 5 times
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 6):
	guess = int(input())
	if guess > secretNumber:
		print(str(guess) + ' is too high.')
	elif guess < secretNumber:
		print(str(guess) + ' is too low.')
	else:
		break # Correct guess
	
if guess == secretNumber:
	print('You guessed my number in only ' + str(guessesTaken) + ' tries.')
else:
	print('Wrong! It was ' + str(secretNumber) + '.')
