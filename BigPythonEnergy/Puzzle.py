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
from PuzzleBuilder import PuzzleAbstract

# Description: Handles the operations of each piece of the puzzle as well as retrieval and the like.
# Constraints: Must have exactly 7 letters, must have a totalScore > 0, must assign a special letter.
class puzzle:
    
    # Constructor that handles creation of the play elements of a specific puzzle.
    def __init__(self, letters=None, specialLetter=None, currentScore=None, foundWords=None, totalWords=None):
        
        self.puzzleBuilt = PuzzleAbstract(letters, specialLetter, currentScore, foundWords, totalWords)

    # ------ Getter Methods ------
    
    def isNotNull(self):
        return self.puzzleBuilt.isNotNull()

    def getLetters(self):
        return self.puzzleBuilt.getLetters()
    
    def getLetterList(self):
        return self.puzzleBuilt.getLetterList()

    def getNormalLetters(self):
        return self.puzzleBuilt.getNormalLetters()
    
    def getSpecialLetter(self):
        return self.puzzleBuilt.getSpecialLetter()
    
    def getCurrentScore(self):
        return self.puzzleBuilt.getCurrentScore()
    
    def getTotalScore(self):
        return self.puzzleBuilt.getTotalScore()
    
    def getFoundWordList(self):
        return self.puzzleBuilt.getFoundWordList()
    
    def getTotalWordList(self):
        return self.puzzleBuilt.getTotalWordList()
    
    # ------ Others ------
    
    # Used to set score directly in case of loading a puzzle.
    def setScore(self, score):
        self.puzzleBuilt.setScore(score)

    def addScore(self, score):
        self.puzzleBuilt.addScore(score)
    
    def addFoundWord(self, word):
        self.puzzleBuilt.addFoundWord(word)

    # Used to set all found words in case of loading a puzzle.
    def setFoundWord(self, wordList):
        self.setFoundWord(wordList)

    def shuffleLetterList(self):
        self.puzzleBuilt.shuffleLetterList()
