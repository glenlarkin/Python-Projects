#! python3
import random
hangmen = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 (O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 (O)  |
 /|\  |
 / \  |
     ===''']

words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
'Animals':'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat foose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pidgeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger roak trout turkey turtle weasel whale wolf wombat zebra'.split()
}
def getRandomWord(wordDict):    #returns a random string from the passed dictionary of lists of strings and its key.
    wordKey = random.choice(list(wordDict.keys()))      #First, randomly select a key from the dictionary.
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)    #Second, randomly select a word from the key's list in the dictionary:
    return [wordDict[wordKey][wordIndex], wordKey]
    
def displayBoard(missedLetters, correctLetters, secretWord):    #Incriments through each 6 of the 'hangmen' photos, as a letter is missed
    print(hangmen[len(missedLetters)])
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):        #Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:   # Show the secret word with spaces between each letter.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):   #Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guesssed that letter. Choose Again.')
        elif guess not in 'abcdefghijklmnopqrstuvwwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
        
def playAgain():    #Returns True if the player wants to play again
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')

difficulty = 'X'
while difficulty not in ['E', 'M', 'H']:
    print('Enter Difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()
if difficulty == 'M':
    del hangmen[8]
    del hangmen[7]
if difficulty == 'H':
    del hangmen[8]
    del hangmen[7]
    del hangmen[5]
    del hangmen[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)     #Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess       #Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! the secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters += guess

        if len(missedLetters) == len(hangmen) - 1:   #Check if player has guessed too many times and lost.
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '."')
            gameIsDone = True

    if gameIsDone:  #Catches if the Game is over, and iniates the playAgain function
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
