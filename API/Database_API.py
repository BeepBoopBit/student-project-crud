from itertools import islice
from re import X
import mysql.connector

class Database_API:
    def __init__(self, userName, userPassword) -> None:
        self.db = mysql.connector.connect(
            host="localhost",
            user=userName,
            password=userPassword
        )
        self.cursor = self.db.cursor(dictionary=True)
        
    #######################################################
    # Use Functions    
    def useDatabase(self, dbName):
        self.cursor.execute(f"USE {dbName}")    
        
    def createDatabase(self, dbName):
        self.cursor.execute(f"CREATE DATABASE {dbName}")
    
    def deleteDatabase(self, dbName):
        self.cursor.execute(f"DROP DATABASE {dbName}")

    def executeCommand(self, command):
        self.cursor.execute(command);
        return self.cursor.fetchall();

    # Getters Function
    def getDatabase(self):
        return self.db
    
    def getCursor(self):
        return self.cursor;
    
    def getDatabaseList(self):
        self.cursor.execute("SHOW DATABASES");
        return self.__formatValue()
    
    # Auxillary
    def __formatValue(self):
        temp = []
        for i in self.cursor.fetchall():
            for j in i.values():
                temp.append(j);
        return temp;
