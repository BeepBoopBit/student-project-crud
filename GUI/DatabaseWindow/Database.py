import os
from tkinter import Widget
from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *

from GUI.CrudWindow.Main import *
from GUI.CrudWindow.TableWindow import *
from GUI.CrudWindow.FilterTable import *
from GUI.CrudWindow.Grouping import *
from GUI.CrudWindow.ModifyTable import *
import traceback

#Database Class
class Database(QMainWindow):
    def __init__(self, apiCrud):
        super(Database, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateDatabaseMenu.ui" 
        self.ui = loadUi(UIPATH,self)
        self.createDatabaseButton.clicked.connect(self.createDatabase) #Create Database Button
        self.useDatabaseButton.clicked.connect(self.useDatabase) #Use Database Button
        self.signOutButton.clicked.connect(self.signOut) #Go back to Sign-in
        self.deleteDatabaseButton.clicked.connect(self.deleteDatabase)
        # Assumes that everything is working properly in the Log-in side
        self.API = apiCrud;
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
            with open("Data/database/databaseName.dat") as f:
                f.write(selectedDatabase);
            Widget.addWidget(CreateDatabase(self.API)) #2
            # CRUD
            Widget.addWidget(MainCrudWindow(self.API)); #3
            Widget.addWidget(FilterTable(self.API)); #4
            Widget.addWidget(GroupingTable(self.API)); #5
            Widget.addWidget(ModifyTable(self.API)); #6
            # TABLE
            Widget.addWidget(NameTable(self.API)); #7
            Widget.addWidget(TableMenu(self.API)); #8
            Widget.addWidget(TableColumn(self.API)); #9
            Widget.addWidget(ForeignKey(self.API)); #10
            
            
            Widget.setCurrentIndex(3)
            
        except Exception:
            print(traceback.format_exc())
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
    def __init__(self, apiCrud):
        super(CreateDatabase, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateDatabase.ui" 
        self.ui = loadUi(UIPATH,self)
        self.okButton.clicked.connect(self.okButtonFunc) 
        self.cancelButton.clicked.connect(self.cancelButtonFunc)
        self.API = apiCrud;

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
    