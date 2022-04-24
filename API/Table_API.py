from msilib.schema import tables

class Table:
    def __init__(self, db) -> None:
        self.db = db
        self.cursor = self.db.cursor()
    
    #######################################################
    
    # Creating
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
    
    
    # Getters
    def getTableList(self):
        self.cursor.execute("SHOW TABLES;")
        return self.__formatValue();
    
    # Dropping
    def dropTable(self, tableName):
        self.cursor.execute(f"DROP TABLE {tableName}")

    # Adding
    def addColumn(self, tableName, columnName, columnType):
        self.cursor.execute(f"ALTER TABLE {tableName} ADD {columnName} {columnType};");
    
    # Removing
    def removeColumn(self, tableName, columnName):
        self.cursor.execute(f"ALTER TABLE {tableName} DROP COLUMN {columnName};");
    
    # Modifying
    def changeType(self, tableName, columnName, dataType):
        self.cursor.execute(f"ALTER TABLE {tableName} MODIFY {columnName} {dataType};");

    # Inserting
    def insertValue(self, tbName, value):
        self.cursor.execute(f"INSERT INTO {tbName} VALUES({value});")
    
    def insertValueDate(self, tbName, value, dateTime):
        str_now = '\"' + dateTime.date().isoformat() + '\"';
        self.cursor.execute(f"INSERT INTO {tbName} VALUES({value}, {str_now});")
    

    # Auxillary
    def __formatValue(self):
        temp = []
        for i in self.cursor.fetchall():
            try:
                temp.append("%s" % i)
            except:
                temp.append("{}".format(i))
        return temp;
    

    # Debuggin
    def describeTable(self, tableName):
        try:            
            self.cursor.execute(f"DESCRIBE {tableName}")
        except:
            print("The Table Might Not exists");
        for i in self.cursor:
            print(i);
