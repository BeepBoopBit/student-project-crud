import csv
import os
import mysql.connector

# PyQt5
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

# GUI
from GUI.globalVariable import *
from GUI.DatabaseWindow.Database import *

class SignIn(QDialog):
    def __init__(self):
        super(SignIn, self).__init__()
        UI_PATH = os.path.dirname(os.path.realpath(__file__)) + "\\SignIn.ui"
        self.ui = loadUi(UI_PATH, self)
        self.SignInButton.clicked.connect(self.SignInfunction)

    # SignIn Process
    def SignInfunction(self): 
        # Check if a connection is established
        if self.checkConnection(self.userName.text(), self.userPassword.text()):
            pop_message(text="Login Succesfully, Welcome!")

            # Try to Write in Data.csv
            try:
                with open(os.path.dirname(os.path.realpath(__file__)) + "\\..\\..\\Data\\user\\login.csv", 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(
                        [self.userName.text(), self.userPassword.text()])
            except Exception:
                pop_message("ERROR: Writing In SignIn")
                print(traceback.format_exc());
                
            # Initialize the API
            self.API = CRUD();
            
            # Try to create an instance of the Database Window 
            try:
                #Database index in Widget = '1'
                Widget.addWidget(Database(self.API))
                # Create Database Window                
                Widget.addWidget(CreateDatabase(self.API))  #2
                
                Widget.setFixedWidth(565)
                Widget.setFixedHeight(295)
            
                #Switch Database -> #1
                Widget.setCurrentIndex(1)
            except:
                pop_message("ERROR: Database Creation Error")
                print(traceback.format_exc());
                
            
        
        # Pop-up a failed Pop-up
        else:
            pop_message("Login Failed, Please Try Again")

    # Checking connection mysql

    def checkConnection(self, name, passw):
        # Try to establish a connection
        try:
            db = mysql.connector.connect(host="localhost", user=name,password=passw)
            return True
        except:
            return False