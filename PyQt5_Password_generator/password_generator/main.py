from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5 import QtGui
import sys
import random_pass as rp
import logging

logging.basicConfig(filename="passwords.txt", format="%(message)s", level=logging.INFO)

with open("showMessage", "r") as f:
    showM = f.read()
    if showM == "1":
        showM = True
    else:
        showM = False


class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.x = 500
        self.y = 500
        self.title = "password-gen"


    def start(self):
        self.setGeometry(100, 100, self.x, self.y)
        self.setWindowTitle(self.title)
        self.setFixedSize(self.x, self.y)
        self.setWindowIcon(QtGui.QIcon("lock.png"))

        self.label1 = QLabel(self)
        self.label1.setText("characters:")
        self.label1.move(190, 50)

        self.charsInput = QLineEdit(self)
        self.charsInput.setText("a,b,c,d")
        self.charsInput.setGeometry(190, 100, 100, 30)

        self.label2 = QLabel(self)
        self.label2.setText("length:")
        self.label2.move(190, 150)

        self.passLength = QLineEdit(self)
        self.passLength.setText("5")
        self.passLength.move(190, 200)

        self.button1 = QPushButton(self)
        self.button1.setText("generate password")
        self.button1.clicked.connect(self.generatePassword)
        self.button1.setGeometry(170, 240, 150, 30)


        self.deletePassButton = QPushButton(self)
        self.deletePassButton.setText("Delete")
        self.deletePassButton.setGeometry(10, 460, 120, 30)
        self.deletePassButton.clicked.connect(self.deletePopUp)
        self.show()


    def generatePassword(self): 
        global showM
        self.chars = self.charsInput.text().split(",")
        self.passLen = int(self.passLength.text())

        self.password = rp.randomPass(self.chars, self.passLen)

        logging.info(f"password: {self.password} ")
    
        if showM:
            self.messageBox()


    def messageBox(self):
        message = QMessageBox()
        message.setText("The password was written to password.txt, show this again?")
        message.setWindowTitle("password")
        message.setIcon(QMessageBox.Question)
        message.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        message.buttonClicked.connect(self.YesNo)


        x = message.exec_()

    def YesNo(self, button):
        if button.text() == "&Yes":
            pass
        elif button.text() == "&No":
            with open("showMessage", "w") as f:
                f.write("0")

    

    def deletePasswords(self, button):
        if button.text() == "&Yes":
            try:
                with open("passwords.txt", "w") as f:
                    f.write("")
            except:
                raise FileNotFoundError("password file not found please press generate password")


    def deletePopUp(self):
        message = QMessageBox()
        message.setText("Are you shure you want to delete all the passwords")
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Cancel)
        message.buttonClicked.connect(self.deletePasswords)

        x = message.exec_()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    win = window()
    win.start()


    sys.exit(app.exec_())
