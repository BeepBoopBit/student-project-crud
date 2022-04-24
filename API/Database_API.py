from dataclasses import dataclass
import mysql.connector

<<<<<<< HEAD
class Database_API:
    def __init__(self) -> None:
        self.db = MySQLdb.connect(
=======
class Database:
    def __init__(self, userName, userPassword) -> None:
        self.db = mysql.connector.connect(
>>>>>>> df239dbd14f5ccc5aa1091602ead0f400534044b
            host="localhost",
            user=userName,
            password=userPassword
        )
        self.cursor = self.db.cursor()
        
    #######################################################
    # Use Functions    
    def useDatabase(self, dbName):
        self.cursor.execute(f"USE {dbName}")    
        
    def createDatabase(self, dbName):
        self.cursor.execute(f"CREATE DATABASE {dbName}")

    # Getters Function
<<<<<<< HEAD
    def getDatabaseList(self):
        self.cmShowDatabase()
        return self.cursor;
    
    def getTables(self):
        self.cursor.execute("SHOW TABLES;")
        return self.cursor
    
    #######################################################
=======
    def getDatabase(self):
        return self.db
>>>>>>> df239dbd14f5ccc5aa1091602ead0f400534044b
    
    def getCursor(self):
        return self.cursor;
        
    
    def getDatabaseList(self):
        self.cursor.execute("SHOW DATABASES");
        return self.__formatValue()
    
    # Auxillary
    def __formatValue(self):
        temp = []
        for i in self.cursor.fetchall():
            try:
                temp.append("%s" % i)
            except:
                temp.append("{}".format(i))
        return temp;
    
    #######################################################
    
    # Debugging Purposes
    def Print_Database(self):
        self.cursor.execute("SHOW DATABASES;")
        print(type(self.cursor));
        for x in self.cursor:
            print(x)
