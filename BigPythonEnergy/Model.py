from Puzzle import *
import DictInterface
import scoreboard

class Model:
    def __init__(self, puzzle=None):
        self.puzzle = puzzle

    def setPuzzle(self, letters, specialLetter=None, currentScore=None, foundWords=None, totalWords=None, isNull=None):
        newPuzzle = puzzle(letters, specialLetter, currentScore, foundWords, totalWords, isNull)
        self.puzzle = newPuzzle
    
    def getPuzzle(self):
        return self.puzzle
    
    def getBingoHint(self):
        return DictInterface.bingoHint(self.puzzle.getSpecialLetter(), self.puzzle.getLetters())

    def getPangramNumbers(self):
        return DictInterface.countPangramAndPerfect(self.puzzle.getSpecialLetter(), self.puzzle.getLetters())
    
    def has_7_unique_letters(self, word):
        return DictInterface.has_7_unique_letters(word)
    
    def getRandomWord(self):
        return DictInterface.randomWord()
    
    def getValidWordList(self):
        return DictInterface.findValid(self.puzzle.getSpecialLetter(), self.puzzle.getLetters())
    
    def isValid(self, guess):
        return DictInterface.isValid(guess)
    
    def getEachStartingWith(self, tup):
        return DictInterface.findStartingWith(tup, self.puzzle.getLetters(), self.puzzle.getSpecialLetter())
    
    def shuffleLetterList(self):
        self.puzzle.shuffleLetterList()

    def addFoundWord(self, word):
        self.puzzle.addFoundWord(word)

    def addScore(self, score):
        self.puzzle.addScore(score)
    
    def getScoreboard(self):
        return scoreboard.getScoreboard()
    
    def addPlayer(self, name):
        score = self.puzzle.getCurrentScore()
        letters = self.puzzle.getAllLetters()
        rletter = self.puzzle.getSpecialLetter()
        return scoreboard.addScore(name, score, letters, rletter)