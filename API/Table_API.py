from dataclasses import dataclass
import MySQLdb

class Table:
    def __init__(self, db) -> None:
        self.db = db
        self.cursor = self.db.cursor()
    
    #######################################################
    # Assumes that the parameter contraint have only one value
    def createTable(self, tableName, columnName, dataType, contraint):
        self.cursor.execute(f"CREATE TABLE {tableName}({columnName} {dataType} {contraint});")

    def getTable(self):
        self.cursor.execute("SHOW TABLES;")
        return self.cursor;

        