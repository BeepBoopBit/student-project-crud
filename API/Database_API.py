from dataclasses import dataclass
import MySQLdb

class Database:
    def __init__(self) -> None:
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            password="@M0cbRAMySQL073cb0M"
        )
        self.cursor = self.db.cursor()
    
    #######################################################
    
    # Use Functions    
    def useDatabase(self, dbName):
        self.cursor.execute(f"USE {dbName}")    
        
    # Getters Function
    def getDatabaseList(self):
        self.cmShowDatabase()
        return self.cursor;
    
    def getTables(self):
        self.cursor.execute("SHOW TABLES;")
        return self.cursor
    
    def getDatabase(self):
        return self.db
        
    #######################################################
    
    # auxiliary Function
    def cmShowDatabase(self):
        self.cursor.execute("SHOW DATABASES");
    
    # Debugging Purposes
    def Print_Database(self):
        self.cursor.execute("SHOW DATABASES;")
        print(type(self.cursor));
        for x in self.cursor:
            print(x)
