"""
This script is the core of a Spelling Bee game application, handling the main game loop and player interactions.

    - `startGame(puzzle)`: The main game loop where players enter guesses, manage the game, and interact with various game commands.
    - Allows players to guess words, save their progress, view found words, shuffle letters, check their rank, and see rank thresholds.
    - Validates guesses based on length, letter availability, and the presence of a special letter.
    - Awards points for valid guesses and updates the game state accordingly.
    - Handles various in-game commands like quitting, saving, and displaying information.
    - Provides feedback on the correctness of guesses and updates the player's score.

This script integrates game logic with player interactions, making it the central component of the Spelling Bee game.
"""

import os
import random
import re
import json
from Puzzle import *
import DictInterface
from ViewCLI import *

# The main game loop, which contains each action a player can make and calls upon the underlying structure.
# Prerequesite: Must run until stopped.
def startGame(puzzle):
    
    mainGameDisplay(puzzle)
    guess = input()
    guess = guess.lower()

    # Stops the program.
    if guess == "/quit":
        exit()

    # Saves the game data to the save file.
    if guess == "/save":
        save = {
            "baseWord":list(puzzle.letterList),
            "foundWords" : list(puzzle.getFoundWordList()),
            "playerPoints": puzzle.getCurrentScore(),
            "requiredLetter":puzzle.specialLetter,
            "maxPoints": puzzle.totalScore
        }
        print('Enter Name for Save File:')
        fileName = input()
        
        with open(fileName+".json", "w") as outfile:
            json.dump(save, outfile)
        clearScreen()
        print('game saved')
        startGame(puzzle)
        #TODO Add SAVE functionality
    
    # Prints the list of found words.
    if guess == "/words":
        getWords(puzzle)
        returnGuessing()
        next = input()
        clearScreen()
        startGame(puzzle)


    # Shuffles the letters.
    if guess == "/shuffle":
        random.shuffle(puzzle.letterList)
        clearScreen()
        print('Letters shuffled')
        startGame(puzzle)

    # Shows the player's current rank in name (not number).
    if guess == "/rank":
        print(puzzle.getCurrentScoreType())

        returnGuessing()
        next = input()
        clearScreen()
        startGame(puzzle)

    # Shows all of the ranks and how many points are needed to obtain them.
    if guess == "/thresholds":
        print(puzzle.getScoreThresholds())

        returnGuessing()
        next = input()
        clearScreen()
        startGame(puzzle)

    # Stops a guess when a word is too short or long
    if len(guess) < 4:
        clearScreen()
        print('Sorry, your guess must be at least 4 letters.\n')
        startGame(puzzle)
    elif len(guess)> 15:
        clearScreen()
        print('Sorry, your guess must be at most 15 letters.\n')
        startGame(puzzle)

    specialLetter = False

    # Stops a guess when it does not contain the correct letters.
    for i in guess:
        if i not in puzzle.letterList:
            clearScreen()
            print('Your guess contains a wrong letter, try again.')
            startGame(puzzle)
        if i+"" == (puzzle.specialLetter+""):
            specialLetter=True
    if not specialLetter:
        clearScreen()
        print('Your guess does not contain the special letter, try again.')
        startGame(puzzle)
    
    # Adds the points gained from a word.
    # Prequesites: The word must be in dictionary and not in the found words list.
    # Postrequisites: Points must go up by 1 for 4, n for n>4, and 7 for a pangram.
    #   If a word is not in the dictionary or found words list, you get notified and reset to the main puzzle screen.
    if DictInterface.isValid(guess):
        if guess not in puzzle.getFoundWordList():
            puzzle.addFoundWord(guess)
            pointsGained = 0
            if len(guess)==4:
                pointsGained=1
            elif len(guess)>4:
                pointsGained = len(guess)
            if set(guess) == set(puzzle.getLetterList()):
                pointsGained += 7
        
            puzzle.addScore(pointsGained)
            clearScreen()
            print('You guessed '+ guess + ', you get ' + str(pointsGained)+ ' points!\n')
        else:
            clearScreen()
            print("You've already guessed this word!\n")
    else:
        clearScreen()
        print("Sorry, your guess is not valid, please try again.\n")
    startGame(puzzle)
