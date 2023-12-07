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
from Model import Model
import random as rd
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (

    QApplication, QDialog, QMainWindow

)

from PyQt5.uic import loadUi

from MainWindowUI import Ui_MainWindow

class MainUI():
    def __init__(self):
        self.model = Model()
    
    def isValidLetter(self, letter):
        if letter in self.model.getPuzzle().getLetters():
            return False
        else:
            return True

    def savedBlank(self, saveName, encrypt):
        if self.model.getPuzzle().isNotNull():
            if encrypt is True:
                save = {
                    "baseWord": list(self.model.getPuzzle().getLetterList()),
                    "foundWords" : list(),
                    "playerPoints": 0,
                    "requiredLetter": self.model.getPuzzle().getSpecialLetter(),
                    "maxPoints": self.model.getPuzzle().getTotalScore(),
                    "secretwordlist": list(self.model.getEncryptedData()),
                    "author": "BigPythonEnergy"
                }
            else:
                save = {
                    "baseWord": list(self.model.getPuzzle().getLetterList()),
                    "foundWords" : list(),
                    "playerPoints": 0,
                    "requiredLetter": self.model.getPuzzle().getSpecialLetter(),
                    "maxPoints": self.model.getPuzzle().getTotalScore(),
                    "wordlist": list(self.model.getPuzzle().getTotalWordList()),
                    "author": "BigPythonEnergy"
                }
            if saveName != "":
                file_path = "BigPythonEnergy/blankSaves/" + saveName + ".json"
                try:
                    with open(file_path, "w") as outfile:
                        json.dump(save, outfile)
                except:
                    return "Not a valid save name."
                return "Saved succesfully!"
            else:
                return "Not a valid save name."
        else:
            return "Please start a new puzzle before attempting to save!"

    def saved(self, saveName, encrypt):
        if self.model.getPuzzle().isNotNull():
            if encrypt is True:
                save = {
                    "baseWord": list(self.model.getPuzzle().getLetterList()),
                    "foundWords" : list(self.model.getPuzzle().getFoundWordList()),
                    "playerPoints": self.model.getPuzzle().getCurrentScore(),
                    "requiredLetter": self.model.getPuzzle().getSpecialLetter(),
                    "maxPoints": self.model.getPuzzle().getTotalScore(),
                    "secretwordlist": list(self.model.getEncryptedData()),
                    "author": "BigPythonEnergy"
                }
            else:
                save = {
                    "baseWord": list(self.model.getPuzzle().getLetterList()),
                    "foundWords" : list(self.model.getPuzzle().getFoundWordList()),
                    "playerPoints": self.model.getPuzzle().getCurrentScore(),
                    "requiredLetter": self.model.getPuzzle().getSpecialLetter(),
                    "maxPoints": self.model.getPuzzle().getTotalScore(),
                    "wordlist": list(self.model.getPuzzle().getTotalWordList()),
                    "author": "BigPythonEnergy"
                }
            if saveName != "":
                file_path = "BigPythonEnergy/saves/" + saveName + ".json"
                try:
                    with open(file_path, "w") as outfile:
                        json.dump(save, outfile)
                except:
                    return "Not a valid save name."
                return "Saved successfully!"
            else:
                return "Not a valid save name."
        else:
            return "Please start a new puzzle before attempting to save!"

    def random(self):
        word = self.model.getRandomWord()
        uniqueCharacters = set(word)
        self.model.setPuzzle(uniqueCharacters)

    def start(self, newWord):
        uniqueCharacters = set()
        for i in newWord:
            uniqueCharacters.add(i)
        self.model.setPuzzle(uniqueCharacters)
    
    def load(self):
        root = tk.Tk()
        root.withdraw()
        file_selected = filedialog.askopenfile()
        if (file_selected != None):
            with open(file_selected.name, "r") as infile:
                data = json.load(infile)

            # Access the attributes from the loaded JSON data
            letters = data["baseWord"]
            special_letter = data["requiredLetter"]
            words = data["foundWords"]
            score = data["playerPoints"]
            try:
                wordlist = data["wordlist"]
            except:
                try:
                    author = data["author"]
                except:
                    author = None
                else:
                    if (author != "BigPythonEnergy"):
                        return -1
            self.model.setPuzzle(set(letters), special_letter, score, set(words))
            return 1
        return 0

    def submit(self, result):
        if self.model.getPuzzle().isNotNull():
            letterList = self.model.getPuzzle().getLetterList()
            foundList = self.model.getPuzzle().getFoundWordList()
            valid = True
            if self.model.isValid(result) and result not in foundList:
                for i in result:
                    if i not in letterList:
                        valid = False
                if self.model.getPuzzle().getSpecialLetter() not in set(result):
                    valid = False
                if valid:
                    self.model.addFoundWord(result)
                    pointsGained = 0
                    if len(result)==4:
                        pointsGained=1
                    elif len(result)>4:
                        pointsGained = len(result)
                    if set(result) == set(self.model.getPuzzle().getLetterList()):
                        pointsGained += 7
                    self.model.addScore(pointsGained)
                    return str(pointsGained)
                else:
                    return "Not a valid word."
            else:
                return "Not a valid word."
        else:
            return "Start a puzzle from the 'new' menu first!"
