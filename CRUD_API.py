from API.Database_API import *
from API.Login_API import *
from API.Select_API import *
from API.Table_API import *

class CRUD:
    def __init__(self) -> None:
        self.loginDetails = Login_API("Data/user/login.csv")
        # Database Stuff        
        self.db = Database_API(self.loginDetails.getUsername(), self.loginDetails.getPassword());
        self.db_list = [];
        self.cursor = self.db.getCursor();
        # Table Stuff
        self.tb = Table_API(self.db.getDatabase());
        self.tb_name = "";
        self.tb_list = [];
        #select
        self.sl = Select_API(self.db.getDatabase(), self.tb);

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
    
    def deleteDatabase(self, dbName):
        self.db.deleteDatabase(dbName);
    
    # Tables
    def createTable(self, tableName, columnName, dataType, contraint):
        self.tb.createTable(tableName, columnName, dataType, contraint)
        if(self.tb_name == ""):
            self.tb_name = tableName;
    
    def createTable(self, tableName, command):
        self.tb.createTable(tableName,command);
    
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
    
    def insertValue(self, tbName, value):
        self.tb.insertValue(tbName,value)

    def insertValueDate(self, tbName, value, dateTime):
        self.tb.insertValueDate(tbName,value,dateTime)
    
    def getAttributeList(self, tableName):
        temp = self.tb.getAttributeList(tableName);
        otherValue = self.tb.fetchAllValue();
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
    
    def getDataGroupedBy(self, tbName, condition, conditionGroup):
        return self.sl.getDataGroupedBy(  tbName, condition, conditionGroup);
    
    def getDataSortedBy(self, tbName, condition, conditionSort):
        return self.sl.getDataSortedBy(tbName, condition, conditionSort);
    
    # Server Stuff
    def __populateServer(self):
        self.db_list = self.getDatabaseList()
        self.tb_list = self.getTableList()
        if len(self.tb_list) > 0:
            self.tb_name = self.tb_list[0];
        else:
            print("WARNING!! There are no table seen")
        
    def commit(self):
        self.db.getDatabase().commit();
        