from dataclasses import dataclass
from msilib.schema import tables
from pydoc import describe
import MySQLdb

class Table:
    def __init__(self, db) -> None:
        self.db = db
        self.cursor = self.db.cursor()
    
    #######################################################
    def createTable(self, tableName, columnName, dataType, constraint):
        newConstraint = ""
        listConstraint = [];

        # Separate the List to the strings
        for word in constraint:
            if isinstance(word,list):
                listConstraint.append(word);
            else:
                newConstraint += word + ' ';                
        
        # Create a string of the SQL command (Incomplete;)
        command = f"CREATE TABLE {tableName}({columnName} {dataType} {newConstraint} "

        listConstraintSize = len(listConstraint)
        # If there is more Constraints to be done, add ','
        if listConstraintSize:
           command += ',';
        # Else, add a ')'
        else:
            command += ");";
        
        # Transform the list inside the listConstraint as string and add them to the command variable 
        for listValue in listConstraint:
            listConstraintSize -= 1;
            tempStr = "";
            for data in listValue:
                tempStr += data + ' ';
            if(listConstraintSize == 0):
                command += tempStr +");";
            else:
                command += tempStr + ',';
        
        # Execute the command
        self.cursor.execute(command)
    
    def getTableList(self):
        self.cursor.execute("SHOW TABLES;")
        return self.cursor.fetchall();
    def dropTable(self, tableName):
        self.cursor.execute(f"DROP TABLE {tableName}")

    def addColumn(self, tableName, columnName, columnType):
        self.cursor.execute(f"ALTER TABLE {tableName} ADD {columnName} {columnType};");
    
    def removeColumn(self, tableName, columnName):
        self.cursor.execute(f"ALTER TABLE {tableName} DROP COLUMN {columnName};");
    
    def changeType(self, tableName, columnName, dataType):
        self.cursor.execute(f"ALTER TABLE {tableName} MODIFY {columnName} {dataType};");

    # Debuggin
    def describeTable(self, tableName):
        try:            
            self.cursor.execute(f"DESCRIBE {tableName}")
        except:
            print("The Table Might Not exists");
        for i in self.cursor:
            print(i);
