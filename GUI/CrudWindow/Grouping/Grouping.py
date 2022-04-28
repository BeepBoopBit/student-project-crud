import os
from pickle import ADDITEMS
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *


# Do a checking if the value is greater than 2 for the attribute in group by
class GroupingTable(QDialog):
    def __init__(self, apiCrud):
        super(GroupingTable, self).__init__()
        UI_PATH = "GUI\\CrudWindow\\Grouping\\Grouping.ui" 
        self.ui = loadUi(UI_PATH,self)
        self.GBAddAttribute.clicked.connect(self.openSelectAttribute)
        self.GBOkButton.clicked.connect(self.confirmButton)
        self.GBExitButton.clicked.connect(self.exitButton)
        self.API = apiCrud;
        self.tbName = ""
        
        # PopUp Message Setup

    def loadData(self, tableName):
        self.tbName = tableName;
        self.tbLabel.setText(tableName);
        pass
    
    def addAttributeInList(self, attName):
        tempQPushButton = QPushButton("X")
        tempQLabel = QLabel(attName);
        tempQPushButton.clicked.connect(lambda: self.removeValue(tempQLabel.text()));
        self.formLayout.addRow(tempQLabel, tempQPushButton)

    def removeValue(self , QLabelValue):
        for i in range(0, self.formLayout.rowCount()):
            value = self.formLayout.itemAt(i,0);
            try:
                textValue = value.widget().text()
                if textValue == QLabelValue:
                    self.formLayout.removeRow(i);
                    break;
            except:               
                pass

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()
        
    def confirmButton(self):
        str = f"SELECT * FROM {self.tbName} GROUP BY "
        for i in range(0,self.formLayout.rowCount()):
            str += self.formLayout.itemAt(i,0).widget().text() + ',';
        str = str.rstrip(',');
        temp = self.API.executeCommand(str)
        isHeader = True;
        for i in temp:
            headerCount = 0
            rowPosition = self.GBTable.rowCount();
            self.GBTable.insertRow(rowPosition);
            for j in i:
                if isHeader == True:
                    colCount = self.GBTable.columnCount()
                    self.GBTable.insertColumn(colCount);
                    self.GBTable.setHorizontalHeaderItem(headerCount,QTableWidgetItem(j))
                else:
                    try:
                        self.GBTable.setItem(rowPosition,headerCount,QTableWidgetItem(j))
                    except:
                        dateTime = j.strftime("%Y-%m-%d")
                        self.GBTable.setItem(rowPosition,headerCount,QTableWidgetItem(dateTime))
                    headerCount += 1
                    pass
                isHeader = not isHeader;
    
    
    def exitButton(self):
        Widget.setCurrentIndex(3)
        
    def openSelectAttribute(self):
        Widget.widget(10).loadData(self.tbName)
        Widget.setCurrentIndex(10)
    
class SelectAddAttribute(QDialog):
    def __init__(self, apiCrud):
        super(SelectAddAttribute, self).__init__()
        UI_PATH = "GUI\\CrudWindow\\Grouping\\SelectAttribute.ui"
        self.ui = loadUi(UI_PATH, self)
        self.GBOkButton.clicked.connect(self.okButton)
        self.GBExitButton.clicked.connect(self.exitButton)
        self.API = apiCrud
        
    def loadData(self, tableName):
        for i in self.API.getAttributeList(tableName):
            self.GBSelectAttribute.addItem(i[0]);
            
    def okButton(self):
        Widget.widget(4).addAttributeInList(self.GBSelectAttribute.currentText());
        self.exitButton()

    def exitButton(self):
        self.GBSelectAttribute.clear()
        Widget.setCurrentIndex(4)