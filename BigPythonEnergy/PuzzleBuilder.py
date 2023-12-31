import random
import DictInterface

# Chooses whether to create a null puzzle or a regular puzzle.
class PuzzleAbstract:
    puzzlePieces = None
    def __init__(self, check, sL, cS, fW, tW):
        if check is None:
            self.puzzlePieces = PuzzleNull()
        else:
            self.puzzlePieces = PuzzleFull(check, sL, cS, fW, tW)
    
    def getLetters(self):
        return self.puzzlePieces.getLetters()
    
    def getLetterList(self):
        return self.puzzlePieces.getLetterList()

    def getNormalLetters(self):
        return self.puzzlePieces.getNormalLetters()
    
    def getSpecialLetter(self):
        return self.puzzlePieces.getSpecialLetter()
    
    def getCurrentScore(self):
        return self.puzzlePieces.getCurrentScore()
    
    def getTotalScore(self):
        return self.puzzlePieces.getTotalScore()
    
    def getFoundWordList(self):
        return self.puzzlePieces.getFoundWordList()
    
    def getTotalWordList(self):
        return self.puzzlePieces.getTotalWordList()
    
    def setScore(self, score):
        self.puzzlePieces.setScore(score)

    def addScore(self, score):
        self.puzzlePieces.addScore(score)
    
    def addFoundWord(self, word):
        self.puzzlePieces.addFoundWord(word)

    def setFoundWord(self, wordList):
        self.puzzlePieces.setFoundWord(wordList)

    def shuffleLetterList(self):
        self.puzzlePieces.shuffleLetterList()

    def isNotNull(self):
        return self.puzzlePieces.isNotNull()

# Builds a puzzle where every variable is None, every function returns None, and isNotNull() returns False.
class PuzzleNull:
    def __init__(self):

        self.letters = None
        self.letterList = None
        self.specialLetter = None
        self.normalLetters = None
        self.currentScore = None
        self.listOfTotalWords = None
        self.listOfFoundWords = None
        self.totalScore = None

    def isNotNull(self):
        return False
    
    def getLetters(self):
        return None
    
    def getLetterList(self):
        return None

    def getNormalLetters(self):
        return None
    
    def getSpecialLetter(self):
        return None
    
    def getCurrentScore(self):
        return None
    
    def getTotalScore(self):
        return None
    
    def getFoundWordList(self):
        return None
    
    def getTotalWordList(self):
        return None
    
    def setScore(self, score):
        return None

    def addScore(self, score):
        return None
    
    def addFoundWord(self, word):
        return None

    def setFoundWord(self, wordList):
        return None

    def shuffleLetterList(self):
        return None

# Returns a function where every parameter is set for the puzzle based on inputs.
# Each function here works as described in the main Puzzle class.
class PuzzleFull:
    def __init__(self, letters, specialLetter, currentScore, foundWords, totalWords):

        # Sets the letter set, which must not be None if this point has been reached.
        self.letters = None
        self.letters = set()
        self.letters = letters

        # Creates a list of letters based on the letter set.
        self.letterList = None
        self.letterList = []
        for i in letters:
            self.letterList.append(i)

        # Either sets the special letter or chooses a random one if none exists.
        if specialLetter is not None:
            self.specialLetter = specialLetter
        if specialLetter is None:
            self.specialLetter = random.choice(tuple(letters))

        # Creates a set of all letters except the special letter.
        self.normalLetters = None
        self.normalLetters = set()
        for i in letters:
            self.normalLetters.add(i)
        self.normalLetters.remove(self.specialLetter)

        # Sets the current score to currentScore on load or 0 on new game.
        if currentScore is not None:
            self.currentScore = currentScore
        else:
            self.currentScore = 0

        # Sets the list of all possible words on load or generates it on new game.
        if totalWords is not None:
            self.listOfTotalWords = None
            self.listOfTotalWords = set()
            self.listOfTotalWords = totalWords
        else:
            self.listOfTotalWords = None
            self.listOfTotalWords = set()
            self.listOfTotalWords = DictInterface.findValid(self.specialLetter, self.letterList)

        # Sets the list of found words on load or creates a blank set on new game.
        if foundWords is not None:
            self.listOfFoundWords = None
            self.listOfFoundWords = set()
            self.listOfFoundWords = foundWords
        else:
            self.listOfFoundWords = None
            self.listOfFoundWords = set()

        # Generates the total score based on the list of all possible words.
        self.totalScore = 0
        for i in self.listOfTotalWords:
            if len(i) == 4:
                self.totalScore += 1
            elif len(i) > 4:
                self.totalScore += len(i)
                if len(set(i)) == 7:
                    self.totalScore += 7

    def isNotNull(self):
        return True

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
    
    def setScore(self, score):
        self.currentScore = score

    def addScore(self, score):
        self.currentScore += score
    
    def addFoundWord(self, word):
        if(word != ""):
            self.listOfFoundWords.add(word)

    def setFoundWord(self, wordList):
        self.listOfFoundWords = wordList

    def shuffleLetterList(self):
        random.shuffle(self.letterList)