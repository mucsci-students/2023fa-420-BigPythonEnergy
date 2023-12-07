"""
This script is the view portion of the MVC for the command line interface. It pushes major groups of text or reused text to the controller for output.

- `clearScreen()`: A helper function to clear the CLI screen.
- `entryDisplay()`: Shows the entry text displaying who made the game.
- `mainGameDisplay()`: Shows the display for the main game, giving the puzzle letters, score, and commands.
- `startMenuDisplay()`: Showcases commands for the starting menu.
- `newGameDisplay()`: Gives options to start a game when the start command is given.
- `unrecognizedCommand()`: For when a command is not recognized.
- `helpMenuDisplay()`: Displays the help menu in its entirety.
- `returnGuessing()`: Tells players to press a key to return to guessing after using a command.
- `getWords()`: Prints a list of all found words.

This script acts as the user interface for the Spelling Bee game and coordinates interactions with other modules and game logic.
"""

import os
from typing import Iterable

from prompt_toolkit.document import Document
import Model
import sys
import prompt_toolkit
from prompt_toolkit import prompt
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
import platform

# Class that handles the tab completion.
class CustomCompleter(Completer):
    def __init__(self, completions):
        self.completions = completions

    def get_completions(self, document: Document, complete_event: CompleteEvent) -> Iterable[Completion]:
        wordIn = document.text_before_cursor
        for c in self.completions:
            if c.startswith(wordIn):
                yield Completion(c, start_position= -len(wordIn))

# Clears the screen
def clearScreen():
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system("cls")  # Clear screen on Windows
    else:
        os.system("clear")  # Clear screen on macOS and Linux

# Shows the first entry display.
def entryDisplay():
    print('--------------------------------')
    print('Welcome to Spelling Bee!')
    print('Created by Big Python Energy')
    print('--------------------------------')

# Shows a nice representation of all letters in the puzzle.
def getAllLetters(model):
        letterList = model.getPuzzle().getLetterList()
        allLetters = "| "
        for i in range(6):
            allLetters = allLetters + letterList[i] + " | "
        allLetters = allLetters + letterList[6] + " |"
        return allLetters

# Shows everything needed for the main game functionality.
def mainGameDisplay(model):
    options = ["/words", "/shuffle", "/rank", "/thresholds", "/save", "/quit", "/hints", "/scoreboard", "/addplayer"]
    custom_completer = CustomCompleter(options)
    print('LETTERS:')
    print('-----------------')
    print(getAllLetters(model) + "\n")
    print('Must Contain: ' + model.getPuzzle().getSpecialLetter())
    print('-----------------\n')
    print('Score:')
    print(model.getPuzzle().getCurrentScore())
    print('\nYou may also:\nEnter /words for a list of words, \nEnter /shuffle to shuffle the letters, \nEnter /rank to see your rank, \nEnter /thresholds to see rank thresholds, \nEnter /quit to quit the program, \nEnter /save or /blanksave to save your progress, \nEnter /hints to display all puzzle hints \nEnter /scoreboard to see the scoreboard \nor /addplayer to add yourself to the scoreboard\n')
    opt = prompt("\nEnter your guess below!\n", completer=custom_completer)
    return opt

# Shows the first menu prompt.
def startMenuDisplay():
    print('Please enter "Start" to begin a game, "Help" for a help page, or "Quit" to leave the game.')

# Shows the new game prompt.
def newGameDisplay():
    print('Welcome to the start page, enter "Random" to start from a random word, "Load" to start from a normal save file, "Blank Load" to load from a blank save file, or "Choose" to get started from your own chosen word.')
    print('You may also enter "Back" to go back to the start page')

# States that a command is unrecognzied.
def unrecognizedCommand():
    clearScreen()
    print('Unrecognized command, please try again:')

# Shows the help menu.
def helpMenuDisplay():
    clearScreen()
    print('---------------------------------------------------------------------------------------------------------------------')
    print('Help Page:\n')
    print('This is a spelling bee game, the objective of the game is to spell out at many words as possible.\n')
    print('A word must be at least 4 and at most 15 letters, use only letters from the 7 on screen, and contain a given special letter.')
    print('You can reuse letters as many times as you need to create your word.')
    print('As you find more words, you will get points which correspond to higher ranks.\n')
    print('Points:')
    print('4 Letter word = 1 point. 5 Letter word = 5 points. 6 Letter word = 6 points, and so on.')
    print('Use all 7 letters given = 7 extra points.')
    print('Rank thresholds are based on the total number of words possible.')
    print('---------------------------------------------------------------------------------------------------------------------\n')
    print('Press enter to continue!')

# Prompts the user to press a key to return to guessing.
def returnGuessing():
    print('Press any key to return to guessing.')

# Shows the found words list.
def getWords(model):
    print ('Words found so far:')
    for i in model.getPuzzle().getFoundWordList():
        print (i)

# Creates a textual representation of the bingo and other hints.
def getBingo(model):
    
    bingo = model.getBingoHint()
    column_widths = [max(len(str(item)) for item in col) for col in zip(*bingo)]
    totalWords = bingo[8][13]
    pangramNumbers = model.getPangramNumbers()
    pangramCount = pangramNumbers[0]
    perfectCount = pangramNumbers[1]
    points = model.getPuzzle().getTotalScore()
    
    # Turns the number of words, points, and pangrams in the puzzle into a string.
    returnString = ("Words: " + str(totalWords) + " Points: " + str(points) + " Pangrams: " + str(pangramCount) + " (Perfect: " + str(perfectCount) + ")" + "\n\n")

    # Adds the bingo 2D array to the string.
    for row in bingo:
        returnString = returnString + ("  ".join(str(item).rjust(width) for item, width in zip(row, column_widths))) + "\n"

    # Places all two letter values with 1 or more words into a list and adds them to the string.
    returnString = returnString + ("\n" + "Two Letter List:  ")

    validWords = model.getValidWordList()
    starters = set()
    for word in validWords:
        starter = word[:2]
        starters.add(starter)

    for tup in starters:
        count = model.getEachStartingWith(tup)
        if count != 0:
            returnString = returnString + (str(tup).upper() + ": " + str(count) + "   ")

    return returnString

# Returns the current word display for the score.
def getCurrentScoreType(model):
    percentage = model.getPuzzle().getCurrentScore() / model.getPuzzle().getTotalScore()

    if(percentage == 1):
        return "Queen Bee"
    elif(0.7 <= percentage < 1):
        return "Genius"
    elif(0.5 <= percentage < 0.7):
        return "Amazing"
    elif(0.4 <= percentage < 0.5):
        return "Great"
    elif(0.25 <= percentage < 0.4):
        return "Nice"
    elif(0.15 <= percentage < 0.25):
        return "Solid"
    elif(0.08 <= percentage < 0.15):
        return "Good"
    elif(0.05 <= percentage < 0.08):
        return "Moving Up"
    elif(0.02 <= percentage < 0.05):
        return "Good Start"
    else:
        return "Beginner"
    
# Returns the points needed to get each score.
def getScoreThresholds(model):
    queenBee = "Queen Bee: " + str(model.getPuzzle().getTotalScore())
    genius = "Genius: " + str(int((model.getPuzzle().getTotalScore() * 0.7) + 0.99999999))
    amazing = "Amazing: " + str(int((model.getPuzzle().getTotalScore() * 0.5) + 0.99999999))
    great = "Great: " + str(int((model.getPuzzle().getTotalScore() * 0.4) + 0.99999999))
    nice = "Nice: " + str(int((model.getPuzzle().getTotalScore() * 0.25) + 0.99999999))
    solid = "Solid: " + str(int((model.getPuzzle().getTotalScore() * 0.15) + 0.99999999))
    good = "Good: " + str(int((model.getPuzzle().getTotalScore() * 0.08) + 0.99999999))
    movingUp = "Moving Up: " + str(int((model.getPuzzle().getTotalScore() * 0.05) + 0.99999999))
    goodStart = "Good Start: " + str(int((model.getPuzzle().getTotalScore() * 0.02) + 0.99999999))
    beginner = "Beginner: 0"

    return "Rank thresholds:\n\n" + queenBee + "\n" + genius + "\n" + amazing + "\n" + great + "\n" + nice + "\n" + solid + "\n" + good + "\n" + movingUp + "\n" + goodStart + "\n" + beginner

# Shows a prompt for save encryption.
def getSaveType():
    clearScreen()
    print("Enter 'yes' to save with encryption: ")
    option = input()
    return option
