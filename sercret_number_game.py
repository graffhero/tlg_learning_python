# Basic secret number guessing game

import random

guesses = 0

print('Hello puny human! What is your name?')
name = input()

secret = random.randint(1,100)
print(name + ' I am thinking of a number between 1-100.')

while guesses < 9999:
    print('Try your best but you will never guess')
    guess = input()
    guess = int(guess)

    guesses = guesses + 1

    if guess < secret:
        print(guess,  'haha too low, dummy!')

    if guess > secret:
        print(guess, 'mwahaha too high, try again!')

    if guess == secret:
        break
if guess == secret:
    print(name, ',', guess, 'congratulations! You win! Took you long enough!')