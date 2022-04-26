from email import header
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *
from CRUD_API import *
from datetime import datetime
class MainCrudWindow(QDialog):

    def truncateFiles(self):
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

    # PopUp Message Setup

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def __init__(self, apiCrud, databaseName):
        super(MainCrudWindow, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\Main.ui"
        self.ui = loadUi(UIPATH, self)
        self.API = apiCrud;
        self.dbName = databaseName
        self.database.setText(self.dbName)

        self.MAddButton.clicked.connect(self.AddAttribute)
        self.MGroupButton.clicked.connect(self.GroupAttribute)
        self.MSearchButton.clicked.connect(self.SearchAttribute)
        self.MModifyButton.clicked.connect(self.ModifyAttribute)
        self.MCreateButton.clicked.connect(self.CreateAttribute)
        self.MDeleteButton.clicked.connect(self.DeleteAttribute)
        self.MChangeButton.clicked.connect(self.ChangeAttribute)
        self.MSignOutButton.clicked.connect(self.SignOutAttribute)
        
        self.loadData();

    # Load the data

    def loadData(self):
        while self.tabWidget.count():
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
            
        tableList = self.API.getTableList();
        if len(tableList) <= 0:
            pass
        else:
            count = 0
            for i in tableList:
                with open("Data/database/tableList.dat", 'a') as f:
                    f.writelines(i + '\n');
                self.tabWidget.addTab(QTableWidget(), i)
                # Save the change of index
                self.tabWidget.currentWidget().itemChanged.connect(self.saveChanged);
                self.tabWidget.setCurrentIndex(count)
                headerCount = 0;
                tempAttributeList =self.API.getAttributeList(i) 
                stuff = self.tabWidget.currentWidget().horizontalHeader();
                stuff.setStretchLastSection(True);
                isFirst = True;
                
                # Get Attribute Type
                attrType = self.API.getAttributeTypes(i);
                attrTypeFile = open("Data/database/attributeType.dat", 'a');
                for j in attrType:
                    attrTypeFile.write(j + ' ');
                attrTypeFile.write('\n');
                attrTypeFile.close()
                
                attListFile = open("Data/database/attributeList.dat", 'a')
                for j in tempAttributeList:
                    attListFile.writelines(str(j[0]) + ' ')
                    colCount = self.tabWidget.currentWidget().columnCount()
                    

                    
                    
                    self.tabWidget.currentWidget().insertColumn(colCount);
                    self.tabWidget.currentWidget().setHorizontalHeaderItem(headerCount,QTableWidgetItem(j[0]))
                    rowPosition = -1;
                    for data in self.API.getDataFrom(i, j[0]):
                        if isFirst:
                            rowPosition = self.tabWidget.currentWidget().rowCount();
                            self.tabWidget.currentWidget().insertRow(rowPosition);
                        else:
                            rowPosition += 1;
                        try:
                            self.tabWidget.currentWidget().setItem(rowPosition,headerCount,QTableWidgetItem(str(data)))
                        except:
                            dateTime = data.strftime("%Y-%m-%d")
                            self.tabWidget.currentWidget().setItem(rowPosition,headerCount,QTableWidgetItem(dateTime))
                    isFirst = False;
                    headerCount += 1;
                attListFile.writelines("\n")
                count += 1
    
    def updateForm(self):
        pass
    
    def saveChanged(self, item):
        
        with open("Data/database/selectCommand.dat", 'a') as f:
            f.write(
                f"""
UPDATE {self.tabWidget.tabText(self.tabWidget.currentIndex())} SET {self.tabWidget.currentWidget().horizontalHeaderItem(item.column()).text()} = "{item.text()}" WHERE {self.tabWidget.currentWidget().horizontalHeaderItem(0).text()} = "{(self.tabWidget.currentWidget().item(item.row(), 0).text())}";
                """)
    
    def AddAttribute(self):
        pass

    def GroupAttribute(self): #Grouping table is the class of group ui
        Widget.setCurrentIndex(4)

    def FilterAttribute(self): # Filter table is the class of filter ui
        Widget.setCurrentIndex(4)
        
    def SearchAttribute(self):
        pass

    def ModifyAttribute(self): #Modify Table is the class of modify ui
        Widget.widget(5).loadData(self.tabWidget.tabText(self.tabWidget.currentIndex()),self.tabWidget.currentIndex())
        Widget.setCurrentIndex(5)
        

    def CreateAttribute(self): #Create Table is the class of create ui
        Widget.setCurrentIndex(6);
        

    def DeleteAttribute(self):
        pass

    def ChangeAttribute(self):
        with open("Data/database/selectCommand.dat") as f:
            for line in f:
                line = line.rstrip()
                if line == '':
                    continue
                else:
                    self.API.changeData(line);
        self.loadData();

    def SignOutAttribute(self): #Sign out is the class of sign out ui
        Widget.setCurrentIndex(0)



    

