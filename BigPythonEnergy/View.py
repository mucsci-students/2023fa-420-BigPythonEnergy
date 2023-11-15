import ViewCLI
import MainWindowUI
import sys

class View:
    def __init__(self):
        view = True

    def getBingo(self, model):
        return ViewCLI.getBingo(model)
    
    def getFoundWordsDisplay(self, model):
        return ViewCLI.getWords(model)
    
    def getReturnGuessingPrompt(self):
        return ViewCLI.returnGuessing()
    
    def getHelpMenu(self):
        return ViewCLI.helpMenuDisplay()

    def getUnrecCommPrompt(self):
        return ViewCLI.unrecognizedCommand()
    
    def getNewGamePrompt(self):
        return ViewCLI.newGameDisplay()
    
    def getStartingPrompt(self):
        return ViewCLI.startMenuDisplay()
    
    def getMainGame(self, model):
        return ViewCLI.mainGameDisplay(model)
    
    def getEntryDisplay(self):
        return ViewCLI.entryDisplay()
    
    def clearScreen(self):
        return ViewCLI.clearScreen()
    
    def getCurrentScoreType(self, model):
        return ViewCLI.getCurrentScoreType(model)
    
    def getScoreThresholdsMenu(self, model):
        return ViewCLI.getScoreThresholds(model)
    
