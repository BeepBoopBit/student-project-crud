import sys, os
sys.path.append("C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT")

from tkinter import Widget
from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *
from CRUD_API import CRUD



#Database Class
class Database(QMainWindow):
    def __init__(self):
        super(Database, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateDatabaseMenu.ui" 
        self.ui = loadUi(UIPATH,self)
        self.createDatabaseButton.clicked.connect(self.createDatabase) #Create Database Button
        self.useDatabaseButton.clicked.connect(self.useDatabase) #Use Database Button
        self.signOutButton.clicked.connect(self.signOut) #Go back to Sign-in
        self.deleteDatabaseButton.clicked.connect(self.deleteDatabase)
        # Assumes that everything is working properly in the Log-in side
        self.API = CRUD();
        self.readDatabase();
        
    def readDatabase(self):
        databaseList = self.API.getDatabaseList()
        for data in databaseList:
            self.insertInTable(data);
    
    def insertInTable(self,data) :
        rowPosition = self.tableWidget.rowCount();
        self.tableWidget.insertRow(rowPosition);
        self.tableWidget.setItem(rowPosition,0,QTableWidgetItem(data))
    
    def useDatabase(self): ##Use DB
        r = self.tableWidget.currentRow()
        selectedDatabase = self.tableWidget.item(r,0).text();
        try:
            self.API.useDatabase(selectedDatabase);
            Widget.setCurrentIndex(3)
        except:
            print("READING DATABASE ERROR: please report this problem")
        
    def deleteDatabase(self):
        self.pop_message(text="Database Successfully Deleted!") 
        r = self.tableWidget.currentRow()
        selectedDatabase = self.tableWidget.item(r,0).text();
        self.API.deleteDatabase(selectedDatabase);
        self.tableWidget.removeRow(r);
    def createDatabase(self): ##Create DB
        Widget.setCurrentIndex(2)
        pass
    
    def signOut(self): ##Signout
        Widget.setCurrentIndex(0)
        
    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec()
#Create Database UI
class CreateDatabase(QDialog):
    def __init__(self):
        super(CreateDatabase, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateDatabase.ui" 
        self.ui = loadUi(UIPATH,self)
        self.okButton.clicked.connect(self.okButtonFunc) 
        self.cancelButton.clicked.connect(self.cancelButtonFunc)
        self.API = CRUD();

    def okButtonFunc(self): #rename kung ano yung name ng button
        self.pop_message(text="Database Successfully Created!") 
        dbName = self.databaseName.toPlainText()
        self.API.createDatabase(dbName)
        Widget.widget(2).insertInTable(dbName);
        self.cancelButtonFunc();

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec()

    def cancelButtonFunc(self):
        Widget.setCurrentIndex(1)
    