# Hangman game


import random

WORDLIST_FILENAME = "movies.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    #line = inFile.readline()
    # wordlist: list of strings
    '''
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
    '''
    wordlist=[]
    for line in inFile:
        wordlist.append(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist
    x.close()
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
    l=[]
    for i in secretWord:
        l.append(i)
    if l in lettersGuessed:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
 

    x=""
    for i in range(len(secretWord)-1):
        if secretWord[i] in lettersGuessed:
            x=x+secretWord[i]
        elif secretWord[i]==" ":
            x=x+"  "
        else:
            x=x+"_ "
    return x



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    x="abcdefghijklmnopqrstuvwxyz0123456789"
    y=""
    for i in x:
        if i in lettersGuessed:
            pass
        else:
            y=y+i
    return y
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    '''
    t=time.time()
    Graphics =['''_____\n|/  |\n|   O\n|  /|\\\n|  / \\\n|''',
    '''_____\n|/\n|   O\n|  /|\\\n|  / \\\n|''',
    '''_____\n|/\n|   O\n|  /|\\\n|  /\n|''',
    '''_____\n|/\n|   O\n|  /|\\\n|\n|''',
    '''_____\n|/\n|   O\n|  /|\n|\n|''',
    '''_____\n|/\n|   O\n|   |\n|\n|''',
    '''_____\n|/\n|   O\n|\n|\n|''',
    '''_____\n|/\n|\n|\n|\n|''',""
    ]
    temp=[]
    
   
    for i in secretWord:
            if i.isalnum():
                temp.append(i)
    chances=8
    print("The length of the word you have to guess is (Including white spaces if any):",len(secretWord)-1)
    import string
    f=[]
    
    for i in secretWord:
        if i in (string.ascii_lowercase or string.ascii_uppercase or string.digits):
            f.append("_ ")
        else:
            f.append("  ")
    print("".join(f))
    lettersGuessed=[]
    while not(isWordGuessed(secretWord, lettersGuessed)):
        guess=input("Enter a suitable character: ")
        guess=guess.lower()
        while guess not in ("abcdefghijklmnopqrstuvwqyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890") or guess not in(getAvailableLetters(lettersGuessed)):
            print("\nYou have entered an invalid character or a character that you have already guessed!")
            guess=input("Kindly enter another suitable character: ")
        lettersGuessed.append(guess)
        if guess not in secretWord:
            chances=chances-1
            
        if chances==0:
            print("Game over!")
            print("The word that was to be guessed: \n\t",secretWord.upper(),"\n")
            print("\nGame Stats:\nIncorrect guesses: ",(8-chances),"\nLetters unused: ",(getAvailableLetters(lettersGuessed)))
            break
        #print(getGuessedWord(secretWord, lettersGuessed))
        temp1=[]
        
        for i in getGuessedWord(secretWord, lettersGuessed):
            if i.isalnum():
                temp1.append(i)
                
        #check if full word is guessed        
        if temp == temp1 :
            print("                             ----------------------")
            print("------------------------Congratulations!!!------------------------")
            print("                             ----------------------")
            print("\n\nYou have been successful in guessing this movie:  ",secretWord.title())
            print("\nGame Stats:\nIncorrect guesses: ",(8-chances),"\nLetters unused: ",(getAvailableLetters(lettersGuessed)))
            print("Time played for: ",time.time()-t," seconds")
            break
        
        print("\n")
        print(Graphics[chances])
        print("\n")
        print("\nGuesses left: ",chances,"\nThe letters you have not guessed so far are: ",(getAvailableLetters(lettersGuessed)).split(","))
        print("\n"*2)
        for d in range(60):
            print("-X-",end="")
        print("\n"*2)
        print(getGuessedWord(secretWord, lettersGuessed))
        
        
    
    
#main block where function gets called
counter=True
while counter:
    figlet="""
    _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/
    """
    print(figlet)
    print("Loading Game Environment. Please Wait ",end="")
    import time
    
    for t in range(6):
        print(". ",end="")
        time.sleep(0.5)
    print("   Load Completed")
    print("\n"*3)
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
    counter_choice=input("Do you want to play another round of hangman ??!    (y/n)")
    while counter_choice not in ["y","n","Y","N"]:
        counter_choice=input("Kindly enter only y or n !")
    if counter_choice=="y" or counter_choice=="Y":
        counter=True
    else:
        counter=False
        
