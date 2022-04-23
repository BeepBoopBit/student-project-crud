import sys
from tkinter.filedialog import Open
from API.Database_API import Database
from API.Login_API import Login
from API.Table_API import Table

import csv

class CRUD:
    def __init__(self) -> None:
        self.loginDetails = Login("Data/user/login.csv")
        # Database Stuff        
        self.db = Database(self.loginDetails.getUsername(), self.loginDetails.getPassword());
        self.db_list = [];
        self.cursor = self.db.getCursor();
        # Table Stuff
        self.tb = Table(self.db.getDatabase());
        self.tb_name = "";
        self.tb_list = [];

    # Database 
    def useDatabase(self, dbName):
        self.db.useDatabase(dbName)
        self.__populateServer();
    
    def createDatabase(self, dbName):
        self.db.createDatabase(dbName)

    def getDatabase(self):
        return self.db.getDatabase();
    
    def getCursor(self):
        return self.db.getCursor();
        
    def getDatabaseList(self):
        return self.db.getDatabaseList();
    
    
    # Tables
    def createTable(self, tableName, columnName, dataType, contraint):
        self.tb.createTable(tableName, columnName, dataType, contraint)
        if(self.tb_name == ""):
            self.tb_name = tableName;
    
    def useTable(self, tableName):
        self.tb_name = tableName;

    def getTableList(self):
        return self.tb.getTableList()
    
    def dropTable(self):
        return self.tb.dropTable()

    def addColumn(self, columnName, columnType):
        return self.tb.addColumn( self.tb_name, columnName, columnType)
    
    def removeColumn(self, columnName):
        return self.tb.removeColumn( self.tb_name, columnName)
    
    def changeType(self, columnName, dataType):
        return self.tb.changeType(self.tb_name, columnName, dataType)
        
        
    # Server Stuff
    def __populateServer(self):
        for i in self.getDatabaseList():
            self.db_list.append("%s" % i)
        for i in self.getTableList():
            self.db_list.append("%s" % i)
        if len(self.tb_name) > 0:
            self.tb_name = self.tb_list[0];
        else:
            print("WARNING!! A Table is used without any table")
        
            
        