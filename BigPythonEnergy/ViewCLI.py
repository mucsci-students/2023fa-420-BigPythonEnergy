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
from Puzzle import *
import sys

def clearScreen():
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system("cls")  # Clear screen on Windows
    else:
        os.system("clear")  # Clear screen on macOS and Linux

def entryDisplay():
    print('--------------------------------')
    print('Welcome to Spelling Bee!')
    print('Created by Big Python Energy')
    print('--------------------------------')

def mainGameDisplay(puzzle):
    print('LETTERS:')
    print('-----------------')
    print(puzzle.getAllLetters() + "\n")
    print('Must Contain: ' + puzzle.specialLetter)
    print('-----------------\n')
    print('Score:')
    print(puzzle.getCurrentScore())
    print ('\nEnter your guess below!\n\nYou may also:\nEnter /words for a list of words, \nEnter /shuffle to shuffle the letters, \nEnter /rank to see your rank, \nEnter /thresholds to see rank thresholds, \nEnter /quit to quit the program, \nEnter /save to save your progress, \nor \nEnter /hints to display all puzzle hints')

def startMenuDisplay():
    print('Please enter "Start" to begin a game, "Help" for a help page, or "Quit" to leave the game.')

def newGameDisplay():
    print('Welcome to the start page, enter "Random" to start from a random word, "Load" to start from a normal save file, "Blank Load" to load from a blank save file, or "Choose" to get started from your own chosen word.')
    print('You may also enter "Back" to go back to the start page')

def unrecognizedCommand():
    clearScreen()
    print('Unrecognized command, please try again:')

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

def returnGuessing():
    print('Press any key to return to guessing.')

def getWords(puzzle):
    print ('Words found:')
    for i in puzzle.getFoundWordList():
        print (i)

def getBingo(puzzle):
    
    bingo = DictInterface.bingoHint(puzzle.getSpecialLetter(), puzzle.getLetters())
    column_widths = [max(len(str(item)) for item in col) for col in zip(*bingo)]
    totalWords = bingo[8][13]
    pangramCount = DictInterface.countPangram(puzzle.getSpecialLetter(), puzzle.getLetters())
    perfectCount = DictInterface.countPangram(puzzle.getSpecialLetter(), puzzle.getLetters())
    points = puzzle.getTotalScore()
    returnString = ("Words: " + str(totalWords) + " Points: " + str(points) + " Pangrams: " + str(pangramCount) + " (Perfect: " + str(perfectCount) + ")" + "\n\n")

    for row in bingo:
        returnString = returnString + ("  ".join(str(item).rjust(width) for item, width in zip(row, column_widths))) + "\n"

    returnString = returnString + ("\n" + "Two Letter List:  ")

    validWords = DictInterface.findValid(puzzle.getSpecialLetter(), puzzle.getLetters())
    starters = set()
    for word in validWords:
        starter = word[:2]
        starters.add(starter)

    for tup in starters:
        count = DictInterface.findStartingWith(tup, puzzle.getLetters(), puzzle.getSpecialLetter())
        if count != 0:
            returnString = returnString + (str(tup).upper() + ": " + str(count) + "   ")

    return returnString