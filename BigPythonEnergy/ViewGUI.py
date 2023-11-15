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

    QApplication, QDialog, QMainWindow

)

from PyQt5.uic import loadUi

from MainWindowUI import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = MainUI()
        self.setupUi(self)
        self.connections()
    
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
        self.addWordLE.textEdited.connect(lambda: self.checkKeyboardInput())
    
    def checkKeyboardInput(self):
        if self.controller.model.getPuzzle().isNotNull():
            if (len(self.addWordLE.text()) > 0 and self.addWordLE.text() != ""):
                if (self.controller.isValidLetter(self.addWordLE.text()[-1])):
                    self.addWordLE.setText(self.addWordLE.text()[:-1])

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

    def getHintsUIDisplay(self):
        return self.controller.model.getBingoHint()
    
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
        
    def setCurrentPoints(self):
        self.pointsGained.setText(str(self.controller.model.getPuzzle().getCurrentScore()))

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

    def remFoundWords(self):
        self.foundWords.clear()

    def savedBlankView(self, text):
        checker = self.controller.savedBlank(text)
        self.wrongInputLabel.setText(checker)
    
    def savedView(self, text):
        checker = self.controller.saved(text)
        self.wrongInputLabel.setText(checker)
    
    def randomView(self):
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
    
    def loadView(self):
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
        else:
            self.wrongInputLabel.setText("Game did not load succesfully.")
    
    def startView(self, newWord):
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

        else:
            self.wrongInputLabel.setText("Not a valid starting word.")
    
    def submitView(self):
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
    
    def shuffle(self):
        if self.controller.model.getPuzzle().isNotNull():
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

class helpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/helpMenu.ui", self)

class aboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/about.ui", self)

class saveDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/saveMenu.ui", self)
        self.connections()
    
    def connections(self):
        self.saveButton.pressed.connect(lambda: win.savedView(self.saveNameEdit.text()))

class blankSaveDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/blankSaveMenu.ui", self)
        self.connections()
    
    def connections(self):
        self.saveButton.clicked.connect(lambda: win.savedBlankView(self.saveNameEdit.text()))

class newGameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/newGame.ui", self)
        self.connections()
    
    def connections(self):
        self.randomButton.clicked.connect(lambda: win.randomView())
        self.startButton.clicked.connect(lambda: win.startView(self.newWord.text()))

class thresholdDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/rankThresholds.ui", self)
        if win.controller.model.getPuzzle().isNotNull():
            self.threshText.setText(win.getScoreThresholds())

class hintDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/hintsMenu.ui", self)
        if win.controller.model.getPuzzle().isNotNull():
            self.threshText.setText(win.getBingo())

class ccDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/ccAttributions.ui", self)


app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())