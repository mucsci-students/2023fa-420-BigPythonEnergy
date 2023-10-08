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
from tkinter import filedialog
from MainGameCLI import *
from puzzle import *
from DictInterface import *
import random as rd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (

    QApplication, QDialog, QMainWindow

)

from PyQt5.uic import loadUi

from MainWindowUI import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.newPuzzle = None
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
    
    def ccMenu(self):
        dialog = ccDialog(self)
        dialog.exec()

    def setCurrentPoints(self):
        self.pointsGained.setText(str(self.newPuzzle.getCurrentScore()))

    def savedBlank(self, saveName):
        if (self.newPuzzle != None):
            save = {
                "baseWord": list(self.newPuzzle.letterList),
                "foundWords" : list(),
                "playerPoints": 0,
                "requiredLetter": self.newPuzzle.specialLetter,
                "maxPoints": self.newPuzzle.totalScore
            }
            file_path = "blankSaves/" + saveName + ".json"
            with open(file_path, "w") as outfile:
                json.dump(save, outfile)
            self.wrongInputLabel.setText("Saved successfully!")

    def saved(self, saveName):
        if (self.newPuzzle != None):
            save = {
                "baseWord": list(self.newPuzzle.letterList),
                "foundWords" : list(self.newPuzzle.getFoundWordList()),
                "playerPoints": self.newPuzzle.getCurrentScore(),
                "requiredLetter": self.newPuzzle.specialLetter,
                "maxPoints": self.newPuzzle.totalScore
            }
            file_path = "saves/" + saveName + ".json"
            with open(file_path, "w") as outfile:
                json.dump(save, outfile)
            self.wrongInputLabel.setText("Saved successfully!")
        

    def shuffle(self):
        if self.newPuzzle is not None:
            loopedLetters = self.newPuzzle.getNormalLetters()
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

    def random(self):
        word = DictInterface.randomWord()
        print(word)
        uniqueCharacters = set(word)
        print (str(uniqueCharacters))
        nPuzzle = puzzle(uniqueCharacters)
        self.newPuzzle = nPuzzle
        print(str(self.newPuzzle.getNormalLetters()))
        loopedLetters = self.newPuzzle.getNormalLetters()
        addLetters = []
        for i in loopedLetters:
            addLetters.append(i)
        self.currentRank.setText(self.newPuzzle.getCurrentScoreType()+"")
        self.letter1.setText(addLetters[0])
        self.letter2.setText(addLetters[1])
        self.letter3.setText(addLetters[2])
        self.letter4.setText(addLetters[3])
        self.letter5.setText(addLetters[4])
        self.letter6.setText(addLetters[5])
        self.specialLetter.setText(self.newPuzzle.specialLetter)
        self.wrongInputLabel.setText("")
        self.setCurrentPoints()
        self.remFoundWords()

    def start(self, newWord):
        if len(newWord)==7 and DictInterface.isValid(newWord):
            uniqueCharacters = set()
            for i in newWord:
                uniqueCharacters.add(i)
            print (str(uniqueCharacters))
            self.newPuzzle = puzzle(uniqueCharacters)
            loopedLetters = self.newPuzzle.getNormalLetters()
            print(str(loopedLetters))
            addLetters = []
            for i in loopedLetters:
                addLetters.append(i)
            self.currentRank.setText(self.newPuzzle.getCurrentScoreType()+"")
            self.letter1.setText(addLetters[0])
            self.letter2.setText(addLetters[1])
            self.letter3.setText(addLetters[2])
            self.letter4.setText(addLetters[3])
            self.letter5.setText(addLetters[4])
            self.letter6.setText(addLetters[5])
            self.specialLetter.setText(self.newPuzzle.specialLetter)
            self.wrongInputLabel.setText("")
            self.setCurrentPoints()
            self.remFoundWords()
        else:
            self.wrongInputLabel.setText("Not a valid starting word.")

    def load(self):
        root = tk.Tk()
        root.withdraw()
        file_selected = filedialog.askopenfile()
        if (file_selected != None):
            print("")
            print(file_selected.name)
            print("")
            with open(file_selected.name, "r") as infile:
                data = json.load(infile)

            # Access the attributes from the loaded JSON data
            letters = data["baseWord"]
            special_letter = data["requiredLetter"]
            words = data["foundWords"]
            score = data["playerPoints"] 
            self.newPuzzle = None
            self.newPuzzle = puzzle(set(letters), special_letter, score)
            self.newPuzzle.listOfFoundWords = set(words)

            # Set text elements.
            self.currentRank.setText(self.newPuzzle.getCurrentScoreType()+"")
            self.letter1.setText(self.newPuzzle.letterList[1])
            self.letter2.setText(self.newPuzzle.letterList[2])
            self.letter3.setText(self.newPuzzle.letterList[3])
            self.letter4.setText(self.newPuzzle.letterList[4])
            self.letter5.setText(self.newPuzzle.letterList[5])
            self.letter6.setText(self.newPuzzle.letterList[6])
            self.specialLetter.setText(self.newPuzzle.specialLetter)
            self.setCurrentPoints()
            self.wrongInputLabel.setText("")
            self.remFoundWords()
            for i in self.newPuzzle.listOfFoundWords:
                self.addFoundWords(i)

    def submit(self):
        if self.newPuzzle != None:
            result = self.addWordLE.text()
            letterList = self.newPuzzle.getLetterList()
            foundList = self.newPuzzle.getFoundWordList()
            valid = True
            if DictInterface.isValid(result) and result not in foundList:
                for i in result:
                    if i not in letterList:
                        valid = False
                if self.newPuzzle.getSpecialLetter() not in set(result):
                    valid = False
                if valid:
                    self.newPuzzle.addFoundWord(result)
                    pointsGained = 0
                    if len(result)==4:
                        pointsGained=1
                    elif len(result)>4:
                        pointsGained = len(result)
                    if set(result) == set(self.newPuzzle.getLetterList()):
                        pointsGained += 7
                    self.newPuzzle.addScore(pointsGained)
                    print(pointsGained)
                    self.addFoundWords(result)
                    self.currentRank.setText(self.newPuzzle.getCurrentScoreType()+"")
                    self.setCurrentPoints()
                    self.wrongInputLabel.setText("You just gained " + str(pointsGained) + " points!")
                else:
                    self.wrongInputLabel.setText("Not a valid word.")
            else:
                self.wrongInputLabel.setText("Not a valid word.")
        else:
            self.wrongInputLabel.setText("Start a puzzle from the 'new' menu first!")

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
        print("")
        self.saveButton.pressed.connect(lambda: win.saved(self.saveNameEdit.text()))

class blankSaveDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/blankSaveMenu.ui", self)
        self.connections()
    
    def connections(self):
        print("")
        self.saveButton.clicked.connect(lambda: win.savedBlank(self.saveNameEdit.text()))

class newGameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/newGame.ui", self)
        self.connections()
    
    def connections(self):
        print("")
        self.randomButton.clicked.connect(lambda: win.random())
        self.startButton.clicked.connect(lambda: win.start(self.newWord.text()))

class thresholdDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/rankThresholds.ui", self)
        if(win.newPuzzle != None):
            self.threshText.setText(win.newPuzzle.getScoreThresholds())

class ccDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/ccAttributions.ui", self)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    win = Window()

    win.show()

    sys.exit(app.exec())