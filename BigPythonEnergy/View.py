import ViewCLI
import MainWindowUI
import sys

# Class that interfaces the view for the CLI.
class View:
    def __init__(self):
        view = True

    # Returns the textual representation of the bingo for the current game.
    def getBingo(self, model):
        return ViewCLI.getBingo(model)
    
    # Returns the textual representation of all found words for the current game.
    def getFoundWordsDisplay(self, model):
        return ViewCLI.getWords(model)
    
    # Returns the prompt to make a guess.
    def getReturnGuessingPrompt(self):
        return ViewCLI.returnGuessing()
    
    # Returns the help menu.
    def getHelpMenu(self):
        return ViewCLI.helpMenuDisplay()

    # Returns a string stating that the command was unrecognized.
    def getUnrecCommPrompt(self):
        return ViewCLI.unrecognizedCommand()
    
    # Returns the prompt for a new game.
    def getNewGamePrompt(self):
        return ViewCLI.newGameDisplay()
    
    # Returns the main menu for the CLI.
    def getStartingPrompt(self):
        return ViewCLI.startMenuDisplay()
    
    # Returns all of the puzzle and command information, essentially the main game display.
    def getMainGame(self, model):
        return ViewCLI.mainGameDisplay(model)
    
    # Returns the starting information for the CLI program.
    def getEntryDisplay(self):
        return ViewCLI.entryDisplay()
    
    # Clears the screen for CLI on Mac, Windows, and Linux.
    def clearScreen(self):
        return ViewCLI.clearScreen()
    
    # Returns the textual rank display of the current score for the current game.
    def getCurrentScoreType(self, model):
        return ViewCLI.getCurrentScoreType(model)
    
    # Returns a textual representation of all scores and their points thresholds for the current game.
    def getScoreThresholdsMenu(self, model):
        return ViewCLI.getScoreThresholds(model)
    
    # Returns the prompt to save with or without encryption.
    def getSaveType(self):
        return ViewCLI.getSaveType()

    # Returns the letter representation seen in the main game.
    def getAllLetters(self, model):
        return ViewCLI.getAllLetters(model)
