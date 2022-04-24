import sys

# PyQT5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import mysql.connector

 
class Window(QWidget):
    def __init__(self) -> None:
        QWindow.__init__(self)
        
        # Setting The Window
        self.setWindowTitle("Sign In")
        self.setMaximumHeight(450);
        self.setMinimumHeight(450);
        self.setMaximumWidth(450);
        self.setMinimumWidth(450);
        
        # Layouts
        self.QV = QVBoxLayout()
        self.QH0 = QHBoxLayout()
        self.QH1 = QHBoxLayout()
        
        self.SQH_start = QVBoxLayout()
        self.SQH_end = QVBoxLayout()
        self.SQH_end.addSpacing(163);
        

        # Setting the Layout        
        self.QV.addStretch(1);
        self.QV.setSpacing(30);


        # Putting the Header    
        title = QLabel("Business Title")
        title.setFont(QFont('Ariel', 22))
        self.QV.addWidget(title);

        # USERNAME
        labelUsername = QLabel("Username:")        
        self.userTextInput = QTextEdit();
        self.userTextInput.setMaximumSize(400,20)
        self.QH0.addWidget(labelUsername)
        self.QH0.addWidget(self.userTextInput)
        
        # PASSWORD
        labelPassword = QLabel("Password:")       
        self.passTextInput = QTextEdit();
        self.passTextInput.setMaximumSize(400,20)
        self.QH1.addWidget(labelPassword)
        self.QH1.addWidget(self.passTextInput)
        
        buttonLogIn = QPushButton("Log In", self)
        self.QV_button = QVBoxLayout();
        self.QV_button.addWidget(buttonLogIn);
        
        self.QV.setSpacing(10);
        self.setLayout(self.QV);
        self.QV.addLayout(self.SQH_start);
        self.QV.addLayout(self.QH0);
        self.QV.addLayout(self.QH1);
        self.QV.addLayout(self.QV_button)
        self.QV.addLayout(self.SQH_end);
        
        # EVENTS
        buttonLogIn.clicked.connect(self.SignInfunction)
    
    def SignInfunction(self):
        if self.checkConnection(self.userTextInput.toPlainText(), self.passTextInput.toPlainText()):
            print("success")
        else:
            print("failed")

    def checkConnection(self, name, passw):
        print(name)
        print(passw);
        try:
           db = mysql.connector.connect(host="localhost",user=name,password=passw)
           return True
        
        except:
           return False

# RUNNER
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())