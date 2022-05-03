from API.Database_API import *
from API.Login_API import *
from API.Select_API import *
from API.Table_API import *

class CRUD:
    def __init__(self) -> None:
        self.loginDetails = Login_API("Data/user/login.csv")
        # Database Stuff        
        self.db = Database_API(self.loginDetails.getUsername(), self.loginDetails.getPassword());
        self.db_list = self.__getDatabaseList()
        self.cursor = self.db.getCursor();
        
        # Table Stuff
        self.tb = Table_API(self.db.getDatabase());
        self.tb_name = "";
        self.tb_list = [];
        
        #select
        self.sl = Select_API(self.db.getDatabase(), self.tb);
        self.executeCommand("SET foreign_key_checks = 0;")


        

    # Database 
    def createDatabase(self, dbName):
        self.db.createDatabase(dbName)
    
    def useDatabase(self, dbName):
        self.db.useDatabase(dbName)
        # Get the database and Table List
        self.__populateServer();

    def getDatabase(self):
        return self.db.getDatabase();
    
    def getCursor(self):
        return self.db.getCursor();
        
    
    # Get the existsing Database List
    def getDatabaseList(self):
        return self.db_list;
    
    def deleteDatabase(self, dbName):
        self.db.deleteDatabase(dbName);
    
    
    def executeCommand(self, command):
        return self.db.executeCommand(command);
        self.__commit();

    # Tables
    def createTable(self, tableName, columnName, dataType, contraint):
        self.tb.createTable(tableName, columnName, dataType, contraint)
        if(self.tb_name == ""):
            self.tb_name = tableName;
    
    def createTable(self, tableName, command):
        self.tb.createTable(tableName,command);
    
    def useTable(self, tableName):
        self.tb_name = tableName;

    # Get the existsing Table List
    def getTableList(self):
        return self.tb_list
    
    
    def dropTable(self, tbName):
        return self.tb.dropTable(tbName)

    def addColumn(self, columnName, columnType):
        return self.tb.addColumn( self.tb_name, columnName, columnType)
    
    def removeColumn(self, columnName):
        return self.tb.removeColumn( self.tb_name, columnName)
    
    def changeType(self, columnName, dataType):
        return self.tb.changeType(self.tb_name, columnName, dataType)
    
    def insertValue(self, tbName, value):
        self.tb.insertValue(tbName,value)
        self.__commit()

    def insertValueDate(self, tbName, value, dateTime):
        self.tb.insertValueDate(tbName,value,dateTime)
        self.__commit()
    
    def getAttributeList(self, tableName):
        temp = self.tb.getAttributeList(tableName);
        self.__tb_fetchAllValue();
        # return the list
        return temp;
    
    def getAttributeTypes(self, tableName):
        temp = self.tb.getAttributeTypes(tableName);
        otherValue = self.tb.fetchAllValue();
        return temp;
    
    
    # Select
    def getAllData(self, tbName):
        return self.sl.getAllData(tbName);
    
    def getData(self, tbName, condition):
        return self.sl.getData( tbName, condition);
    
    def getDataFrom(self, tbName, columnName):
        temp = self.sl.getDataFrom( tbName, columnName);
        otherValue = self.tb.fetchAllValue();
        return temp;
    
    def getSpecificData(self, tbName, attName, operation, condition):
        temp = self.sl.getSpecificData(tbName, attName, operation, condition);
        otherValue = self.tb.fetchAllValue();
        return temp;
    
    def getDataCommand(self, tbName, command):
        temp = self.sl.getDataCommand(tbName, command);
        otherValue = self.tb.fetchAllValue();
        return temp;
        
    
    def getDataGroupedByCondition(self, tbName, condition, conditionGroup):
        return self.sl.getDataGroupedBy(  tbName, condition, conditionGroup);
    
    def getDataSortedBy(self, tbName, conditionGroup):
        temp = self.sl.getDataSortedBy(tbName, conditionGroup);
        otherValue = self.tb.fetchAllValue();
        return temp;
    
    def getDataGroupedBy(self, tbName, conditionGroup):
        return self.sl.getDataGroupedBy(tbName, conditionGroup);
    
    def getDataSortedByCondition(self, tbName, condition, conditionSort):
        return self.sl.getDataSortedByCondition(tbName, condition, conditionSort);
    
    def changeData(self, command):
        if len(command) < 1:
            pass
        else:
            self.sl.changeData(command);
            # Commit the changes into the selected Database
            self.__commit();

    def deleteItem(self, tableName, attName, value):
        temp = self.sl.deleteItem( tableName, attName, value);
        otherValue = self.tb.fetchAllValue();
        self.__commit();
        return temp;
    


    
    # Server Stuff
    
    def __tb_fetchAllValue(self):
        return self.tb.fetchAllValue();

    def __db_fetchAllValue(self):
        return self.tb.fetchAllValue();
    
    def __getDatabaseList(self):
        return self.db.getDatabaseList();
    
    def __getTableList(self):
        return self.tb.getTableList()
    
    def __populateServer(self):
        self.tb_list = self.__getTableList()
        if len(self.tb_list) > 0:
            self.tb_name = self.tb_list[0];
        else:
            # Debugging Purposes, Can be remove
            print("WARNING!! There are no table seen")
            pass

    def __commit(self):
        self.db.getDatabase().commit();
        