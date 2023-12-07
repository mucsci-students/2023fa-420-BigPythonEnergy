"""
This script is the graphical user interface (GUI) component of a Spelling Bee game application. It provides a visual interface for players to interact with the game, including starting new games, saving progress, submitting words, shuffling letters, and viewing various game-related information.

- `clearScreen()`: A helper function to clear the CLI screen.
- `Window`: The main GUI window class, which extends QMainWindow and incorporates the game's visual elements and interactions.
    - Handles menu actions like starting new games, displaying help and about dialogs, saving progress, shuffling letters, and more.
    - Manages UI elements for displaying current game state, letters, special letter, and found words.
    - Connects UI elements to corresponding actions and functions.
- Dialog classes (`helpDialog`, `aboutDialog`, `saveDialog`, `blankSaveDialog`, `newGameDialog`, `thresholdDialog`, `ccDialog`): These classes define various dialogs for displaying help, about, save, and other information to the player.
- GUI initialization (`if __name__ == "__main__"`): Sets up the GUI application, creates the main window, and starts the event loop.

This script integrates the graphical interface with the Spelling Bee game logic and provides an interactive experience for players.
"""

import sys
import time

import tkinter as tk
import json
from tkinter import filedialog
from MainUI import MainUI
from Model import Model
import random as rd
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (

    QApplication, QDialog, QMainWindow, QGraphicsOpacityEffect, QGraphicsEffect

)

from PyQt5.uic import loadUi

from MainWindowUI import Ui_MainWindow

# Main class for interfacing with the auto-generated MainWindowUI.py
class Window(QMainWindow, Ui_MainWindow):

    # Sets up the connection to each dialog window, the main window itself, and a few necessary variables.
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = MainUI()
        self.setupUi(self)
        self.connections()

        # Checks whether or not a file should be encrypted. Reset every time a save is successful or the save prompt is closed.
        self.encrypt = False

        # Will become 1 if a game is completed.
        self._state = 0
    
    # Connections to each separate window based on actions buttons.
    # Also, a connection to the keyboard input checker when a key is used for input.
    def connections(self):
        self.action_Exit.triggered.connect(self.close)
        self.action_New.triggered.connect(self.newGameMenu)
        self.action_About.triggered.connect(self.aboutMenu)
        self.actionAbout.triggered.connect(self.helpMenu)
        self.actionSave.triggered.connect(self.saveMenu)
        self.actionSave_Blank.triggered.connect(self.blankSaveMenu)
        self.action_Rank_Thresholds.triggered.connect(self.thresholdMenu)
        self.action_CC_Attributions.triggered.connect(self.ccMenu)
        self.actionHints.triggered.connect(self.hintMenu)
        self.actionScoreboard.triggered.connect(self.scoreMenu)
        self.addWordLE.textEdited.connect(lambda: self.checkKeyboardInput())

    # If there is a puzzle, pops up the add to scoreboard dialog first.
    # If scoreboard dialog is canceled, the main window does not close.
    # If X is pressed or a score is successfully added, the main window closes.
    def closeEvent(self, event):
        if self.controller.model.getPuzzle().isNotNull():
            dialog = scoreAddDialog(self)
            check = dialog.exec()
            if check == 0:
                event.accept()
            else:
                event.ignore()
    
    # Prevents the player from typing any letter that is not in the word.
    def checkKeyboardInput(self):
        if self.controller.model.getPuzzle().isNotNull() and self._state == 0:
            if (len(self.addWordLE.text()) > 0 and self.addWordLE.text() != ""):
                if (self.controller.isNotValidLetter(self.addWordLE.text()[-1])):
                    self.addWordLE.setText(self.addWordLE.text()[:-1])

    # Menus: Connections to dialog boxes, defined below.
    # --------------------------------------------------

    def helpMenu(self):
        dialog = helpDialog(self)
        dialog.exec()

    def aboutMenu(self):
        dialog = aboutDialog(self)
        dialog.exec()

    def saveMenu(self):
        dialog = saveDialog(self)
        dialog.exec()

    def blankSaveMenu(self):
        dialog = blankSaveDialog(self)
        dialog.exec()

    def newGameMenu(self):
        dialog = newGameDialog(self)
        dialog.exec()

    def thresholdMenu(self):
        dialog = thresholdDialog(self)
        dialog.exec()

    def hintMenu(self):
        dialog = hintDialog(self)
        dialog.exec()
    
    def ccMenu(self):
        dialog = ccDialog(self)
        dialog.exec()

    def scoreMenu(self):
        dialog = scoreDialog(self)
        dialog.exec()
    
    # Returns the entire bingo, pangram, and two letter hint display.
    # For more documentation, see ViewCLI, where the function is implemented the exact same way.
    def getBingo(self):
    
        bingo = self.controller.model.getBingoHint()
        column_widths = [max(len(str(item)) for item in col) for col in zip(*bingo)]
        totalWords = bingo[8][13]
        pangramNumbers = self.controller.model.getPangramNumbers()
        pangramCount = pangramNumbers[0]
        perfectCount = pangramNumbers[1]
        points = self.controller.model.getPuzzle().getTotalScore()
        returnString = ("Words: " + str(totalWords) + " Points: " + str(points) + " Pangrams: " + str(pangramCount) + " (Perfect: " + str(perfectCount) + ")" + "\n\n")

        for row in bingo:
            returnString = returnString + ("  ".join(str(item).rjust(width) for item, width in zip(row, column_widths))) + "\n"

        returnString = returnString + ("\n" + "Two Letter List:  ")

        validWords = self.controller.model.getValidWordList()
        starters = set()
        for word in validWords:
            starter = word[:2]
            starters.add(starter)

        for tup in starters:
            count = self.controller.model.getEachStartingWith(tup)
            if count != 0:
                returnString = returnString + (str(tup).upper() + ": " + str(count) + "   ")

        return returnString
    
    # Returns the list of scores needed for each score type.
    def getScoreThresholds(self):
        queenBee = "Queen Bee: " + str(self.controller.model.getPuzzle().getTotalScore())
        genius = "Genius: " + str(int((self.controller.model.getPuzzle().getTotalScore() * 0.7) + 0.99999999))
        amazing = "Amazing: " + str(int((self.controller.model.getPuzzle().getTotalScore() * 0.5) + 0.99999999))
        great = "Great: " + str(int((self.controller.model.getPuzzle().getTotalScore() * 0.4) + 0.99999999))
        nice = "Nice: " + str(int((self.controller.model.getPuzzle().getTotalScore() * 0.25) + 0.99999999))
        solid = "Solid: " + str(int((self.controller.model.getPuzzle().getTotalScore() * 0.15) + 0.99999999))
        good = "Good: " + str(int((self.controller.model.getPuzzle().getTotalScore() * 0.08) + 0.99999999))
        movingUp = "Moving Up: " + str(int((self.controller.model.getPuzzle().getTotalScore() * 0.05) + 0.99999999))
        goodStart = "Good Start: " + str(int((self.controller.model.getPuzzle().getTotalScore() * 0.02) + 0.99999999))
        beginner = "Beginner: 0"

        return "Rank thresholds:\n\n" + queenBee + "\n" + genius + "\n" + amazing + "\n" + great + "\n" + nice + "\n" + solid + "\n" + good + "\n" + movingUp + "\n" + goodStart + "\n" + beginner
    
    # Returns the current textual score type.
    def getCurrentScoreType(self):
        percentage = self.controller.model.getPuzzle().getCurrentScore() / self.controller.model.getPuzzle().getTotalScore()

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
        
    # Puts the current score into a points textbox.
    def setCurrentPoints(self):
        self.pointsGained.setText(str(self.controller.model.getPuzzle().getCurrentScore()))

    # Puts a found word into the found words display widget.
    def addFoundWords(self, text):
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        item.setFont(font)
        self.foundWords.addItem(item)
        item.setText(text)
        self.foundWords.sortItems()

    # Clears all found words from the display widget.
    def remFoundWords(self):
        self.foundWords.clear()

    # Handles the view updates for saving a new blank game.
    # Resets encrypt boolean.
    def savedBlankView(self, text, encrypt):
        checker = self.controller.savedBlank(text, encrypt)
        self.wrongInputLabel.setText(checker)
        self.encrypt = False
    
    # Handles the view updates for saving the game.
    # Resets encrypt boolean.
    def savedView(self, text, encrypt):
        checker = self.controller.saved(text, encrypt)
        self.wrongInputLabel.setText(checker)
        self.encrypt = False
    
    # Handles the view updates for starting a new random game.
    def randomView(self):
        if self.controller.model.getPuzzle().isNotNull():
            dialog = scoreAddDialog(self)
            dialog.exec()
        self.controller.random()
        self.currentRank.setText(self.getCurrentScoreType()+"")
        loopedLetters = self.controller.model.getPuzzle().getNormalLetters()
        addLetters = []
        for i in loopedLetters:
            addLetters.append(i)
        self.currentRank.setText(self.getCurrentScoreType()+"")
        self.letter1.setText(addLetters[0])
        self.letter2.setText(addLetters[1])
        self.letter3.setText(addLetters[2])
        self.letter4.setText(addLetters[3])
        self.letter5.setText(addLetters[4])
        self.letter6.setText(addLetters[5])
        self.specialLetter.setText(self.controller.model.getPuzzle().getSpecialLetter())
        self.wrongInputLabel.setText("New game set! Have fun!")
        self.setCurrentPoints()
        self.remFoundWords()
        self._state = 0
    
    # Handles the view updates for loading a game.
    def loadView(self):
        if self.controller.model.getPuzzle().isNotNull():
            dialog = scoreAddDialog(self)
            dialog.exec()

        checker = self.controller.load()

        if checker == 1:
            loopedLetters = self.controller.model.getPuzzle().getNormalLetters()
            addLetters = []
            for i in loopedLetters:
                addLetters.append(i)

            self.currentRank.setText(self.getCurrentScoreType()+"")
            self.letter1.setText(addLetters[0])
            self.letter2.setText(addLetters[1])
            self.letter3.setText(addLetters[2])
            self.letter4.setText(addLetters[3])
            self.letter5.setText(addLetters[4])
            self.letter6.setText(addLetters[5])
            self.specialLetter.setText(self.controller.model.getPuzzle().getSpecialLetter())
            self.setCurrentPoints()
            self.wrongInputLabel.setText("Game loaded successfully!")

            self.remFoundWords()
            for i in self.controller.model.getPuzzle().getFoundWordList():
                self.addFoundWords(i)
            
            self._state = 0
            if self.controller.model.getPuzzle().getCurrentScore() == self.controller.model.getPuzzle().getTotalScore():
                self.stateChange()

        elif checker == 0:
            self.wrongInputLabel.setText("Game did not load succesfully.")

        else:
            self.wrongInputLabel.setText("Decryption was unsuccessful.")
    
    # Handles the view updates for starting a game from a word.
    def startView(self, newWord):
        if self.controller.model.getPuzzle().isNotNull():
            dialog = scoreAddDialog(self)
            dialog.exec()
        if self.controller.model.has_7_unique_letters(newWord) and self.controller.model.isValid(newWord):
            self.controller.start(newWord)
            loopedLetters = self.controller.model.getPuzzle().getNormalLetters()
            addLetters = []
            for i in loopedLetters:
                addLetters.append(i)
            self.currentRank.setText(self.getCurrentScoreType()+"")
            self.letter1.setText(addLetters[0])
            self.letter2.setText(addLetters[1])
            self.letter3.setText(addLetters[2])
            self.letter4.setText(addLetters[3])
            self.letter5.setText(addLetters[4])
            self.letter6.setText(addLetters[5])
            self.specialLetter.setText(self.controller.model.getPuzzle().getSpecialLetter())
            self.wrongInputLabel.setText("New game set! Have fun!")
            self.setCurrentPoints()
            self.remFoundWords()
            self._state = 0

        else:
            self.wrongInputLabel.setText("Not a valid starting word.")
    
    # Handles the view updates from submission of a word.
    # Will not allow submission of a word at all if the game is completed.
    def submitView(self):
        if self._state == 0:
            result = self.addWordLE.text()
            checker = self.controller.submit(result)
            if checker == "Not a valid word.":
                self.wrongInputLabel.setText("Not a valid word.")
            elif checker == "Start a puzzle from the 'new' menu first!":
                self.wrongInputLabel.setText("Start a puzzle from the 'new' menu first!")
            else:
                self.addFoundWords(result)
                self.currentRank.setText(self.getCurrentScoreType()+"")
                self.setCurrentPoints()
                self.wrongInputLabel.setText("You just gained " + checker + " points!")
                if self.controller.model.getPuzzle().getCurrentScore() == self.controller.model.getPuzzle().getTotalScore():
                    self.stateChange()
    
    # Handles the view updates for shuffling letters.
    # Will not allow shuffling if the game is completed.
    def shuffle(self):
        if self.controller.model.getPuzzle().isNotNull() and self._state == 0:
            loopedLetters = self.controller.model.getPuzzle().getNormalLetters()
            addLetters = []
            for i in loopedLetters:
                addLetters.append(i)
            rd.shuffle(addLetters)
            self.letter1.setText(addLetters[0])
            self.letter2.setText(addLetters[1])
            self.letter3.setText(addLetters[2])
            self.letter4.setText(addLetters[3])
            self.letter5.setText(addLetters[4])
            self.letter6.setText(addLetters[5])
        
    # Flips the encryption boolean. to its opposite value.
    def encryptSwap(self):
        if self.encrypt is True:
            self.encrypt = False
        else:
            self.encrypt = True

    # Changes the state to a completed game (1).
    # Is only triggered when the current score is equal to the total score.
    # Changes text and background to show a completed game.
    def stateChange(self):
        self._state = 1
        self.wrongInputLabel.setText("CONGRATULATIONS! You won! Start a new game to play again.")
        self.letter1.setText("!")
        self.letter2.setText("!")
        self.letter3.setText("!")
        self.letter4.setText("!")
        self.letter5.setText("!")
        self.letter6.setText("!")
        self.specialLetter.setText("!")
        stylesheet = """
            background-image: url("BigPythonEnergy/ui/icons/BirthdayCakeBackgroundCCFree.png"); 
            background-repeat: no-repeat; 
            background-position: center;
            opacity: 0.2;
        """
        self.widget.setStyleSheet(stylesheet)
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.2)
        self.widget.setGraphicsEffect(self.opacity_effect)
    

# Shows the help menu.
class helpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/helpMenu.ui", self)

# Shows the about menu.
class aboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/about.ui", self)

# Shows the save menu, allows for saving from this menu.
# Resets encrypt boolean on close.
class saveDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/saveMenu.ui", self)
        self.connections()
    
    def connections(self):
        self.encryptButton.toggled.connect(lambda: win.encryptSwap())
        self.saveButton.pressed.connect(lambda: win.savedView(self.saveNameEdit.text(), win.encrypt))

    def closeEvent(self, event):
        win.encrypt = False

# Shows the blank save menu, allows for saving from this menu.
# Resets encrypt boolean on close.
class blankSaveDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/blankSaveMenu.ui", self)
        self.connections()
    
    def connections(self):
        self.encryptButton.toggled.connect(lambda: win.encryptSwap())
        self.saveButton.clicked.connect(lambda: win.savedBlankView(self.saveNameEdit.text(), win.encrypt))

    def closeEvent(self, event):
        win.encrypt = False

# Prompts for a new game.
class newGameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/newGame.ui", self)
        self.connections()
    
    def connections(self):
        self.randomButton.clicked.connect(lambda: win.randomView())
        self.startButton.clicked.connect(lambda: win.startView(self.newWord.text()))

# Shows score thresholds.
class thresholdDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/rankThresholds.ui", self)
        if win.controller.model.getPuzzle().isNotNull():
            self.threshText.setText(win.getScoreThresholds())

# Shows all hints in textual format.
class hintDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/hintsMenu.ui", self)
        if win.controller.model.getPuzzle().isNotNull():
            self.threshText.setText(win.getBingo())

# Shows all Creative Commons licensing.
class ccDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/ccAttributions.ui", self)

# Shows scoreboard for the current game.
class scoreDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/scoreboardMenu.ui", self)
        if win.controller.model.getPuzzle().isNotNull():
            self.scoreText.setText(win.controller.model.getScoreboard())

# Shows prompt to add a score to the scoreboard.
class scoreAddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/scoreAddMenu.ui", self)
        self.connections()
    
    def connections(self):
        self.addButton.clicked.connect(lambda: win.controller.model.addPlayer(self.scoreNameEdit.text()))

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())