from GUI.SignInWindow.SignIn import *
from GUI.globalVariable import *
from GUI.DatabaseWindow.Database import *

import traceback
try:
    SignInWindow=SignIn()
    Widget.addWidget(SignInWindow)
    Widget.setFixedWidth(1100)
    Widget.setFixedHeight(650)
    Widget.show()
except Exception:
    print(traceback.format_exc())
    
colName = open("Data/createTable/columnName.dat", 'w')
command = open("Data/createTable/command.dat", 'w')
constraints = open("Data/createTable/constraints.dat", 'w')
fk = open("Data/createTable/fk.dat", 'w')
tableName = open("Data/createTable/tableName.dat", 'w')
typeName = open("Data/createTable/type.dat", 'w')

colName.truncate()
command.truncate()
constraints.truncate()
fk.truncate()
tableName.truncate()
typeName.truncate()

app.exec()