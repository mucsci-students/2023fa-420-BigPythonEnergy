import sys


from PyQt5.QtWidgets import (

    QApplication, QDialog, QMainWindow, QMessageBox

)

from PyQt5.uic import loadUi


from MainWindowUI import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
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

class blankSaveDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/blankSaveMenu.ui", self)

class newGameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/newGame.ui", self)

class thresholdDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("BigPythonEnergy/ui/rankThresholds.ui", self)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    win = Window()

    win.show()

    sys.exit(app.exec())