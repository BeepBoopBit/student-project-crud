import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *

class ModifyTable(QDialog):
    def __init__(self, apiCrud):
        super(ModifyTable, self).__init__()
        UI_PATH = "GUI\\CrudWindow\\\\Table\\ModifyTable\\ModifyTable.ui" 
        self.ui = loadUi(UI_PATH,self)
        self.MOKbutton.clicked.connect(self.submitButton)
        self.MExitbutton.clicked.connect(self.cancelButton)
        self.API = apiCrud;
        self.tbName = ""
        self.tbNumber = 0

    
    def truncateFiles(self):
        tName = open("Data/database/tableList.dat", 'w')
        attList = open("Data/database/attributeList.dat", 'w')
        attType = open("Data/database/attributeType.dat", 'w')
        attList.truncate()
        attType.truncate()
        tName.close()
        attList.close()
        attType.close()


    # Load Data

    def loadData(self, tableName, tabIndex):
        with open("Data/database/alterCommand.dat", 'w') as f:
            f.truncate();
        self.tbName = tableName;
        self.tbNumber = tabIndex;
        
        attrFile = open("Data/database/attributeList.dat", 'r')
        for i, attrValue in enumerate(attrFile):
            if i == tabIndex:
                attrValue = attrValue.split(' ')
                typeList = self.API.getAttributeTypes(tableName);
                for i in range(0,len(attrValue) - 1):
                    rowPosition = self.tableWidget.rowCount();
                    self.tableWidget.insertRow(rowPosition);
                    self.tableWidget.setItem(rowPosition,0,QTableWidgetItem(str(attrValue[i])))
                    self.tableWidget.setItem(rowPosition,1,QTableWidgetItem(str(typeList[i])))
                break;
        attrFile.close();
        self.tableWidget.itemChanged.connect(self.saveData)
    
    def submitButton(self):
        str = ""
        with open("Data/database/alterCommand.dat",'r') as f:
            for line in f:
                if str == "":
                    str = line;
                    newStr = line;
                    self.API.executeCommand(str)
                else:
                    newStr = line;
                    if str == newStr:
                        pass
                    else:
                        str = line;
                        self.API.executeCommand(str)
        self.cancelButton();        
    
    def cancelButton(self):
        self.tableWidget.setRowCount(0);
        self.truncateFiles()
        
        Widget.setFixedWidth(1100)
        Widget.setFixedHeight(650)
        Widget.widget(3).loadData()
        Widget.setCurrentIndex(3)
        
    
    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def saveData(self, item):
        newValue = item.text();
        rowIndex = item.row();
        colIndex = item.column()
        prevValue = "";
        rowName = self.tableWidget.item(rowIndex, 0).text()
        
        if colIndex == 1:
            typeFile = open("Data/database/attributeType.dat", 'r');
            for i, typeValue in enumerate(typeFile):
                if i == self.tbNumber:
                    typeValue = typeValue.split(' ')
                    prevValue = typeValue[rowIndex]
                    break;
            typeFile.close();            
            if prevValue == newValue:
                pass;
            else:
                with open("Data/database/alterCommand.dat",'a') as f:
                    str = f"ALTER TABLE {self.tbName} MODIFY COLUMN {rowName} {newValue};\n"
                    f.write(str);
        else:
            attrFile = open("Data/database/attributeList.dat", 'r');
            for i, attrValue in enumerate(attrFile):
                if i == self.tbNumber:
                    attrValue = attrValue.split(' ')
                    prevValue = attrValue[rowIndex]
                    break;
            attrFile.close();
            if prevValue == newValue:
                pass;
            else:
                with open("Data/database/alterCommand.dat",'a') as f:
                    str = f"ALTER TABLE {self.tbName} RENAME COLUMN {prevValue} TO {newValue};\n"
                    f.write(str);