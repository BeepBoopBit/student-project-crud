from ast import While
import email
import sys
import sqlite3
from tkinter import Widget
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import os
import MySQLdb
import mysql.connector
from GUI.globalVariable import *
import csv
from GUI.DatabaseWindow.Database import *
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
            Widget.addWidget(Database())
            Widget.setCurrentIndex(Widget.currentIndex()+1)
        else:
            self.pop_message("Login Failed, Please Try Again")

    def checkConnection(self, name, passw):
        try:
            db = mysql.connector.connect(host="localhost", user=name,password=passw)
            return True
        except:
            return False