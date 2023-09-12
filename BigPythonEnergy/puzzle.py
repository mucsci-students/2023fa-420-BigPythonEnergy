import random
import string

# Description: Handles the operations of each piece of the puzzle as well as retrieval and the like.
# Constraints: Must have exactly 7 letters, must have a totalScore > 0, must assign a special letter.
# Contributors: Rosaline Mattaboni
class puzzle:

    listOfTotalWords = set()
    listOfFoundWords = set()
    currentScore = 0
    totalScore = 0
    
    def __init__(self, letters):
        self.letters = letters
        self.specialLetter = random.choice(letters)

        #TODO - pull words from JSON list, put them in a set, should be handled by R/W.
        totalWords = set()

        self.listOfTotalWords = totalWords

    def __init__(self):
        #TODO - for when no word is chosen. Has to pull from a random (exactly 7-letter) word for the letters.
        return 0

    def getAllLetters(self):
        return self.letters

    def getNormalLetters(self):
        normalLetters = self.letters
        normalLetters.remove(self.getSpecialLetter())
        return normalLetters
    
    def getSpecialLetter(self):
        return self.specialLetter
    
    def getCurrentScore(self):
        return self.currentScore
    
    def getTotalScore(self):
        return self.totalScore
    
    def initalizeTotalScore(self):
        self.totalScore = 0

        for i in self.getTotalWordList():
            if len(i) == 4:
                self.totalScore += 1
            elif len(i) > 4:
                self.totalScore += len(i)

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
    
    def getFoundWordList(self):
        return self.listOfFoundWords
    
    def getTotalWordList(self):
        return self.listOfTotalWords