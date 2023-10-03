import os
import re
from MainGameCLI import *
from puzzle import *
import DictInterface

# Main screen loop for getting the user around the application, can go to the start screen, the help screen, or quit the application.
def inputCheck():
    print('Please enter "Start" to begin a game, "Help" for a help page, or "Quit" to leave the game.') 
    userInput = input()
    userInput = userInput.lower() # Turns the user input into lower case for easy checking.
    
    if userInput == "start":
        startPage()
    elif userInput == "help":
        helpPage()
    elif userInput == "quit":
        exit()
    else:
        os.system('cls')
        print('unrecognized command, please try again:')
        inputCheck()

# Start page where the user can select what type of puzzle they want, or they can go back to the main screen.
def startPage():
    os.system('cls')
    print('Welcome to the start page, enter "Random" to start from a random word, "Load" to start from a save file, or "Choose" to started from your own Chosen word.')
    print('Or enter "Back" to go back to the start page')
    userInput = input()
    userInput = userInput.lower() # Turns the user input into lower case for easy checking.

    if userInput == "random":
        randomWord()
        
    # Load the JSON data from the file.
    elif userInput == "load":
        with open("sample.json", "r") as infile:
            data = json.load(infile)

    # Access the attributes from the loaded JSON data
        letters = data["letters"]
        special_letter = data["specialLetter"]
        words = data["words"]
        score = data["score"]        
        newPuzzle = puzzle(letters)
        newPuzzle.currentScore = score
        newPuzzle.listOfFoundWords = set(words)
        newPuzzle.specialLetter = special_letter
        os.system('cls')
        print('Loaded save')
        startGame(newPuzzle)

    elif userInput == "choose":
        chooseWord()

    elif userInput == "back":
        inputCheck()
    
    else:
        print('unknown command, please enter another')
        startPage()

#Choose word script used if the player wants to choose their own word to base the puzzle off of
def chooseWord():

    os.system('cls')
    
    print('Enter an english word with atleast 7 unique letters')
    wordInput = input()
    wordInput = wordInput.lower() 

    # checks if the length is atleast 7.
    if len(wordInput)<7:
        os.system('cls')
        print('Word does not contain enough letters')
        chooseWord()

    # Checks if word has any non-English letters.
    elif not re.match("^[a-zA-Z]+$", wordInput): 
        os.system('cls') 
        print('Word contains non english letters')
        chooseWord()
    
    # Checks if the word has exactly 7 unique letters.
    os.system('cls')
    uniqueCharacters = set()
    for i in wordInput:  
        uniqueCharacters.add(i)
    if len(uniqueCharacters) != 7:
        uniqueCharacters.clear()
        print('your word does not contain exactly 7 unique characters')
        chooseWord()
    
    # Checks the dictionary to see if the word is a valid word.
    if DictInterface.isValid(wordInput):
        newPuzzle = puzzle(uniqueCharacters)
        startGame(newPuzzle)
    else:
        chooseWord()



# Prints out the help page containing information useful to the player.
def helpPage():
    os.system('cls')
    print('---------------------------------------------------------------------------------------------------------------------')
    print('Help Page:\n')
    print('This is a spelling bee game, the objective of the game is to spell out at many words as possible.\n')
    print('A word must be at least 4 words, use only letters from the 7 on screen, and contain a given special letter.')
    print('You can reuse letters as many times as you need to create your word.')
    print('As you find more words, you will get points which correspond to higher ranks.\n')
    print('Points:')
    print('4 Letter word = 1 point. 5 Letter word = 5 points. 6 Letter word = 6 points, and so on.')
    print('Use all 7 letters given = 7 extra points.')
    print('Rank thresholds are based on the total number of words possible.')
    print('---------------------------------------------------------------------------------------------------------------------\n')
    print('Press enter to continue!')
    next = input()
    os.system('cls')
    inputCheck()

# Function to initialize a new puzzle with a randomly selected word
def randomWord():
    word = DictInterface.randomWord()
    uniqueCharacters = set()
    for i in word:  
        uniqueCharacters.add(i)
    newPuzzle = puzzle(uniqueCharacters)
    startGame(newPuzzle)

# Start script to clear the command line so the user just sees the instructions.
os.system('cls')
print('--------------------------------')
print('Welcome to Spelling Bee!')
print('Created by Big Python Energy')
print('--------------------------------')
inputCheck()


