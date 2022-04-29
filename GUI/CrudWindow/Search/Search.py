import os
from pickle import ADDITEMS
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QTableWidgetItem, QTextEdit, QHBoxLayout
from PyQt5.uic import loadUi
from GUI.globalVariable import *


# Do a checking if the value is greater than 2 for the attribute in group by
# Problem in inserting
# if you have 'a' as inserted value, you'll have a problem now because in our software it'll be ' a '
# TODO: Strip the spaces when inserting value
class SearchingTable(QDialog):
    def __init__(self, apiCrud):
        super(SearchingTable, self).__init__()
        UI_PATH = "GUI\\CrudWindow\\Search\\SearchWindow.ui" 
        self.ui = loadUi(UI_PATH,self)

        # Initialize Signals
        self.SearchAdd.clicked.connect(self.openSelectAttribute) # Using the previous select Attribute Method
        self.SEOkButton.clicked.connect(self.confirmButton)
        self.SEExitButton.clicked.connect(self.exitButton)
        
        # Initialize the values
        self.API = apiCrud;
        self.tbName = ""
        
        self.textEditList = []
        self.operationlist = []
        self.logicalList = []
        
    def loadData(self, tableName):
        # Initialize the Values
        self.tbName = tableName;
        pass
    
    def addAttributeInList(self, attName):
        # Create temporary QWidgets
        tempQPushButton = QPushButton("X")

        tempQTextEdit = QTextEdit()
        self.textEditList.append(tempQTextEdit);
        
        tempQLabel = QLabel(attName);
        tempQWidget = QHBoxLayout()      

        tempQWidget.addWidget(tempQTextEdit);
        tempQWidget.addWidget(tempQPushButton);
        
        # Connect the Button into RemoveValue with a passing value of the label's text
        tempQPushButton.clicked.connect(lambda: self.removeValue(tempQLabel.text()));
        
        #get the operation
        self.operationlist.append(self.SEOperation.currentText())
        
        # get logical
        self.logicalList.append(self.SEOperation_2.currentText())
        
        
        # The it to the row 
        self.formLayout_2.addRow(tempQLabel, tempQWidget)

        
    def removeValue(self , QLabelValue):
        # Iterate through all the rows in the form layout by index
        for i in range(0, self.formLayout_2.rowCount()):
            # get the item at the position (i,0)
            value = self.formLayout_2.itemAt(i,0);
            # try if the value is a widget
            try:
                # get the text in the widget
                textValue = value.widget().text()

                # find the right widget for the remove item
                if textValue == QLabelValue:
                    # Remove it into the layout
                    self.formLayout_2.removeRow(i);
                    del self.textEditList[i]
                    del self.operationlist[i]
                    del self.logicalList[i]
                    break;
            except:               
                pass

    def confirmButton(self):
        self.SearchResult.setColumnCount(0)
        self.SearchResult.setRowCount(0);
        
        # Create the Select Statement
        
        commandList = []
        
        
        # Get the text values in the forms
        for i in range(0,self.formLayout_2.rowCount()):
            tempStr = ""
            
            # Get Attribute
            tempStr += self.formLayout_2.itemAt(i,0).widget().text() + ' '
            
            # Get Operation
            tempStr += self.operationlist[i] + ' '
            
            # Get value
            tempText = self.textEditList[i].toPlainText()
            if isinstance(tempText, int):
                tempStr += tempText;
            else:
                tempStr += "'" + tempText + "' "
            
            # Get Logical
            tempValue = self.logicalList[i]  + ' '
            if tempValue == "NULL ":
                tempStr += ';'
            else:
                tempStr += tempValue;
            commandList.append(tempStr);
        
        totalCommand = "";
        
        # Execute the command 
        for i in commandList:
            totalCommand += i + ' '
            
        temp = self.API.getDataCommand(self.tbName, totalCommand)
        
        # Initial variables
        headerCount = 0
        for data in self.API.getAttributeList(self.tbName):
            self.__insertColumn(headerCount, data[0]);
            headerCount += 1;
        
        tempHeaderCount = 0
        rowPosition = self.SearchResult.rowCount();
        for data in temp:
            if tempHeaderCount == headerCount or tempHeaderCount == 0:
                # Reset it to zero
                tempHeaderCount = 0;
                # Insert a new Row
                rowPosition = self.SearchResult.rowCount();
                self.SearchResult.insertRow(rowPosition);

            # Insert an item in row
            self.__insertRow(rowPosition,tempHeaderCount,QTableWidgetItem(str(data)));
            tempHeaderCount += 1
    
    
    def exitButton(self):
        Widget.setCurrentIndex(3)
        
    def openSelectAttribute(self):
        Widget.widget(14).loadData(self.tbName)
        Widget.setCurrentIndex(14)
        
    def __insertColumn(self, headerPosition, data):
        colCount = self.SearchResult.columnCount()
        self.SearchResult.insertColumn(colCount);
        self.SearchResult.setHorizontalHeaderItem(headerPosition,QTableWidgetItem(data))
    
    def __insertRow(self, rowPosition, headerPosition, data):
        try:
            self.SearchResult.setItem(rowPosition,headerPosition,QTableWidgetItem(data))
        except:
            dateTime = data.strftime("%Y-%m-%d")
            self.SearchResult.setItem(rowPosition,headerPosition,QTableWidgetItem(dateTime))
            
class SearchAddAttribute(QDialog):
    def __init__(self, apiCrud):
        super(SearchAddAttribute, self).__init__()
        UI_PATH = "GUI\\CrudWindow\\Grouping\\SelectAttribute.ui"
        self.ui = loadUi(UI_PATH, self)
        self.GBOkButton.clicked.connect(self.okButton)
        self.GBExitButton.clicked.connect(self.exitButton)
        self.API = apiCrud
        
    def loadData(self, tableName):
        for i in self.API.getAttributeList(tableName):
            self.GBSelectAttribute.addItem(i[0]);
            
    def okButton(self):
        Widget.widget(13).addAttributeInList(self.GBSelectAttribute.currentText());
        self.exitButton()

    def exitButton(self):
        self.GBSelectAttribute.clear()
        Widget.setCurrentIndex(13)