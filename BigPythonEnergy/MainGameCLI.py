import os
import random
import re
from puzzle import *
import DictInterface 

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
    print ('Enter Guess below, enter /words for a list of words, enter /shuffle to shuffle the letters, enter /quit to quit the program, or enter /save to save your progress')
    guess = input()
    guess = guess.lower()
    if guess == "/quit":
        exit()

    if guess == "/save":
        print('save')
        #TODO Add SAVE functionality
    
    if guess == "/words":
        print ('Words found:')
        print (puzzle.getFoundWordList())

        print("press enter to return to guessing")
        next = input()
        os.system('cls')
        startGame(puzzle)


    if guess == "/shuffle":
        random.shuffle(puzzle.letterList)
        startGame(puzzle)

    if len(guess) < 4:
        os.system('cls')
        print('word is too short')
        startGame(puzzle)
    elif len(guess)> 15:
        os.system('cls')
        print('word is too long')
        startGame(puzzle)
    specialLetter = False
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
    
    #TODO Check if word is in dictionary here

    if DictInterface.isValid(guess):
        puzzle.addFoundWord(guess)
        pointsGained = 0
        if len(guess)==4:
            pointsGained=4
        elif len(guess)>4:
            pointsGained = len(guess)
        
        puzzle.addScore(pointsGained)
        os.system('cls')
        print('You guessed '+ guess + ' you get ' + str(pointsGained)+ ' Points')
        
    startGame(puzzle)
