import os
from tkinter import Widget
from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *

from GUI.CrudWindow.Main import *
from GUI.CrudWindow.TableWindow import *
from GUI.CrudWindow.Grouping import *
from GUI.CrudWindow.ModifyTable import *
import traceback

# Database Class

class Database(QMainWindow):
    def __init__(self, apiCrud):
        super(Database, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateDatabaseMenu.ui" 
        self.ui = loadUi(UIPATH,self)
        self.createDatabaseButton.clicked.connect(self.createDatabase)                      # Create Database
        self.useDatabaseButton.clicked.connect(self.useDatabase)                            # Use Database
        self.deleteDatabaseButton.clicked.connect(self.deleteDatabase)                      # Delete Database
        self.signOutButton.clicked.connect(self.signOut)                                    # Return SignIn -> #0

        # Assumes that everything is working properly in the Log-in side

        self.API = apiCrud;
        self.readDatabase();
        
    # Read Database
        
    def readDatabase(self):
        databaseList = self.API.getDatabaseList()
        for data in databaseList:
            self.insertInTable(data);
    
    # Insert Database

    def insertInTable(self,data) :
        rowPosition = self.tableWidget.rowCount();
        self.tableWidget.insertRow(rowPosition);
        self.tableWidget.setItem(rowPosition,0,QTableWidgetItem(data))
    
    # Use Database

    def useDatabase(self): 
        r = self.tableWidget.currentRow()
        selectedDatabase = self.tableWidget.item(r,0).text();
        try:
            self.API.useDatabase(selectedDatabase);
            with open("Data/database/databaseName.dat", 'w') as f:
                f.write(selectedDatabase);
            Widget.addWidget(CreateDatabase(self.API))       #2  (Create)

            # CRUD
            Widget.addWidget(MainCrudWindow(self.API, selectedDatabase)); #3
            Widget.addWidget(GroupingTable(self.API)); #4
            Widget.addWidget(ModifyTable(self.API)); #5
            # TABLE
            Widget.addWidget(NameTable(self.API)); #6
            Widget.addWidget(TableMenu(self.API)); #7
            Widget.addWidget(TableColumn(self.API)); #8
            Widget.addWidget(ForeignKey(self.API)); #9
            
            
            Widget.setCurrentIndex(3)
            
        except Exception:
            print(traceback.format_exc())
            print("READING DATABASE ERROR: please report this problem")

    # Delete Database 

    def deleteDatabase(self):
        self.pop_message(text="Database Successfully Deleted!") 
        r = self.tableWidget.currentRow()
        selectedDatabase = self.tableWidget.item(r,0).text();
        self.API.deleteDatabase(selectedDatabase);
        self.tableWidget.removeRow(r);

    # Create Database 

    def createDatabase(self): 
        Widget.setCurrentIndex(2)
        pass
    
    # Signout 

    def signOut(self): 
        Widget.setCurrentIndex(0)

    # PopUp Message Setup

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec()

# Create Database UI Class

class CreateDatabase(QDialog):
    def __init__(self, apiCrud):
        super(CreateDatabase, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateDatabase.ui" 
        self.ui = loadUi(UIPATH,self)
        self.okButton.clicked.connect(self.okButtonFunc) 
        self.cancelButton.clicked.connect(self.cancelButtonFunc)
        self.API = apiCrud;

    # OK Button

    def okButtonFunc(self): 
        self.pop_message(text="Database Successfully Created!") 
        dbName = self.databaseName.toPlainText()
        self.API.createDatabase(dbName)
        Widget.widget(2).insertInTable(dbName);
        self.cancelButtonFunc();

    # PopUp Message Setup

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec()

    # Cancel Button

    def cancelButtonFunc(self):
        Widget.setCurrentIndex(1)
    