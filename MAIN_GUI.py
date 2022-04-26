from GUI.SignInWindow.SignIn import *
from GUI.globalVariable import *
from GUI.DatabaseWindow.Database import *

import traceback

def truncateFiles():
    colName = open("Data/createTable/columnName.dat", 'w')
    command = open("Data/createTable/command.dat", 'w')
    constraints = open("Data/createTable/constraints.dat", 'w')
    fk = open("Data/createTable/fk.dat", 'w')
    tableName = open("Data/createTable/tableName.dat", 'w')
    typeName = open("Data/createTable/type.dat", 'w')
    dbName = open("Data/database/databaseName.dat", 'w')
    tName = open("Data/database/tableList.dat", 'w')
    attList = open("Data/database/attributeList.dat", 'w')
    attType = open("Data/database/attributeType.dat", 'w')
    selectCommand = open("Data/database/selectCommand.dat", 'w')
    indexChange = open("Data/database/indexChange.dat", 'w')
    alterFile = open("Data/database/alterCommand.dat", 'w')
    colName.truncate()
    command.truncate()
    constraints.truncate()
    fk.truncate()
    tableName.truncate()
    typeName.truncate()
    dbName.truncate()
    tName.truncate()
    attList.truncate()
    attType.truncate()
    selectCommand.truncate()
    indexChange.truncate()
    alterFile.truncate()
    colName.close()
    command.close()
    constraints.close()
    fk.close()
    tableName.close()
    typeName.close()
    dbName.close()
    tName.close()
    attList.close()
    attType.close()
    selectCommand.close()
    indexChange.close()
    alterFile.close()
truncateFiles();

try:
    SignInWindow=SignIn()
    Widget.addWidget(SignInWindow)
    Widget.setFixedWidth(1100)
    Widget.setFixedHeight(650)
    Widget.show()
except Exception:
    print(traceback.format_exc())
    

truncateFiles();

app.exec()
