import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    c = 1
    for i in secretWord:
        if i in lettersGuessed:
            c += 1
            if len(secretWord) < c:
                return True
        else:
            return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    str1 = ""
    for i in secretWord:
        if i in lettersGuessed:
            str1 += i
        else:
            str1 += "_"
    return str1


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    str1 = ""
    for i in string.ascii_lowercase:
        if i in lettersGuessed:
            str1 = str1
        else:
            str1 += i
    return str1


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord),"letters long.")

    guess = 8
    lg = []
    s = ""
    while True:
        print("-------------")
        if isWordGuessed(secretWord, lg):
            print("Congratulations, you won!")
            break

        if guess > 0:
            print("You have", guess, "guesses left.")
            print("Available Letters:", getAvailableLetters(lg))
            s = (input("Please guess a letter:"))
            if s in lg:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lg))
            elif s in secretWord:
                if s in lg:
                    print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lg))
                else:
                    lg.append(s)
                    print("Good guess:", getGuessedWord(secretWord, lg))

            else:
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord, lg))
                lg.append(s)
                guess-=1

        else:
            print("Sorry, you ran out of guesses. The word was", secretWord,".")
            break


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
