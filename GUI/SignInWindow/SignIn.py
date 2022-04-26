import csv
import os
import mysql.connector
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

# GUI
from GUI.globalVariable import *
from GUI.DatabaseWindow.Database import *
from GUI.CrudWindow.Main import *
from GUI.CrudWindow.TableWindow import *
from GUI.CrudWindow.FilterTable import *
from GUI.CrudWindow.Grouping import *
from GUI.CrudWindow.ModifyTable import *

# SignIn Class

class SignIn(QDialog):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super(SignIn, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\SignIn.ui"
        self.ui = loadUi(UIPATH, self)
        self.SignInbutton.clicked.connect(self.SignInfunction)
        self.API = CRUD();

    # PopUp message set-up

    def pop_message(self, text=""): 
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    # SignIn Process

    def SignInfunction(self): 
        if self.checkConnection(self.userName.text(), self.userPassword.text()):
            self.pop_message(text="Login Succesfully, Welcome!")

            # Exporting Data.csv

            with open(os.path.dirname(os.path.realpath(__file__)) + "\\..\\..\\Data\\user\\login.csv", 'w') as f:
                writer = csv.writer(f)
                writer.writerow(
                    [self.userName.text(), self.userPassword.text()])

            #Switch Database -> #1

            Widget.addWidget(Database(self.API))
            Widget.setCurrentIndex(1)
        else:
            self.pop_message("Login Failed, Please Try Again")

    # Checking connection mysql

    def checkConnection(self, name, passw):
        try:
            db = mysql.connector.connect(host="localhost", user=name,password=passw)
            return True
        except:
            return False