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
    def __init__(self, letters=None, specialLetter=None, currentScore=None, foundWords=None, totalWords=None, isNull=None):
        if letters is not None:
            
            self.letters = None
            self.letters = set()
            self.letters = letters
            self.letterList = None
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
        if totalWords is not None:
            self.listOfTotalWords = totalWords
        else:
            self.listOfTotalWords = None
            self.listOfTotalWords = set()
            self.listOfTotalWords = DictInterface.findValid(self.specialLetter, self.letterList)
        if foundWords is not None:
            self.listOfFoundWords = foundWords
        else:
            self.listOfFoundWords = None
            self.listOfFoundWords = set()
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
    
    def getLetters(self):
        return self.letters
    
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
        if(word != ""):
            self.listOfFoundWords.add(word)

    # Used to set all found words in case of loading a puzzle.
    def setFoundWord(self, wordList):
        self.listOfFoundWords = wordList

    def shuffleLetterList(self):
        random.shuffle(self.letterList)
