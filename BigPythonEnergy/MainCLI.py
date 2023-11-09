"""
This script is the main entry point for a Spelling Bee game application. It provides various functions and interfaces for users to interact with the game, including selecting game modes (random, load, or choose), starting the game, and displaying a help page.

- `inputCheck()`: The main loop for navigating the application, allowing users to start a game, access the help page, or quit.
- `startPage()`: The screen where users can choose game modes (random, load, choose) or go back to the main screen.
- `randomWord()`: Initializes a new puzzle with a randomly selected word.
- `chooseWord()`: Allows the player to input their own word for the game.
- `helpPage()`: Displays a help page with game instructions and scoring details.

This script acts as the user interface for the Spelling Bee game and coordinates interactions with other modules and game logic.
"""

import os
import re
import json
from Model import Model
from View import View
from MainGameCLI import startGame
import sys

# Main screen loop for getting the user around the application, can go to the start screen, the help screen, or quit the application.
def inputCheck():
    view.getStartingPrompt()
    userInput = input()
    userInput = userInput.lower() # Turns the user input into lower case for easy checking.
    
    if userInput == "start":
        view.clearScreen()
        startPage()
    elif userInput == "help":
        helpPage()
    elif userInput == "quit":
        exit()
    else:
        view.clearScreen()
        view.getUnrecCommPrompt()
        inputCheck()

# Start page where the user can select what type of puzzle they want, or they can go back to the main screen.
def startPage():
    view.getNewGamePrompt()
    userInput = input()
    userInput = userInput.lower() # Turns the user input into lower case for easy checking.

    if userInput == "random":
        randomWord()
        
    # Load the JSON data from the save file.

    elif userInput == "load":
        view.clearScreen()
        print("Please enter the save name to load: ")
        file_selected = input()
        file_path = "BigPythonEnergy/saves/" + file_selected + ".json"
        try:
            with open(file_path, "r") as infile:
                data = json.load(infile)
        except:
            view.clearScreen()
            print("Not a correct filename, try again!")
            startPage()

        else:
            # Access the attributes from the loaded JSON data
            letters = data["baseWord"]
            special_letter = data["requiredLetter"]
            words = data["foundWords"]
            score = data["playerPoints"] 

            model.setPuzzle(letters, special_letter, score, words)
            view.clearScreen()
            print('Loaded save')
            startGame(model, view)

    # Load the JSON data from the blank save file.

    elif userInput == "blank load":
        view.clearScreen()
        print("Please enter the save name of the blank save to load: ")
        file_selected = input()
        file_path = "BigPythonEnergy/blankSaves/" + file_selected + ".json"
        try:
            with open(file_path, "r") as infile:
                data = json.load(infile)
        except:
            print("Not a correct filename, try again!")
            view.clearScreen()
            startPage()

        else:
            # Access the attributes from the loaded JSON data
            letters = data["baseWord"]
            special_letter = data["requiredLetter"]
            words = data["foundWords"]
            score = data["playerPoints"] 

            model.setPuzzle(letters, special_letter, score, words)
            view.clearScreen()
            print('Loaded save')
            startGame(model, view)

    elif userInput == "choose":
        chooseWord()

    elif userInput == "back":
        view.clearScreen()
        inputCheck()
    
    else:
        view.getUnrecCommPrompt()
        startPage()

#Choose word script used if the player wants to choose their own word to base the puzzle off of
def chooseWord():

    view.clearScreen()
    
    print('Enter an english word with at least 7 unique letters.')
    wordInput = input()
    wordInput = wordInput.lower() 

    # checks if the length is atleast 7.
    if len(wordInput)<7:
        view.clearScreen()
        print('Your word does not contain enough letters.')
        chooseWord()

    # Checks if word has any non-English letters.
    elif not re.match("^[a-zA-Z]+$", wordInput): 
        view.clearScreen()
        print('Your word contains non-English letters.')
        chooseWord()
    
    # Checks if the word has exactly 7 unique letters.
    view.clearScreen()
    uniqueCharacters = set()
    for i in wordInput:  
        uniqueCharacters.add(i)
    if len(uniqueCharacters) != 7:
        uniqueCharacters.clear()
        print('Your word does not contain exactly 7 unique characters.')
        chooseWord()
    
    # Checks the dictionary to see if the word is a valid word.
    if model.isValid(wordInput):
        model.setPuzzle(uniqueCharacters)
        startGame(model, view)
    else:
        chooseWord()



# Prints out the help page containing information useful to the player.
def helpPage():
    view.getHelpMenu()
    next = input()
    view.clearScreen()
    inputCheck()

# Function to initialize a new puzzle with a randomly selected word
def randomWord():
    word = model.getRandomWord()
    uniqueCharacters = set()
    for i in word:  
        uniqueCharacters.add(i)
    model.setPuzzle(uniqueCharacters)
    view.clearScreen()
    startGame(model, view)

# Start script to clear the command line so the user just sees the instructions.
model = Model()
view = View()
view.getEntryDisplay()
inputCheck()
