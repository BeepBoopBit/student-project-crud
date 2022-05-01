import os
from tkinter import Widget
from PyQt5.QtWidgets import QDialog, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *

from GUI.CrudWindow.Main import *
from GUI.CrudWindow.Table.MainTable.TableWindow import *
from GUI.CrudWindow.Grouping.Grouping import *
from GUI.CrudWindow.Table.ModifyTable.ModifyTable import *
from GUI.CrudWindow.Sort.Sort import * 
from GUI.CrudWindow.Search.Search import *
import traceback

# Database Class

class Database(QMainWindow):
    def __init__(self, apiCrud):
        super(Database, self).__init__()
        UI_PATH = "GUI\\DatabaseWindow\\CreateDatabaseMenu.ui" 
        self.ui = loadUi(UI_PATH,self)
        
        # Initialize Signals
        self.createDatabaseButton.clicked.connect(self.createDatabase)
        self.useDatabaseButton.clicked.connect(self.useDatabase)
        self.deleteDatabaseButton.clicked.connect(self.deleteDatabase)
        self.signOutButton.clicked.connect(self.signOut)

        # Initialize API
        self.API = apiCrud;
        
        # Read the Database
        self.readDatabase();
    
    def truncateFiles(self):
        
        alterFile = open("Data/database/alterCommand.dat", 'w')
        alterFile.truncate()
        alterFile.close()
        
        attListFile = open("Data/database/attributeList.dat", 'w')
        attListFile.truncate()
        attListFile.close()
        
        attTypeFile = open("Data/database/attributeType.dat", 'w')
        attTypeFile.truncate()
        attTypeFile.close()
    
        colName = open("Data/createTable/columnName.dat", 'w')
        colName.truncate()
        colName.close()
        
        command = open("Data/createTable/command.dat", 'w')
        command.truncate()
        command.close()
        
        constraints = open("Data/createTable/constraints.dat", 'w')
        constraints.truncate()
        constraints.close()
    
        dbName = open("Data/database/databaseName.dat", 'w')
        dbName.truncate()
        dbName.close()
    
        fkFile = open("Data/createTable/fk.dat", 'w')
        fkFile.truncate()
        fkFile.close()
        
        indexChange = open("Data/database/indexChange.dat", 'w')
        indexChange.truncate()
        indexChange.close()
        
        loginFile = open("Data/user/login.dat", 'w')
        loginFile.truncate();
        loginFile.close();
        
        selectCommand = open("Data/database/selectCommand.dat", 'w')
        selectCommand.truncate()
        selectCommand.close()
        
        tableName = open("Data/createTable/tableName.dat", 'w')
        tableName.truncate()
        tableName.close()
        
        typeName = open("Data/createTable/type.dat", 'w')
        typeName.truncate()
        typeName.close()
        
        tName = open("Data/database/tableList.dat", 'w')
        tName.truncate()
        tName.close()
    

    # Read Database
    def readDatabase(self):
        # Get the list of Databases
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
        
        self.truncateFiles()
        
        # Get selected database
        currentTableRow = self.tableWidget.currentRow()
        selectedDatabase = self.tableWidget.item(currentTableRow,0).text();
        
        # Try to load the
        try:
            self.API.useDatabase(selectedDatabase);
            with open("Data/database/databaseName.dat", 'w') as f:
                f.write(selectedDatabase);
                

            # CRUD
            Widget.addWidget(MainCrudWindow(self.API, selectedDatabase)); #3
            Widget.addWidget(GroupingTable(self.API)); #4
            Widget.addWidget(ModifyTable(self.API)); #5
            
            # TABLE
            Widget.addWidget(NameTable(self.API)); #6
            #Widget.addWidget(CreateTableName(self.API)); #6
            Widget.addWidget(TableMenu(self.API)); #7
            Widget.addWidget(TableColumn(self.API)); #8
            Widget.addWidget(ForeignKey(self.API)); #9
            #Widget.addWidget(TableForeignKey(self.API)); #9
            Widget.addWidget(SelectAddAttribute(self.API)) # 10
            
            Widget.addWidget(SortTable(self.API)) # 11
            Widget.addWidget(SortSelectAddAttribute(self.API)) # 12
            Widget.addWidget(SearchingTable(self.API)) # 13
            Widget.addWidget(SearchAddAttribute(self.API)) # 14
            
            Widget.widget(3).loadData()
            Widget.setCurrentIndex(3)
            
        except Exception:
            pop_message("ERROR: Using Database")
            print(traceback.format_exc())

    # Delete Database 

    def deleteDatabase(self):
        
        # Get the selected Database
        currentTableRow = self.tableWidget.currentRow()
        selectedDatabase = self.tableWidget.item(currentTableRow,0).text();
        
        # Delete the database
        self.API.deleteDatabase(selectedDatabase);
        
        # Remove the row from the tableWidget
        self.tableWidget.removeRow(currentTableRow);
        
        pop_message("Database Successfully Deleted!") 
        

    # Create Database 
    def createDatabase(self): 
        Widget.setCurrentIndex(2)
        Widget.show();
    
    # Signout 

    def signOut(self): 
        Widget.setCurrentIndex(0)

# Create Database UI Class

class CreateDatabase(QDialog):
    def __init__(self, apiCrud):
        super(CreateDatabase, self).__init__()
        UI_PATH = "GUI\\DatabaseWindow\\CreateDatabase.ui" 
        self.ui = loadUi(UI_PATH,self)
        self.okButton.clicked.connect(self.okButtonFunc) 
        self.cancelButton.clicked.connect(self.cancelButtonFunc)
        self.API = apiCrud;

    # OK Button

    def okButtonFunc(self): 
        self.pop_message(text="Database Successfully Created!") 
        dbName = self.databaseName.toPlainText()
        Widget.widget(1).insertInTable(dbName);
        self.API.createDatabase(dbName)
        self.cancelButtonFunc();

    # PopUp Message Setup

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec()

    # Cancel Button

    def cancelButtonFunc(self):
        Widget.setCurrentIndex(1)
    