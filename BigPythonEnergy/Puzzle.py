"""
This script defines a `puzzle` class that represents a game puzzle in a Spelling Bee game application. The class handles various aspects of the puzzle, including letter management, scoring, word validation, and rank calculations. Additionally, it provides getter methods to retrieve game-related information.

- `puzzle` class: Represents a game puzzle and includes methods for initializing, managing, and retrieving game-related data.
  - Constructor (`__init__`): Initializes the puzzle with 7 letters, a special letter, and an optional current score.
  - `initializeTotalScore()`: Initializes the total possible score based on the puzzle's word list.
  - Getter methods for various game attributes like letters, scores, and found words.
  - Methods for adding and updating the player's score and found words.
  - `getCurrentScoreType()`: Calculates and returns the player's rank based on their current score as a percentage of the total score.
  - `getScoreThresholds()`: Returns rank thresholds and the corresponding total scores.
  - Static methods `clearScreen()`: Clears the command line screen based on the platform.

Overall, this script provides the core functionality for managing game puzzles, tracking player progress, and calculating ranks in the Spelling Bee game.
"""

import random
import string
import DictInterface
import os
import platform

# Description: Handles the operations of each piece of the puzzle as well as retrieval and the like.
# Constraints: Must have exactly 7 letters, must have a totalScore > 0, must assign a special letter.
class puzzle:

    listOfTotalWords = set()
    listOfFoundWords = set()
    normalLetters = set()
    currentScore = 0
    totalScore = 0
    letterList = []
    
    # Constructor that handles creation of the play elements of a specific puzzle.
    def __init__(self, letters=None, specialLetter=None, currentScore=None):
        if letters is not None:
            
            self.letters = None
            self.letters = set()
            self.letters = letters
            self.letterList = []
            if specialLetter is not None:
                self.specialLetter = specialLetter
            if specialLetter is None:
                self.specialLetter = random.choice(tuple(letters))
            for i in letters:
                self.letterList.append(i)
            self.normalLetters = None
            self.normalLetters = set()
            for i in letters:
                self.normalLetters.add(i)
            self.normalLetters.remove(self.getSpecialLetter())
        # Mostly for testing purposes.
        else:
            self.letterList = []
            self.specialLetter = None

        # Sets current score to a new game or a loaded value.
        if currentScore is not None:
            self.currentScore = currentScore
        else:
            self.currentScore = 0

        # Initializes blank sets and new total score for a new game.
        self.listOfTotalWords = None
        self.listOfTotalWords = set()
        self.listOfFoundWords = None
        self.listOfFoundWords = set()
        self.listOfTotalWords = DictInterface.findValid(self.specialLetter, self.letterList)
        self.initializeTotalScore()

    # Initializes the total possible score, primarily for puzzle setup.
    def initializeTotalScore(self):
        self.totalScore = 0

        for i in self.getTotalWordList():
            if len(i) == 4:
                self.totalScore += 1
            elif len(i) > 4:
                self.totalScore += len(i)

    # ------ Getter Methods ------

    def getAllLetters(self):
        allLetters = "| "
        for i in range(6):
            allLetters = allLetters + self.letterList[i] + " | "
        allLetters = allLetters + self.letterList[6] + " |"
        return allLetters
    
    def getLetterList(self):
        return self.letterList

    def getNormalLetters(self):
        return self.normalLetters
    
    def getSpecialLetter(self):
        return self.specialLetter
    
    def getCurrentScore(self):
        return self.currentScore
    
    def getTotalScore(self):
        return self.totalScore
    
    def getCurrentScoreType(self):
        percentage = self.currentScore / self.totalScore

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
    
    def getScoreThresholds(self):
        queenBee = "Queen Bee: " + str(self.getTotalScore())
        genius = "Genius: " + str(int((self.getTotalScore() * 0.7) + 0.99999999))
        amazing = "Amazing: " + str(int((self.getTotalScore() * 0.5) + 0.99999999))
        great = "Great: " + str(int((self.getTotalScore() * 0.4) + 0.99999999))
        nice = "Nice: " + str(int((self.getTotalScore() * 0.25) + 0.99999999))
        solid = "Solid: " + str(int((self.getTotalScore() * 0.15) + 0.99999999))
        good = "Good: " + str(int((self.getTotalScore() * 0.08) + 0.99999999))
        movingUp = "Moving Up: " + str(int((self.getTotalScore() * 0.05) + 0.99999999))
        goodStart = "Good Start: " + str(int((self.getTotalScore() * 0.02) + 0.99999999))
        beginner = "Beginner: 0"

        return "Rank thresholds:\n\n" + queenBee + "\n" + genius + "\n" + amazing + "\n" + great + "\n" + nice + "\n" + solid + "\n" + good + "\n" + movingUp + "\n" + goodStart + "\n" + beginner
    
    def getFoundWordList(self):
        return self.listOfFoundWords
    
    def getTotalWordList(self):
        return self.listOfTotalWords
    
    # ------ Others ------
    
    # Used to set score directly in case of loading a puzzle.
    def setScore(self, score):
        self.currentScore = score

    def addScore(self, score):
        self.currentScore += score 
    
    def addFoundWord(self, word):
        self.listOfFoundWords.add(word)

    # Used to set all found words in case of loading a puzzle.
    def setFoundWord(self, wordList):
        self.listOfFoundWords = wordList

    def clearScreen():
        system_platform = platform.system()
        if system_platform == "Windows":
            os.system("cls")  # Clear screen on Windows
        else:
            os.system("clear")  # Clear screen on macOS and Linux
