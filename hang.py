# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# Mark Addinall - Sept 2015
# MIT Computer Science - Python
#


# test cases for functions 

# print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
# print isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
# print isWordGuessed('grapefruit', ['i', 'z', 's', 'q', 'u', 'w', 'h', 'd', 'r', 'e'])
# print isWordGuessed('grapefruit', ['n', 'c', 'u', 'z', 'x', 't', 's', 'r', 'i', 'g'])
# print isWordGuessed('broccoli', [])

# print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])
# print getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'])
# print getGuessedWord('mangosteen', ['d', 'v', 'e', 'r', 'g', 'c', 'k', 'm', 'h', 'n'])
# print getGuessedWord('mangosteen', ['l', 'd', 'q', 'r', 'e', 'm', 'p', 'b', 'c', 'i'])




import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
                                                # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
                                                # line: string
    line = inFile.readline()
                                                # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''


    guessed = False
    hits    = 0
            
    if lettersGuessed == []:                # nothing guessed,
        return guessed                      # has to be false
                            
    if len(secretWord) == 0:                # should never happen,
        return guessed                      # but if it does, it's false
                                                
    for ch in secretWord:                   # take each character from secret
        if ch in lettersGuessed:            # has it been guessed yet?
              hits += 1                     # yes, how many times?

    if hits == len(secretWord):             # number of characters in
        guessed = True                      # sectret, found in guesses

    return guessed






def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    print_string = []                           # strings immutable, use a list

    if lettersGuessed == []:                    # nothing guessed yet.
        print_string = '_' * len(secretWord) 
        return ' '.join(print_string)           # " _ _ _ _ _ _ _ _ _ _ "
                            
    if len(secretWord) == 0:                    # should never happen, but,
        print_string = 'ERROR'
        return ''.join(print_string)
                                                
    for ch in secretWord:                       # take the secret apart by char
        if ch in lettersGuessed:                # has it been guessed yet?
            print_string.append(ch)             # yes, stick it in place
        else:
            print_string.append(' ')            # no?  Stick in an underscore
            print_string.append('_')            # with some space for usability
            print_string.append(' ')            # " _ dd _ n _ ll"

    return ''.join(print_string)                



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
   
    available = []                               # strings are immutable, use a set
    alphabet = string.ascii_lowercase            # a..z 

    for ch in alphabet:                          # check the whole alphabet
        if ch not in lettersGuessed:             # if it hasn't been guessed,
            available.append(ch)                 # it's available

    return ''.join(available)



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    *   At the start of the game, let the user know how many 
        letters the secretWord contains.

    *   Ask the user to supply one guess (i.e. letter) per round.

    *   After each round, you should also display to the user the 
        partially guessed word so far, as well as letters that the 
        user has not yet guessed.

    *   A user is allowed 8 guesses. Make sure to remind the user of how 
        many guesses s/he has left after each round. Assume that players 
        will only ever submit one character at a time (A-Z).

    *   A user loses a guess only when s/he guesses incorrectly.

    *   If the user guesses the same letter twice, do not take away a guess - 
        instead, print a message letting them know they've already guessed 
        that letter and ask them to try again.

    *   The game should end when the user constructs the full word or runs 
        out of guesses. If the player runs out of guesses (s/he "loses"), 
        reveal the word to the user when the game ends.* The user should 
        receive feedback immediately after each guess 
        about whether their guess appears in the computers word.

    '''

    # print(secretWord)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " characters long")
    print("---------------")

    guesses         = 8
    finished        = False
    won             = False
    guessed_word    = []

    while not finished:

        print("You have " + str(guesses) + " guesses left")

        letters_left = getAvailableLetters(guessed_word)
        print("Available letters: " + letters_left)
        c = raw_input("Please guess a letter: ")
        ch = c.lower()
        if ch in letters_left:
            guessed_word.append(ch)
            if ch in secretWord: 
                print("Good guess: " 
                        + getGuessedWord(secretWord, guessed_word))
            else:
                print("Oops!  That letter is not in my word: "  
                        + getGuessedWord(secretWord, guessed_word))
                guesses -= 1
                if guesses < 1:
                    finished = True
        else:
            print("Oops! You have already guessed that letter:  "
                    + getGuessedWord(secretWord, guessed_word))

        print("---------------")
        if isWordGuessed(secretWord, guessed_word):
            finished = True
            won = True
            break

    if won:
        print("Congratulations, you won!")
    else:
        print"Sorry, you ran out of guesses.  The word was " + secretWord + "."


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist    = loadWords()
secretWord  = chooseWord(wordlist).lower()
hangman(secretWord)




