#! python3
# This game has the user guess a number between 1 and 20
import random

guessesTaken = 0

print('Hello! What might your name be?')
myName = input().upper()

number = random.randint(1, 20)  #picks a number between the range 1 and 20
print('Okay, ' + myName + ' I want you to guess a number between 1 and 20. \nYou have 6 guesses')

for guessesTaken in range(6):   #gives user 6 guesses
    print('What is the Number I\'m thinking of?')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Sorry amigo, your guess is too low.')

    if guess > number:
        print('My apologies, that guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Sorry ' + myName +', you\'ve used up all of your guesses. The correct answer was ' + number + '.')