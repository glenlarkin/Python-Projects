#! python 3
# kingsWishes.py - Enter into an imaginary village of Kings, you're selling computers
import random
import time

def displayIntro():
    print('''You have found yourself in a wonderful land of Kings, Queens, and Dragons. 
    in front of you, you see two castles.
    In one castle, there is a very nice King who would like to purchase a computer from you.
    The other castle has a medieval king that wants you to be dragon food.''')
print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the castle...')
    time.sleep(2)
    print('It takes quite a while to climb the steps...')
    time.sleep(2)
    print('The knight at the door fetches the king....')
    time.sleep(2)
    print('The King runs out, red in the face, and yells...')
    print()
    time.sleep(2)

    friendlyKing = random.randint(1, 2)

    if chosenCave == str(friendlyKing):
        print('"I want to buy the best model you got with all the storage, teraflops, and everything. \nGIVE IT TO MEEEEE DADDY \nYOU WIN')
    else:
        print("I'M GOING TO UNLEASH THE MOST AWFUL DRAGON ON YOUR SORRY BUTT \nYOU LOSE")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()