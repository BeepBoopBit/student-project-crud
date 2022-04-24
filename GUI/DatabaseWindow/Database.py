from re import L
import sys, os
import mysql.connector
from tkinter import Widget
from turtle import width
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *

sys.path.append("C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT")
from CRUD_API import CRUD


#Database Class
class Database(QMainWindow):
    def __init__(self):
        super(Database, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateDatabaseMenu.ui" 
        self.ui = loadUi(UIPATH,self)
        self.createDatabaseButton.clicked.connect(self.createDatabase) #Create Database Button
        self.useDatabaseButton.clicked.connect(self.useDatabase) #Use Database Button
        self.signOutButton.clicked.connect(self.signOut) #Go back to Signin
        # Assumes that everything is working properly in the Log-in side
        self.API = CRUD();
        self.readDatabase();
        
    def readDatabase(self):
        databaseList = self.API.getDatabaseList()
        for data in databaseList:
            rowPosition = self.tableWidget.rowCount();
            self.tableWidget.insertRow(rowPosition);
            self.tableWidget.setItem(rowPosition,0,QTableWidgetItem(data))
        
    def useDatabase(self): ##Use DB
        r = self.tableWidget.currentRow()
        selectedDatabase = self.tableWidget.item(r,0).text();
        try:
            self.API.useDatabase(selectedDatabase);
        except:
            print("READING DATABASE ERROR: please report this problem")
        print(f"Successfully Linked {selectedDatabase}");
        
        
    def createDatabase(self): ##Create DB
        pass
    
    def signOut(self): ##Signout
        Widget.setCurrentIndex(Widget.currentIndex()-1)
        
