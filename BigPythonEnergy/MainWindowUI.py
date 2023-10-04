# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gameBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
from MainGameCLI import *
from puzzle import *
from DictInterface import *
import random as rd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setSizeIncrement(QtCore.QSize(1, 1))
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.letter6 = QtWidgets.QPushButton(self.centralwidget)
        self.letter6.setGeometry(QtCore.QRect(250, 210, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.letter6.setFont(font)
        self.letter6.setText("")
        self.letter6.setObjectName("letter6")
        self.letter5 = QtWidgets.QPushButton(self.centralwidget)
        self.letter5.setGeometry(QtCore.QRect(170, 210, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.letter5.setFont(font)
        self.letter5.setText("")
        self.letter5.setObjectName("letter5")
        self.letter4 = QtWidgets.QPushButton(self.centralwidget)
        self.letter4.setGeometry(QtCore.QRect(140, 155, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.letter4.setFont(font)
        self.letter4.setText("")
        self.letter4.setObjectName("letter4")
        self.letter1 = QtWidgets.QPushButton(self.centralwidget)
        self.letter1.setGeometry(QtCore.QRect(280, 155, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.letter1.setFont(font)
        self.letter1.setText("")
        self.letter1.setObjectName("letter1")
        self.letter2 = QtWidgets.QPushButton(self.centralwidget)
        self.letter2.setGeometry(QtCore.QRect(250, 100, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.letter2.setFont(font)
        self.letter2.setText("")
        self.letter2.setObjectName("letter2")
        self.letter3 = QtWidgets.QPushButton(self.centralwidget)
        self.letter3.setGeometry(QtCore.QRect(170, 100, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.letter3.setFont(font)
        self.letter3.setText("")
        self.letter3.setObjectName("letter3")
        self.specialLetter = QtWidgets.QPushButton(self.centralwidget)
        self.specialLetter.setGeometry(QtCore.QRect(210, 155, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.specialLetter.setFont(font)
        self.specialLetter.setText("")
        self.specialLetter.setObjectName("specialLetter")
        self.addWordButton = QtWidgets.QPushButton(self.centralwidget)
        self.addWordButton.setGeometry(QtCore.QRect(180, 340, 90, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.addWordButton.setFont(font)
        self.addWordButton.setObjectName("addWordButton")
        self.scrollingText = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollingText.setGeometry(QtCore.QRect(380, 190, 200, 230))
        self.scrollingText.setWidgetResizable(True)
        self.scrollingText.setObjectName("scrollingText")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 198, 228))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.foundWords = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.foundWords.setGeometry(QtCore.QRect(10, 10, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.foundWords.setFont(font)
        self.foundWords.setObjectName("foundWords")
        self.scrollingText.setWidget(self.scrollAreaWidgetContents)
        self.currRankLabel = QtWidgets.QLabel(self.centralwidget)
        self.currRankLabel.setGeometry(QtCore.QRect(380, 90, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.currRankLabel.setFont(font)
        self.currRankLabel.setObjectName("currRankLabel")
        self.currentRank = QtWidgets.QLabel(self.centralwidget)
        self.currentRank.setGeometry(QtCore.QRect(370, 130, 220, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.currentRank.setFont(font)
        self.currentRank.setAlignment(QtCore.Qt.AlignCenter)
        self.currentRank.setObjectName("currentRank")
        self.shuffleButton = QtWidgets.QPushButton(self.centralwidget)
        self.shuffleButton.setGeometry(QtCore.QRect(30, 100, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.shuffleButton.setFont(font)
        self.shuffleButton.setObjectName("shuffleButton")
        self.addWordLE = QtWidgets.QLineEdit(self.centralwidget)
        self.addWordLE.setGeometry(QtCore.QRect(115, 290, 220, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.addWordLE.setFont(font)
        self.addWordLE.setObjectName("addWordLE")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBar.setFont(font)
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(QtCore.Qt.RightToolBarArea|QtCore.Qt.TopToolBarArea)
        self.toolBar.setOrientation(QtCore.Qt.Vertical)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.actionSave_Blank = QtWidgets.QAction(MainWindow)
        self.actionSave_Blank.setObjectName("actionSave_Blank")
        self.action_Rank_Thresholds = QtWidgets.QAction(MainWindow)
        self.action_Rank_Thresholds.setObjectName("action_Rank_Thresholds")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_New = QtWidgets.QAction(MainWindow)
        self.action_New.setObjectName("action_New")
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.actionLoad)
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionSave_Blank)
        self.menu_File.addAction(self.action_Exit)
        self.menu_Help.addAction(self.actionAbout)
        self.menu_Help.addAction(self.action_Rank_Thresholds)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionLoad)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_Blank)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addAction(self.action_Rank_Thresholds)

        self.retranslateUi(MainWindow)
        self.shuffleButton.clicked.connect(self.shuffle)
        self.addWordButton.clicked.connect(self.submit)
        self.actionSave.triggered.connect(self.saved)
        self.actionSave_Blank.triggered.connect(self.savedBlank)
        self.actionLoad.triggered.connect(self.load)
        self.addWordButton.clicked.connect(self.addWordLE.clear) # type: ignore
        self.addWordLE.returnPressed.connect(self.addWordButton.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addWordButton.setText(_translate("MainWindow", "Add Word"))
        self.foundWords.setText(_translate("MainWindow", "Found Words:"))
        self.currRankLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Current Rank:</span></p></body></html>"))
        self.currentRank.setText(_translate("MainWindow", "Beginner"))
        self.shuffleButton.setText(_translate("MainWindow", "Shuffle"))
        self.addWordLE.setPlaceholderText(_translate("MainWindow", "Type here or click letters!"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionLoad.setText(_translate("MainWindow", "&Load"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionAbout.setText(_translate("MainWindow", "&Help Menu"))
        self.action_About.setText(_translate("MainWindow", "&About"))
        self.actionSave_Blank.setText(_translate("MainWindow", "Save &Blank"))
        self.action_Rank_Thresholds.setText(_translate("MainWindow", "&Rank Thresholds"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_New.setText(_translate("MainWindow", "&New"))


    def savedBlank(self):
        if (self.newPuzzle != None):
            save = {
                "baseWord": list(self.newPuzzle.letterList),
                "foundWords" : list(),
                "playerPoints": 0,
                "requiredLetter": self.newPuzzle.specialLetter,
                "maxPoints": self.newPuzzle.totalScore
            }
            file_path = self.addWordLE.text() + ".json"
            with open(file_path, "w") as outfile:
                json.dump(save, outfile)

    def saved(self):
        if (self.newPuzzle != None):
            save = {
                "baseWord": list(self.newPuzzle.letterList),
                "foundWords" : list(self.newPuzzle.getFoundWordList()),
                "playerPoints": self.newPuzzle.getCurrentScore(),
                "requiredLetter": self.newPuzzle.specialLetter,
                "maxPoints": self.newPuzzle.totalScore
            }
            file_path = self.addWordLE.text() + ".json"
            with open(file_path, "w") as outfile:
                json.dump(save, outfile)
        

    def shuffle(self):
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

    def submit(self):
        if(not self.newPuzzle):
            if len(self.addWordLE.text())==7 and DictInterface.isValid(self.addWordLE.text()):
                uniqueCharacters=set()
            for i in self.addWordLE.text():
                uniqueCharacters.add(i)
            self.newPuzzle = puzzle(uniqueCharacters)
            loopedLetters = self.newPuzzle.getNormalLetters()
            addLetters = []
            for i in loopedLetters:
                addLetters.append(i)
            self.letter1.setText(addLetters[0])
            self.letter2.setText(addLetters[1])
            self.letter3.setText(addLetters[2])
            self.letter4.setText(addLetters[3])
            self.letter5.setText(addLetters[4])
            self.letter6.setText(addLetters[5])
            self.specialLetter.setText(self.newPuzzle.specialLetter)
        else:
            result = self.addWordLE.text()
            letterList = self.newPuzzle.getLetterList()
            foundList = self.newPuzzle.getFoundWordList()
            valid = True
            if DictInterface.isValid(result) and result not in foundList:
                for i in result:
                    if i not in letterList:
                        valid = False
                if valid:
                    print('Good')
                    self.newPuzzle.addFoundWord(result)
                    self.newPuzzle.addScore(1)
                    words = ""
                    for i in self.newPuzzle.listOfFoundWords:
                        words = words + "," + i
                    self.foundWords.setText(words)
                    self.currentRank.setText(self.newPuzzle.getCurrentScoreType()+"")
                    
    def notGood():
        print('Not Good')
            
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
            self.newPuzzle = puzzle(letters)
            self.newPuzzle.currentScore = score
            self.newPuzzle.listOfFoundWords = set(words)
            self.newPuzzle.specialLetter = special_letter

            print('here')
            self.letter1.setText(self.newPuzzle.letterList[1])
            self.letter2.setText(self.newPuzzle.letterList[2])
            self.letter3.setText(self.newPuzzle.letterList[3])
            self.letter4.setText(self.newPuzzle.letterList[4])
            self.letter5.setText(self.newPuzzle.letterList[5])
            self.letter6.setText(self.newPuzzle.letterList[6])
            self.specialLetter.setText(self.newPuzzle.specialLetter)
            words = ""
            for i in self.newPuzzle.listOfFoundWords:
                words = words + "," + i
                self.foundWords.setText(words)