#  game2.py
#  vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#  Mark Addinall - September 2015
#  MIT Computer Science - Python
# 
# INTRODUCTION - A WORD GAME
# 
# This is essentially the same as game1.py, with one significant difference. 
# Instead of the human playing the game, we program the computer to do so
# as well.  We give the player a choice of human or machine play.  That
# way the hooman can pit skill against a brute force algorithm
# which is a pretty bloody hard ask.
#
# This game is a lot like Scrabble or Words With Friends, if you've played those. Letters are dealt to players, who then construct one or more words out of their letters. Each valid word receives a score, based on the length of the word and the letters in that word.
# 
# The rules of the game are as follows:
# 
# Dealing
# A player is dealt a hand of n letters chosen at random (assume n=7 for now).
# 
# The player arranges the hand into as many words as they want out of the letters, using each letter at most once.
# 
# Some letters may remain unused (these won't be scored).
# 
# Scoring
# The score for the hand is the sum of the scores for each word formed.
# 
# The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.
# 
# Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.
# 
# For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!
# 
# As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).
# 
# Sample Output
# 
# Here is how the game output will look!
# 
# Loading word list from file...
#    83667 words loaded.
#    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
#    Current Hand: p z u t t t o
#    Enter word, or a "." to indicate that you are finished: tot
#    "tot" earned 9 points. Total: 9 points
#    Current Hand: p z u t
#    Enter word, or a "." to indicate that you are finished: .
#    Total score: 9 points.
# 
#    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
#    Current Hand: p z u t t t o
#    Enter word, or a "." to indicate that you are finished: top
#    "top" earned 15 points. Total: 15 points
#    Current Hand: z u t t
#    Enter word, or a "." to indicate that you are finished: tu
#    Invalid word, please try again.
#    Current Hand: z u t t
#    Enter word, or a "." to indicate that you are finished: .
#    Total score: 15 points.
# 
#    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
#    Current Hand: a q w f f i p
#    Enter word, or a "." to indicate that you are finished: paw
#    "paw" earned 24 points. Total: 24 points
#    Current Hand: q f f i
#    Enter word, or a "." to indicate that you are finished: qi
#    "qi" earned 22 points. Total: 46 points
#    Current Hand: f f
#    Enter word, or a "." to indicate that you are finished: .
#    Total score: 46 points.
# 
#    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
#    Current Hand: a r e t i i n
#    Enter word, or a "." to indicate that you are finished: inertia
#    "inertia" earned 99 points. Total: 99 points
#    Run out of letters. Total score: 99 points.
# 
#    Enter n to deal a new hand, r to replay the last hand, or e to end game: e
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7                               # number of tiles in the hand.  Can change
                                            # BUT only on this line of code!

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"



#
#--------------
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."

    inFile = open(WORDLIST_FILENAME, 'r', 0)    # inFile: file
   
    wordList = []                               # wordList: list of strings
    for line in inFile:                         # read file sequentially
        wordList.append(line.strip().lower())   # append to dictionary after lowering case
    print "  ", len(wordList), "words loaded."  # screen fluff
    return wordList                             # send it into the game


#
#------------------------------
def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
   
    freq = {}                                   # freqs: dictionary (element_type -> int)
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	


#
#-------------------------
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """

    score = 0                                   # total word scrore
    count = 0                                   # word length

    for ch in word:                             # take word apart
        score += SCRABBLE_LETTER_VALUES[ch]     # fetch the key: value from dict
        count += 1                              # keep track of word length

    score *= count                              # multiply score by word lenght
    if count == n:                              # and add additional bonus if
        score += 50                             # entire hand is used

    return score                                # and send it back to caller



#
#---------------------
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line



#
#--------------
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand



#
#--------------------------
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    new_hand = hand.copy()              # under instructions NOT to mutate
                                        # the object coming in
    for ch in word:                     # take word apart
        new_hand[ch] -= 1               # decrease occurance count

    return new_hand                     # and return the new dictionary





#
#------------------------------------
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    cards_left = hand.copy()                # do not want to mutate the object in
    valid = True                            # assume a valid word for now
    if word in wordList:                    # is the word in the valid LIST of words?
        for ch in word:                     # if so, take the word apart
            if not ch in cards_left or cards_left[ch] == 0:        
                                            # do we actually hold the card in  
                                            # our hand? This code is for multiple
                valid = False               # use of the same char "booboo"
                break                       # if not, fail and return
            else:
                cards_left[ch] -= 1         # remove the card from our hand
    else:
        valid = False                       # not even a real word, fail

    return valid                            # and return validity of the word`




#
#-------------------------
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """

    cards = 0                               # we can get an empty hand
    for card in hand:                       # iterate pver the keys 'a'...'z'
        cards += hand[card]                 # and count the cards!
    return cards                            # send back the hand size`



#
#-------------------------------
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    score = 0                                       # Keep track of the total score
    cards_left = calculateHandlen(hand)             # dope initial hand size

    while cards_left > 0:                           # As long as there are still letters 
                                                    # left in the hand:
        print('Current Hand: '),                    # display title
        displayHand(hand)                           # Display the hand
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if word == '.':                             # If the input is a single period:
            break                                   # End the game (break out of the loop)
        else:                                       # Otherwise (the input is not a single period):
            if not isValidWord(word, hand, wordList):           
                                                    # If the word is not valid:
                print("Invalid word, please try again")
                                                    # Reject invalid word (print a message 
                print                               # followed by a blank line)
            else:                                   # Otherwise (the word is valid):
                wscore = getWordScore(word, n)      # get the score for the word
                score += wscore                     # update the total
                print('"'+word+'"'+" earned "),     # Tell the user how many points the word earned, 
                print(str(wscore)+" points. "),     # and the updated total score, in one line 
                print("Total: "+str(score)),
                print(" points")
                print                               # followed by a blank line
                hand = updateHand(hand, word)       # Update the hand 
                cards_left = calculateHandlen(hand) # dope resultant hand size
                                                    # this can end the hand when
                                                    # cards left becomes zero
    if word == '.':                                 # Game is over (user entered a '.' or ran out of letters), 
        msg = 'Goodbye! '                           # so tell user the total score
    else:                                           # slightly different message based on
        msg = 'Run out of letters. '                # hand exit status

    print(msg + 'Total score: ' + str(score) + ' points.')



#
#-------------------------------------
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    highest_score = 0                   # Create a new variable to store the maximum 
                                        # score seen so far (initially 0)
    best_word = None                    # Create a new variable to store the best word 
                                        # seen so far (initially None)  

    for word in wordList:                       # For each word in the wordList
        if isValidWord(word, hand, wordList):   # If you can construct the word from the hand
            score = getWordScore(word, n)       # Find out how much making that word is worth
            if score > highest_score:           # If the score for that word is higher than 
                                                # the best score
                highest_score = score           # Update the best score,
                best_word = word                # and best word accordingly

    return best_word                    # return the best word found.





#
#----------------------------------
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """

    score = 0                                       # Keep track of the total score
    cards_left = calculateHandlen(hand)             # dope initial hand size

    while cards_left > 0:                           # As long as there are still letters 
                                                    # left in the hand:
        print('Current Hand: '),                    # display title
        displayHand(hand)                           # Display the hand
        word = compChooseWord(hand, wordList, n)    # computer fetches best word so far
        if word == None:                            # If the input is a single period:
            break                                   # End the game (break out of the loop)
        else:                                       # Otherwise 
            wscore = getWordScore(word, n)          # get the score for the word
            score += wscore                         # update the total
            print('"'+word+'"'+" earned "),         # Display how many points the word earned, 
            print(str(wscore)+" points. "),         # and the updated total score, in one line 
            print("Total: "+str(score)),
            print(" points")
            print                                   # followed by a blank line
            hand = updateHand(hand, word)           # Update the hand 
            cards_left = calculateHandlen(hand)     # dope resultant hand size
                                                    # this can end the hand when
                                                    # cards left becomes zero

    print('Total score: ' + str(score) + ' points.')




# 
#---------------------
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
       * If the user inputs 'e', immediately exit the game.
       * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
       * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
       * If the user inputted 'n', play a new (random) hand.
       * Else, if the user inputted 'r', play the last hand again.
                               
       * If the user inputted 'u', let the user play the game
         with the selected hand, using playHand.
       * If the user inputted 'c', let the computer play the 
         game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)

    """

    finished = False                                # just the game controller
    last_hand = {}                                  # empty set to save the soon to be current game
    while not finished:                             # loop forever
        ch = ''                                     # empty the input character
        while ch not in ['n','r','e']:              # (n)ew, (r)replay, (e)nd
            ch = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            if ch == 'r':                           # wants to replay eh?
                if last_hand == {}:                 # can't, haven't played yet
                    print("You have not played a hand yet.  Please play a new hand first!")
                    ch = ''                         # reset input character
                    print                           # output blank line and try again
                else:
                    hand = last_hand.copy()         # let them play THIS game again
            elif ch == 'e':
                finished = True                     # wants to quit
            elif ch == 'n':
                hand = dealHand(HAND_SIZE)          # new game, get a hand
            else:
                print("Invalid command.")           # dumb keypress, try again

        if not finished:
            ch = ''                                 # empty the input character
            while ch not in ['u','c']:              # user or computer
                ch = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if ch not in ['u','c']:
                    print("Invalid command")

            if ch == 'u':                           # people game    
                playHand(hand, wordList, HAND_SIZE)
            else:                                   # machine game
                compPlayHand(hand, wordList, HAND_SIZE)
            last_hand = hand.copy()                 # and save the game in case the player
                                                    # wants to have another shot with the
                                                    # same cards


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
#-----EOF------------------------------

