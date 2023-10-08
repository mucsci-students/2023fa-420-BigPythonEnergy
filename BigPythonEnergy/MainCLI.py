"""
This script is the main entry point for a Spelling Bee game application. It provides various functions and interfaces for users to interact with the game, including selecting game modes (random, load, or choose), starting the game, and displaying a help page.

- `clearScreen()`: A helper function to clear the CLI screen.
- `inputCheck()`: The main loop for navigating the application, allowing users to start a game, access the help page, or quit.
- `startPage()`: The screen where users can choose game modes (random, load, choose) or go back to the main screen.
- `randomWord()`: Initializes a new puzzle with a randomly selected word.
- `chooseWord()`: Allows the player to input their own word for the game.
- `helpPage()`: Displays a help page with game instructions and scoring details.

This script acts as the user interface for the Spelling Bee game and coordinates interactions with other modules and game logic.
"""

import os
import re
import tkinter as tk
from tkinter import filedialog
from MainGameCLI import *
from puzzle import *
from MainUI import *
import DictInterface
import sys
from viewCLI import *

# Main screen loop for getting the user around the application, can go to the start screen, the help screen, or quit the application.
def inputCheck():
    startMenuDisplay() 
    userInput = input()
    userInput = userInput.lower() # Turns the user input into lower case for easy checking.
    
    if userInput == "start":
        startPage()
    elif userInput == "help":
        helpPage()
    elif userInput == "quit":
        exit()
    else:
        clearScreen()
        unrecognizedCommand()
        inputCheck()

# Start page where the user can select what type of puzzle they want, or they can go back to the main screen.
def startPage():
    clearScreen()
    newGameDisplay()
    userInput = input()
    userInput = userInput.lower() # Turns the user input into lower case for easy checking.

    if userInput == "random":
        randomWord()
        
    # Load the JSON data from the file.

    ##This is broken now, please fix
    elif userInput == "load":
        root = tk.Tk()
        root.withdraw()
        file_selected = filedialog.askopenfile()
        print("")
        print(file_selected.name)
        print("")
        with open(file_selected.name, "r") as infile:
            data = json.load(infile)

    # Access the attributes from the loaded JSON data
        letters = data["baseWord"]
        special_letter = data["requiredLetter"]
        words = data["foundWords"]
        score = data["playerPoints"] 

        newPuzzle = puzzle(letters)
        newPuzzle.currentScore = score
        newPuzzle.listOfFoundWords = set(words)
        newPuzzle.specialLetter = special_letter
        clearScreen()
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

    clearScreen()
    
    print('Enter an english word with atleast 7 unique letters')
    wordInput = input()
    wordInput = wordInput.lower() 

    # checks if the length is atleast 7.
    if len(wordInput)<7:
        clearScreen()
        print('Word does not contain enough letters')
        chooseWord()

    # Checks if word has any non-English letters.
    elif not re.match("^[a-zA-Z]+$", wordInput): 
        clearScreen()
        print('Word contains non english letters')
        chooseWord()
    
    # Checks if the word has exactly 7 unique letters.
    clearScreen()
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
    helpMenuDisplay()
    next = input()
    clearScreen()
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
if str(len(sys.argv) > 1 and sys.argv[1]) == "--gui":
    exec(open("BigPythonEnergy/MainUI.py").read())
entryDisplay()
inputCheck()
