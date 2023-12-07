from Puzzle import *
import DictInterface
import scoreboard
from cryptography.fernet import Fernet

# Singleton design pattern: makes sure there is only ever one instance of this class.
class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Model(metaclass=Singleton):

    # Constructor for both with and without a puzzle.
    def __init__(self, setupPuzzle=None):
        if setupPuzzle is not None:
            self.puzzle = setupPuzzle
        else:
            self.puzzle = puzzle()

    # Sets a new puzzle.
    def setPuzzle(self, letters=None, specialLetter=None, currentScore=None, foundWords=None, totalWords=None):
        newPuzzle = puzzle(letters, specialLetter, currentScore, foundWords, totalWords)
        self.puzzle = newPuzzle
    
    # Gets the puzzle.
    def getPuzzle(self):
        return self.puzzle
    
    # Gets the full bingo 2D array.
    def getBingoHint(self):
        return DictInterface.bingoHint(self.puzzle.getSpecialLetter(), self.puzzle.getLetters())

    # Gets the number of pangrams and perfect pangrams as a list.
    def getPangramNumbers(self):
        return DictInterface.countPangramAndPerfect(self.puzzle.getSpecialLetter(), self.puzzle.getLetters())
    
    # Checks if a word has 7 unique letters.
    def has_7_unique_letters(self, word):
        return DictInterface.has_7_unique_letters(word)
    
    # Gets a random word with exactly 7 unique letters.
    def getRandomWord(self):
        return DictInterface.randomWord()
    
    # Gets the list of all valid words for the puzzle.
    def getValidWordList(self):
        return DictInterface.findValid(self.puzzle.getSpecialLetter(), self.puzzle.getLetters())
    
    # Checks if a word is in the dictionary.
    def isValid(self, guess):
        return DictInterface.isValid(guess)
    
    # Returns an int representing the number of words that start with the first two letters represented by tup.
    def getEachStartingWith(self, tup):
        return DictInterface.findStartingWith(tup, self.puzzle.getLetters(), self.puzzle.getSpecialLetter())
    
    # Shuffles the letter list to new positions.
    def shuffleLetterList(self):
        self.puzzle.shuffleLetterList()

    # Adds a word to the found words list.
    def addFoundWord(self, word):
        self.puzzle.addFoundWord(word)

    # Adds an int represented by score to the current score.
    def addScore(self, score):
        self.puzzle.addScore(score)
    
    # Gets the scoreboard for the current puzzle in progress.
    def getScoreboard(self):
        placedLetters = ""
        letters = self.puzzle.getLetterList()
        letters.sort()
        for i in letters:
            placedLetters += i
        rletter = self.puzzle.getSpecialLetter()
        return scoreboard.getScoreboard(placedLetters, rletter)
    
    # Adds a player to the scoreboard based on the current puzzle in progress.
    def addPlayer(self, name):
        score = self.puzzle.getCurrentScore()
        placedLetters = ""
        letters = self.puzzle.getLetterList()
        letters.sort()
        for i in letters:
            placedLetters += i
        rletter = self.puzzle.getSpecialLetter()
        return scoreboard.addScore(name, score, placedLetters, rletter)

    # Encrypts the valid word list using a key into a group of bytes.
    def getEncryptedData(self):
        fern = Fernet(Fernet.generate_key())
        data = DictInterface.findValid(self.puzzle.getSpecialLetter(), self.puzzle.getLetters())
        bytes = ','.join(map(str, data))
        return fern.encrypt(bytes.encode())

    pass