import os
import random
import re
import json
from puzzle import *
import DictInterface 

# The main game loop, which contains each action a player can make and calls upon the underlying structure.
# Prerequesite: Must run until stopped.
def startGame(puzzle):
    
    


    letters = ""
    for i in puzzle.getAllLetters():
        letters+= i+" "

    print('LETTERS:')
    print('-----------------')
    print(puzzle.letterList)
    print('Must Contain: ' + puzzle.specialLetter)
    print('-----------------')
    print('Score:')
    print(puzzle.getCurrentScore())
    print ('Enter Guess below, enter /words for a list of words, enter /shuffle to shuffle the letters, enter /rank to see your rank, enter /thresholds to see rank thresholds, enter /quit to quit the program, or enter /save to save your progress')
    guess = input()
    guess = guess.lower()

    # Stops the program.
    if guess == "/quit":
        exit()

    # Saves the game data to the save file.
    if guess == "/save":
        save = {
            "letters":list(puzzle.letterList),
            "specialLetter":puzzle.specialLetter,
            "words" : list(puzzle.getFoundWordList()),
            "score": puzzle.getCurrentScore()
        }
        
        with open("sample.json", "w") as outfile:
            json.dump(save, outfile)
        os.system('cls')
        print('game saved')
        startGame(puzzle)
        #TODO Add SAVE functionality
    
    # Prints the list of found words.
    if guess == "/words":
        print ('Words found:')
        print (puzzle.getFoundWordList())

        print("press enter to return to guessing")
        next = input()
        os.system('cls')
        startGame(puzzle)


    # Shuffles the letters.
    if guess == "/shuffle":
        random.shuffle(puzzle.letterList)
        os.system('cls')
        print('Letters shuffled')
        startGame(puzzle)

    # Shows the player's current rank in name (not number).
    if guess == "/rank":
        print(puzzle.getCurrentScoreType())

        print("press enter to return to guessing")
        next = input()
        os.system('cls')
        startGame(puzzle)

    # Shows all of the ranks and how many points are needed to obtain them.
    if guess == "/thresholds":
        print(puzzle.getScoreThresholds())

        print("press enter to return to guessing")
        next = input()
        os.system('cls')
        startGame(puzzle)

    # Stops a guess when a word is too short or long
    if len(guess) < 4:
        os.system('cls')
        print('word is too short')
        startGame(puzzle)
    elif len(guess)> 15:
        os.system('cls')
        print('word is too long')
        startGame(puzzle)

    specialLetter = False

    # Stops a guess when it does not contain the correct letters.
    for i in guess:
        if i not in puzzle.letterList:
            os.system('cls')
            print('word contains a letter not in the list')
            startGame(puzzle)
        if i+"" == (puzzle.specialLetter+""):
            specialLetter=True
    if not specialLetter:
        os.system('cls')
        print('word does not contain special letter')
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
            if set(guess) == set(puzzle.getAllLetters()):
                pointsGained += 7
        
            puzzle.addScore(pointsGained)
            os.system('cls')
            print('You guessed '+ guess + ', you get ' + str(pointsGained)+ ' points!')
        else:
            os.system('cls')
            print("You've already guessed this word!\n")
    else:
        os.system('cls')
        print("Sorry, this word is not a valid answer!\n")
    startGame(puzzle)
