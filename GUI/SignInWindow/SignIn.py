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

# SignIn Process of the Program
class SignIn(QDialog):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        super(SignIn, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\SignIn.ui"
        self.ui = loadUi(UIPATH, self)
        self.SignInbutton.clicked.connect(self.SignInfunction)

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def SignInfunction(self):
        if self.checkConnection(self.userName.text(), self.userPassword.text()):
            self.pop_message(text="Login Succesfully, Welcome!")
            # Exporting Data
            with open(os.path.dirname(os.path.realpath(__file__)) + "\\..\\..\\Data\\user\\login.csv", 'w') as f:
                writer = csv.writer(f)
                writer.writerow(
                    [self.userName.text(), self.userPassword.text()])
            # Sign-in #0
            #Database
            Widget.addWidget(Database()) #1
            Widget.addWidget(CreateDatabase()) #2
            
            # CRUD
            Widget.addWidget(MainCrudWindow()); #3
            Widget.addWidget(FilterTable()); #4
            Widget.addWidget(GroupingTable()); #5
            Widget.addWidget(ModifyTable()); #6
            
            # TABLE
            Widget.addWidget(NameTable()); #7
            Widget.addWidget(TableMenu()); #8
            Widget.addWidget(TableColumn()); #9
            Widget.addWidget(ForeignKey()); #10
            
            Widget.setCurrentIndex(1)
        else:
            self.pop_message("Login Failed, Please Try Again")

    def checkConnection(self, name, passw):
        try:
            db = mysql.connector.connect(host="localhost", user=name,password=passw)
            return True
        except:
            return False