import os
from pickle import ADDITEMS
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *


# Do a checking if the value is greater than 2 for the attribute in group by
class SortTable(QDialog):
    def __init__(self, apiCrud):
        super(SortTable, self).__init__()
        UI_PATH = "GUI\\CrudWindow\\Grouping\\Grouping.ui" 
        self.ui = loadUi(UI_PATH,self)

        # Initialize Signals
        self.GBAddAttribute.clicked.connect(self.openSelectAttribute)
        self.GBOkButton.clicked.connect(self.confirmButton)
        self.GBExitButton.clicked.connect(self.exitButton)
        
        # Initialize the values
        self.API = apiCrud;
        self.tbName = ""
        
        # PopUp Message Setup

    def loadData(self, tableName):
        # Initialize the Values
        self.tbName = tableName;
        self.tbLabel.setText(tableName);
        pass
    
    def addAttributeInList(self, attName):
        # Create temporary QWidgets
        tempQPushButton = QPushButton("X")
        tempQLabel = QLabel(attName);
        
        # Connect the Button into RemoveValue with a passing value of the label's text
        tempQPushButton.clicked.connect(lambda: self.removeValue(tempQLabel.text()));
        
        # The it to the row 
        self.formLayout.addRow(tempQLabel, tempQPushButton)

    def removeValue(self , QLabelValue):
        # Iterate through all the rows in the form layout by index
        for i in range(0, self.formLayout.rowCount()):
            # get the item at the position (i,0)
            value = self.formLayout.itemAt(i,0);
            # try if the value is a widget
            try:
                # get the text in the widget
                textValue = value.widget().text()

                # find the right widget for the remove item
                if textValue == QLabelValue:
                    # Remove it into the layout
                    self.formLayout.removeRow(i);
                    break;
            except:               
                pass

    def confirmButton(self):
        self.GBTable.setColumnCount(0)
        self.GBTable.setRowCount(0);
        
        # Create the Select Statement
        strValue = ""
        # Get the text values in the forms
        for i in range(0,self.formLayout.rowCount()):
            strValue += self.formLayout.itemAt(i,0).widget().text() + ',';
            
        # Remove the ',' at the end
        strValue = strValue.rstrip(',');
        
        # Execute the command 
        try:
            temp = self.API.getDataSortedBy(self.tbName, strValue)
            # Initial variables
            headerCount = 0
            for data in self.API.getAttributeList(self.tbName):
                self.__insertColumn(headerCount, data[0]);
                headerCount += 1;
            
            tempHeaderCount = 0
            rowPosition = self.GBTable.rowCount();
            for data in temp:
                if tempHeaderCount == headerCount or tempHeaderCount == 0:
                    # Reset it to zero
                    tempHeaderCount = 0;
                    # Insert a new Row
                    rowPosition = self.GBTable.rowCount();
                    self.GBTable.insertRow(rowPosition);
    
                # Insert an item in row
                self.__insertRow(rowPosition,tempHeaderCount,QTableWidgetItem(str(data)));
                tempHeaderCount += 1
        except:
            if len(strValue) < 1:
                pop_message("No Data Input")
            else:
                pop_message("UNKNOWN ERROR: Please Try again and report this problem")
                
    
    def exitButton(self):
        Widget.setCurrentIndex(3)
        
    def openSelectAttribute(self):
        Widget.widget(12).loadData(self.tbName)
        Widget.setCurrentIndex(12)
        
    def __insertColumn(self, headerPosition, data):
        colCount = self.GBTable.columnCount()
        self.GBTable.insertColumn(colCount);
        self.GBTable.setHorizontalHeaderItem(headerPosition,QTableWidgetItem(data))
    
    def __insertRow(self, rowPosition, headerPosition, data):
        try:
            self.GBTable.setItem(rowPosition,headerPosition,QTableWidgetItem(data))
        except:
            dateTime = data.strftime("%Y-%m-%d")
            self.GBTable.setItem(rowPosition,headerPosition,QTableWidgetItem(dateTime))
        
        
    
class SortSelectAddAttribute(QDialog):
    def __init__(self, apiCrud):
        super(SortSelectAddAttribute, self).__init__()
        UI_PATH = "GUI\\CrudWindow\\Grouping\\SelectAttribute.ui"
        self.ui = loadUi(UI_PATH, self)
        self.GBOkButton.clicked.connect(self.okButton)
        self.GBExitButton.clicked.connect(self.exitButton)
        self.API = apiCrud
        
    def loadData(self, tableName):
        for i in self.API.getAttributeList(tableName):
            self.GBSelectAttribute.addItem(i[0]);
            
    def okButton(self):
        Widget.widget(11).addAttributeInList(self.GBSelectAttribute.currentText());
        self.exitButton()

    def exitButton(self):
        self.GBSelectAttribute.clear()
        Widget.setCurrentIndex(11)