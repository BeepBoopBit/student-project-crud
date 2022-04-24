import mysql.connector

class Database:
    def __init__(self, userName, userPassword) -> None:
        self.db = mysql.connector.connect(
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
    
    def deleteDatabase(self, dbName):
        self.cursor.execute(f"DROP DATABASE {dbName}")

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
            try:
                temp.append("%s" % i)
            except:
                temp.append("{}".format(i))
        return temp;
