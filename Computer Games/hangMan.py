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
     ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat foose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pidgeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger roak trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):    #returns a random string from the passed list of strings
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList(wordIndex)

def displayBoard(missedLetters, correctLetters, secretWord):
    print(hangmen[len(missedLetters)])
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):        #Replace blanks with correctly guesses letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1;]

    for letters in blanks:  # Show the secret word with spaces between each letter.
        print(letter, end=' ')
    print()

