from GUI.SignInWindow.SignIn import *
from GUI.globalVariable import *
from GUI.DatabaseWindow.Database import *

import traceback

def truncateFiles():
    
    alterFile = open("Data/database/alterCommand.dat", 'w')
    alterFile.truncate()
    alterFile.close()
    
    attListFile = open("Data/database/attributeList.dat", 'w')
    attListFile.truncate()
    attListFile.close()
    
    attTypeFile = open("Data/database/attributeType.dat", 'w')
    attTypeFile.truncate()
    attTypeFile.close()

    colName = open("Data/createTable/columnName.dat", 'w')
    colName.truncate()
    colName.close()
    
    command = open("Data/createTable/command.dat", 'w')
    command.truncate()
    command.close()
    
    constraints = open("Data/createTable/constraints.dat", 'w')
    constraints.truncate()
    constraints.close()

    dbName = open("Data/database/databaseName.dat", 'w')
    dbName.truncate()
    dbName.close()

    fkFile = open("Data/createTable/fk.dat", 'w')
    fkFile.truncate()
    fkFile.close()
    
    indexChange = open("Data/database/indexChange.dat", 'w')
    indexChange.truncate()
    indexChange.close()
    
    loginFile = open("Data/user/login.dat", 'w')
    loginFile.truncate();
    loginFile.close();
    
    selectCommand = open("Data/database/selectCommand.dat", 'w')
    selectCommand.truncate()
    selectCommand.close()
    
    tableName = open("Data/createTable/tableName.dat", 'w')
    tableName.truncate()
    tableName.close()
    
    typeName = open("Data/createTable/type.dat", 'w')
    typeName.truncate()
    typeName.close()
    
    tName = open("Data/database/tableList.dat", 'w')
    tName.truncate()
    tName.close()
    


if __name__ == "__main__":
    
    # Make sure that the files doesn't have any value inside before proceeding
    truncateFiles();
    
    try:
        # Create an Instance of the SignIn Class
        SignInWindow=SignIn()
        
        # Add the instance to the global variable Widget
        Widget.addWidget(SignInWindow) # 1
    
        # Set the Dimensions
        Widget.setFixedWidth(1100)
        Widget.setFixedHeight(650)
    
        # Show the Widget
        Widget.show()
    except Exception:
        print(traceback.format_exc())
    
    app.exec()
    