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

    # Constructor for this controller that creates a model for which to interface with.
    def __init__(self):
        self.model = Model()
    
    # Checks if a letter is not valid.
    def isNotValidLetter(self, letter):
        if letter in self.model.getPuzzle().getLetters():
            return False
        else:
            return True

    # Saves a blank copy of the current game.
    # If there is no game, it does nothing and returns a special string.
    # If the save name is blank or does not work, it does nothing and returns a special string.
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
                return "Saved successfully!"
            else:
                return "Not a valid save name."
        else:
            return "Please start a new puzzle before attempting to save!"

    # Saves a copy of the current game.
    # If there is no game, it does nothing and returns a special string.
    # If the save name is blank or does not work, it does nothing and returns a special string.
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

    # Generates a new random puzzle.
    def random(self):
        word = self.model.getRandomWord()
        uniqueCharacters = set(word)
        self.model.setPuzzle(uniqueCharacters)

    # Starts a new game based on a given word and, optionally, special letter.
    def start(self, newWord, specialLetter=None):
        uniqueCharacters = set()
        for i in newWord:
            uniqueCharacters.add(i)
        self.model.setPuzzle(uniqueCharacters)
        if specialLetter is not None:
            self.model.setPuzzle(uniqueCharacters, specialLetter)
    
    # Loads a new game from a file.
    # If no file is chosen, returns 0.
    # If the author is wrong in the case of decryption, returns -1.
    # If the load is successful, sets puzzle and returns 1.
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

    # Checks a submitted result.
    # If the puzzle is null, this does nothing and returns a special string.
    # If the word is not in the dictionary or is not in the found words list, this does nothing and returns a special string.
    # If the word has a wrong letter or does not have the special letter, this does nothing and returns a special string.
    # If the guess is correct, the correct amount of points is added and the word is added to the found words list.
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
