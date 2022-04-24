from ast import While
import email
import sys
import sqlite3
from tkinter import Widget
from turtle import goto, width
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import os
import mysql.connector

#Database Class
class Database(QMainWindow):
    def __init__(self):
        super(Database, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateDatabaseMenu.ui" 
        self.ui = loadUi(UIPATH,self)
        self.createdbbutton.clicked.connect(self.createDatabase) #Create Database Button
        self.usedbbutton.clicked.connect(self.useDatabase) #Use Database Button
        self.signoutbutton.clicked.connect(self.gotosignout) #Go back to Signin
        
    def useDatabase(self, dbName): ##Use DB
        self.cursor.execute(f"USE {dbName}")    
        
    def createDatabase(self, dbName): ##Create DB
        self.cursor.execute(f"CREATE DATABASE {dbName}")
    
    def gotosignout(self): ##Signout
        gotosignout = SignIn()
        Widget.addWidget(gotosignout)
        Widget.setCurrentIndex(Widget.currentIndex()+1)

#Signout and Signin Process of the Program
class SignIn(QDialog):
    def __init__(self):
        super(SignIn, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\SignIn.ui" 
        self.ui = loadUi(UIPATH,self)
        self.SignInbutton.clicked.connect(self.SignInfunction)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def SignInfunction(self):
        if self.checkConnection(self.userName.text(), self.userPassword.text()):
           self.pop_message(text="Login Succesfully, Welcome!")
        else:
            self.pop_message("Login Failed, Please Try Again")

    def checkConnection(self, name, passw):
        try:
           db = mysql.connector.connect(host="localhost",user=name,password=passw)
           return True
        
        except:
           return False

app=QApplication(sys.argv)
mainwindow=Database()
Widget=QtWidgets.QStackedWidget()
Widget.addWidget(mainwindow)
Widget.setFixedWidth(600)
Widget.setFixedHeight(350)
Widget.show()
app.exec()
