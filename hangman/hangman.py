from tkinter import *
from PIL import ImageTk, Image
import random
import math
import string
from tkinter import messagebox


root = Tk()
root.title("Hangman!")
root.geometry("636x327+477+257")

try:
    root.wm_iconbitmap('F:hangman\Image\image_100Noor.ico')
except TclError:
    pass
global ImageLabel

my_image0 = ImageTk.PhotoImage(Image.open("F:\hangman\Image\pic0.png"))
my_image1 = ImageTk.PhotoImage(Image.open("F:\hangman\Image\pic1.png"))
my_image2 = ImageTk.PhotoImage(Image.open("F:\hangman\Image\pic2.png"))
my_image3 = ImageTk.PhotoImage(Image.open("F:\hangman\Image\pic3.png"))
my_image4 = ImageTk.PhotoImage(Image.open("F:\hangman\Image\pic4.png"))
my_image5 = ImageTk.PhotoImage(Image.open("F:\hangman\Image\pic5.png"))
my_image6 = ImageTk.PhotoImage(Image.open("F:\hangman\Image\pic6.png"))
my_image7 = ImageTk.PhotoImage(Image.open("F:\hangman\Image\pic7.png"))
ImageLabel = Label(image=my_image0)
ImageLabel.place(relx=0.016, rely=0.061)

image_list = [my_image0, my_image1, my_image2, my_image3, my_image4, my_image5, my_image6, my_image7]

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

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
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
    str1 = ""
    for i in secretWord:
        if i in lettersGuessed:
            str1 += i
        else:
            str1 += "_ "
    return str1


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str1 = ""
    for i in string.ascii_lowercase:
        if i in lettersGuessed:
            str1 = str1
        else:
            str1 += i
    return str1


def ImageShowing(n):
    global ImageLabel
    my_image = ImageTk.PhotoImage(Image.open("Image\pic"+str(n)+".png"))
    ImageLabel = Label(image=image_list[n])
    ImageLabel.place(relx=0.016, rely=0.061)


def Click(ch):

    try:
        c = ch.lower()
        secret = secretWord[:]

        if isWordGuessed(secret, lg) == True:
            Result_Screen = Label(root, text="Congratulations, you won!", padx=5, pady=5, background="#ffffff").place(relx=0.503, rely=0.428, height=31, width=244)
        else:
            if c in secret:
                if c in lg and len(lg) > 0:
                    Result_Screen = Label(root, text="Oops! You've already guessed that letter", padx=5, pady=5, background="#ffffff").place(relx=0.503, rely=0.428, height=31, width=244)
                else:
                    lg.append(c)
                    Play_Screen = Label(root, text=getGuessedWord(secretWord, lg).upper(),foreground="White" ,background="#424242", font=("the times roman", 15)).place(relx=0.44, rely=0.092, height=71, width=334)
                    Result_Screen = Label(root, text="Good guess!", padx=5, pady=5, background="#ffffff").place(relx=0.503, rely=0.428, height=31, width=244)
                    if isWordGuessed(secret, lg) == True:
                        Result_Screen = Label(root, text="Congratulations, you won!", padx=5, pady=5, background="#ffffff").place(relx=0.503, rely=0.428, height=31, width=244)
            elif c in lg :
                Result_Screen = Label(root, text="Oops! You've already guessed that letter", padx=5, pady=5, background="#ffffff").place(relx=0.503, rely=0.428, height=31, width=244)
            else:
                Result_Screen = Label(root, text="Oops! That letter is not in my word", padx=5, pady=5, background="#ffffff").place(relx=0.503, rely=0.428, height=31, width=244)
                lg.append(c)
                guess.append(1)
                n = len(guess)
                if n < 7 and n > 0:
                    ImageShowing(n)

                if n == 7:
                    my_image = ImageTk.PhotoImage(Image.open("Image\pic7.png"))
                    ImageLabel = Label(image=my_image)
                    ImageLabel.place(relx=0.016, rely=0.061)
                    guessLbl = Label(root, text= "Guess: "+ str(n))
                    guessLbl.place(relx=0.456, rely=0.856, height=31, width=94)
                    msg = "The word was ''"+ secret + "''. " + "Play Again?"
                    response = messagebox.askyesno("Sorry, you ran out of guesses.", msg)
                    if response == True:
                        Play()
                    else:
                        root.quit()
        guessLbl = Label(root, text= "Guess: "+ str(n))
        guessLbl.place(relx=0.456, rely=0.856, height=31, width=94)
    except NameError:
        pass


def Play():
    global secretWord
    global lg
    global guess
    lg = []
    guess = []
    secretWord = chooseWord(wordlist).lower()
    n = "I am thinking of a word that is "+ str(len(secretWord)) + " letters long."
    Result_Screen = Label(root, text=n, padx=5, pady=5, background="#ffffff").place(relx=0.503, rely=0.428, height=31, width=244)
    Play_Screen = Label(root, text=getGuessedWord(secretWord, lg),foreground="White" ,background="#424242", font=("the times roman", 15)).place(relx=0.44, rely=0.092, height=71, width=334)

Result_Screen = Label(root, text="", padx=10, pady=10, background="#ffffff")
Result_Screen.place(relx=0.503, rely=0.428, height=31, width=244)

Play_Screen = Label(root, text="Welcome to the game, Hangman!",foreground="White" ,background="#424242", font=("the times roman", 15)).place(relx=0.44, rely=0.092, height=71, width=334)

btnA = Button(root, text="A", command=lambda:Click("A")).place(relx=0.44,  rely=0.581, height=24, width=29)
btnB = Button(root, text="B", command=lambda:Click("B")).place(relx=0.487, rely=0.581, height=24, width=29)
btnC = Button(root, text="C", command=lambda:Click("C")).place(relx=0.535, rely=0.581, height=24, width=29)
btnD = Button(root, text="D", command=lambda:Click("D")).place(relx=0.582, rely=0.581, height=24, width=29)
btnE = Button(root, text="E", command=lambda:Click("E")).place(relx=0.629, rely=0.581, height=24, width=29)
btnF = Button(root, text="F", command=lambda:Click("F")).place(relx=0.676, rely=0.581, height=24, width=29)
btnG = Button(root, text="G", command=lambda:Click("G")).place(relx=0.723, rely=0.581, height=24, width=29)
btnH = Button(root, text="H", command=lambda:Click("H")).place(relx=0.77,  rely=0.581, height=24, width=29)
btnI = Button(root, text="I", command=lambda:Click("I")).place(relx=0.818, rely=0.581, height=24, width=29)
btnJ = Button(root, text="J", command=lambda:Click("J")).place(relx=0.865, rely=0.581, height=24, width=29)
btnK = Button(root, text="K", command=lambda:Click("K")).place(relx=0.912, rely=0.581, height=24, width=29)
btnL = Button(root, text="L", command=lambda:Click("L")).place(relx=0.44,  rely=0.673, height=24, width=29)
btnM = Button(root, text="M", command=lambda:Click("M")).place(relx=0.487, rely=0.673, height=24, width=29)
btnN = Button(root, text="N", command=lambda:Click("N")).place(relx=0.535, rely=0.673, height=24, width=29)
btnO = Button(root, text="O", command=lambda:Click("O")).place(relx=0.582, rely=0.673, height=24, width=29)
btnP = Button(root, text="P", command=lambda:Click("P")).place(relx=0.629, rely=0.673, height=24, width=29)
btnQ = Button(root, text="Q", command=lambda:Click("Q")).place(relx=0.676, rely=0.673, height=24, width=29)
btnR = Button(root, text="R", command=lambda:Click("R")).place(relx=0.723, rely=0.673, height=24, width=29)
btnS = Button(root, text="S", command=lambda:Click("S")).place(relx=0.77, rely=0.673, height=24, width=29)
btnT = Button(root, text="T", command=lambda:Click("T")).place(relx=0.818, rely=0.673, height=24, width=29)
btnU = Button(root, text="U", command=lambda:Click("U")).place(relx=0.865, rely=0.673, height=24, width=29)
btnV = Button(root, text="V", command=lambda:Click("V")).place(relx=0.912, rely=0.673, height=24, width=29)
btnW = Button(root, text="W", command=lambda:Click("W")).place(relx=0.582, rely=0.765, height=24, width=29)
btnX = Button(root, text="X", command=lambda:Click("X")).place(relx=0.629, rely=0.765, height=24, width=29)
btnY = Button(root, text="Y", command=lambda:Click("Y")).place(relx=0.676, rely=0.765, height=24, width=29)
btnZ = Button(root, text="Z", command=lambda:Click("Z")).place(relx=0.723, rely=0.765, height=24, width=29)


btnPlay = Button(root, text="Play", command=lambda: Play()).place(relx=0.645, rely=0.856, height=24, width=43)
btnExit = Button(root, text="<Exit>", command=root.quit).place(relx=0.786, rely=0.856, height=24, width=56)

guessLbl = Label(root, text="Guess: ", background="#ffffff")
guessLbl.place(relx=0.456, rely=0.856, height=31, width=94)

root.mainloop()
