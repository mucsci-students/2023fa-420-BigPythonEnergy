"""
This script is the core of a Spelling Bee game application, handling the main game loop and player interactions.

    - `startGame(model, view)`: The main game loop where players enter guesses, manage the game, and interact with various game commands.
    - Allows players to guess words, save their progress, view found words, shuffle letters, check their rank, and see rank thresholds.
    - Validates guesses based on length, letter availability, and the presence of a special letter.
    - Awards points for valid guesses and updates the game state accordingly.
    - Handles various in-game commands like quitting, saving, and displaying information.
    - Provides feedback on the correctness of guesses and updates the player's score.

This script integrates game logic with player interactions, making it the central component of the Spelling Bee game.
"""

import json
from Model import Model
from View import View

# The main game loop, which contains each action a player can make and calls upon the underlying structure.
# Prerequesite: Must run until stopped.
def startGame(model, view):
    
    guess = view.getMainGame(model)
    guess = guess.lower()

    # Stops the program.
    if guess == "/quit":
        response = ""
        view.clearScreen()
        while response != "y" or response != "n":
            print("Would you like to add your score to the scoreboard? (y or n) ")
            response = input()
            response = response.lower()
            if response == "y":
                view.clearScreen()
                print("Enter your name for the scoreboard: ")
                name = input()
                view.clearScreen()
                print("You have successfully added yourself to the scoreboard!")
                model.addPlayer(name)
                exit()
            elif response == "n":
                exit()
            else:
                view.clearScreen()
                print("Sorry, please input y or n.")
        exit()

    # Saves the game data to the save file.
    if guess == "/save":
        saveType = view.getSaveType()
        view.clearScreen()
        if saveType == "yes":
            save = {
                "baseWord": list(model.getPuzzle().getLetterList()),
                "foundWords" : list(model.getPuzzle().getFoundWordList()),
                "playerPoints": model.getPuzzle().getCurrentScore(),
                "requiredLetter": model.getPuzzle().getSpecialLetter(),
                "maxPoints": model.getPuzzle().getTotalScore(),
                "secretwordlist": list(model.getEncryptedData()),
                "author": "BigPythonEnergy"
            }
        else:
            save = {
                "baseWord": list(model.getPuzzle().getLetterList()),
                "foundWords" : list(model.getPuzzle().getFoundWordList()),
                "playerPoints": model.getPuzzle().getCurrentScore(),
                "requiredLetter": model.getPuzzle().getSpecialLetter(),
                "maxPoints": model.getPuzzle().getTotalScore(),
                "wordlist": list(model.getPuzzle().getTotalWordList()),
                "author": "BigPythonEnergy"
            }

        print('Enter a name for your save file:')
        fileName = input()
        if fileName == "":
            view.clearScreen()
            print('You may only save from a valid file name.')
            startGame(model, view)
        with open("BigPythonEnergy/saves/"+fileName+".json", "w") as outfile:
            json.dump(save, outfile)
        view.clearScreen()
        print('Game saved.')
        startGame(model, view)

    # Saves a blank copy of the game to a save file.
    if guess == "/blanksave":
        saveType = view.getSaveType()
        view.clearScreen()
        if saveType == "yes":
            save = {
                "baseWord": list(model.getPuzzle().getLetterList()),
                "foundWords" : list(),
                "playerPoints": 0,
                "requiredLetter": model.getPuzzle().getSpecialLetter(),
                "maxPoints": model.getPuzzle().getTotalScore(),
                "secretwordlist": list(model.getEncryptedData()),
                "author": "BigPythonEnergy"
            }
        else:
            save = {
                "baseWord": list(model.getPuzzle().getLetterList()),
                "foundWords" : list(),
                "playerPoints": 0,
                "requiredLetter": model.getPuzzle().getSpecialLetter(),
                "maxPoints": model.getPuzzle().getTotalScore(),
                "wordlist": list(model.getPuzzle().getValidWordList()),
                "author": "BigPythonEnergy"
            }

        print('Enter a name for your blank save file:')
        fileName = input()
        if fileName == "":
            view.clearScreen()
            print('You may only save from a valid file name.')
            startGame(model, view)
        with open("BigPythonEnergy/blankSaves/"+fileName+".json", "w") as outfile:
            json.dump(save, outfile)
        view.clearScreen()
        print('Game saved.')
        startGame(model, view)
    
    # Prints the list of found words.
    if guess == "/words":
        view.clearScreen()
        view.getFoundWordsDisplay(model)
        view.getReturnGuessingPrompt()
        next = input()
        view.clearScreen()
        startGame(model, view)


    # Shuffles the letters.
    if guess == "/shuffle":
        model.shuffleLetterList()
        view.clearScreen()
        print('Letters shuffled.')
        startGame(model, view)

    # Shows the player's current rank in name (not number).
    if guess == "/rank":
        view.clearScreen()
        print(view.getCurrentScoreType(model))
        view.getReturnGuessingPrompt()
        next = input()
        view.clearScreen()
        startGame(model, view)

    # Shows all of the ranks and how many points are needed to obtain them.
    if guess == "/thresholds":
        view.clearScreen()
        print(view.getScoreThresholdsMenu(model))
        view.getReturnGuessingPrompt()
        next = input()
        view.clearScreen()
        startGame(model, view)

    # Shows the bingo, pangram, and first two letters hints.
    if guess == "/hints":
        view.clearScreen()
        print(view.getBingo(model))
        view.getReturnGuessingPrompt()
        input()
        view.clearScreen()
        startGame(model, view)

    # Shows the scoreboard for the current game.
    if guess == "/scoreboard":
        view.clearScreen()
        df = model.getScoreboard()
        print(str(df))
        #for index, row in df.iterrows():
        #    print(f'Rank: {index}, Name: {row["name"]}, score: {row["score"]}, letters: {row["letters"]}, Required Letter: {row["special letter"]}')

        print ("Hit enter to continue the game: ")
        input()
        view.clearScreen()
        startGame(model, view)
        
    # Stops a guess when a word is too short or long
    if len(guess) < 4:
        view.clearScreen()
        print('Sorry, your guess must be at least 4 letters.\n')
        startGame(model, view)
    elif len(guess)> 15:
        view.clearScreen()
        print('Sorry, your guess must be at most 15 letters.\n')
        startGame(model, view)

    specialLetter = False

    # Stops a guess when it does not contain the correct letters.
    for i in guess:
        if i not in model.getPuzzle().getLetterList():
            view.clearScreen()
            print('Your guess contains a wrong letter, try again.')
            startGame(model, view)
        if i+"" == (model.getPuzzle().getSpecialLetter()+""):
            specialLetter=True
    if not specialLetter:
        view.clearScreen()
        print('Your guess does not contain the special letter, try again.')
        startGame(model, view)
    
    # Adds the points gained from a word.
    # Prequesites: The word must be in dictionary and not in the found words list.
    # Postrequisites: Points must go up by 1 for 4, n for n>4, and 7 for a pangram.
    #   If a word is not in the dictionary or found words list, you get notified and reset to the main puzzle screen.
    if model.isValid(guess):
        if guess not in model.getPuzzle().getFoundWordList():
            model.addFoundWord(guess)
            pointsGained = 0
            if len(guess)==4:
                pointsGained=1
            elif len(guess)>4:
                pointsGained = len(guess)
            if set(guess) == set(model.getPuzzle().getLetterList()):
                pointsGained += 7
        
            model.addScore(pointsGained)
            view.clearScreen()
            print('You guessed '+ guess + ', you get ' + str(pointsGained)+ ' points!\n')
        else:
            view.clearScreen()
            print("You've already guessed this word!\n")
    else:
        view.clearScreen()
        print("Sorry, your guess is not valid, please try again.\n")
    startGame(model, view)
