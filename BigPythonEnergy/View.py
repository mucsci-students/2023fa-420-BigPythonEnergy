import ViewCLI
import ViewGUI
import MainWindowUI
import sys

from PyQt5.QtWidgets import QApplication

class View:
    def __init__(self, win=None, app=None):
        if(win != None):
            self.win = ViewGUI.Window()
        if(app != None):
            app = QApplication(sys.argv)

    def startGUI(self):
        ViewGUI.start(self.app, self.win)

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
