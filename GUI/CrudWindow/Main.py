from email import header
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QPushButton,  QStackedLayout, QFormLayout, QWidget, QScrollArea
from PyQt5.uic import loadUi
from GUI.globalVariable import *
from CRUD_API import *
from datetime import datetime
class MainCrudWindow(QDialog):


    def __init__(self, apiCrud, databaseName):
        super(MainCrudWindow, self).__init__()
        UI_PATH = "GUI\\CrudWindow\\Main.ui"
        self.ui = loadUi(UI_PATH, self)
        self.API = apiCrud;
        self.dbName = databaseName
        self.database.setText(self.dbName)

        # Initializing Signals
        self.MGroupButton.clicked.connect(self.GroupAttribute)
        self.MSearchButton.clicked.connect(self.SearchAttribute)
        self.MModifyButton.clicked.connect(self.ModifyAttribute)
        self.MCreateButton.clicked.connect(self.CreateAttribute)
        self.MDeleteButton.clicked.connect(self.DeleteAttribute)
        self.MChangeButton.clicked.connect(self.ChangeAttribute)
        self.MSignOutButton.clicked.connect(self.SignOutAttribute)
        self.tabWidget.currentChanged.connect(self.tabChanged);
        
        # Load The Data
        self.loadData();

    def loadData(self):
        
        # While there are tabs, delete them
        while self.tabWidget.count():
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
            
        # Get the List of Tables
        tableList = self.API.getTableList();
        
        
        # Initial Variables
        count = 0
        
        
        # Iterate through the list of tables
        for tableName in tableList:
            
            # Open the list of tables
            with open("Data/database/tableList.dat", 'a') as f:
                # Write it by line
                f.writelines(tableName + '\n');
                
            # Add a Table Table to the current Tab
            self.tabWidget.addTab(QTableWidget(), tableName)
            
            # Connect the New Table in the Tab to the function SaveChange when a certain item is Changed
            self.tabWidget.currentWidget().itemChanged.connect(self.saveChanged);
            
            # Set the current tab to the last Tab
            self.tabWidget.setCurrentIndex(count)
            
            
            # Get the list of Attribute
            attributeList = self.API.getAttributeList(tableName) 
            
            # Get the current header
            stuff = self.tabWidget.currentWidget().horizontalHeader();
            # Make the table stretch 
            stuff.setStretchLastSection(True);
            
            # Get Attribute Type
            with open("Data/database/attributeType.dat", 'a') as attrTypeFile:
                attrType = self.API.getAttributeTypes(tableName);
                for typeName in attrType:
                    attrTypeFile.write(typeName + ' ');
                attrTypeFile.write('\n');
            
            # Initial variables
            headerCount = 0;
            isFirst = True;
            
            with open("Data/database/attributeList.dat", 'a') as attListFile:
                for attributeName in attributeList:
                    
                    # Write the attribute name to the file
                    attListFile.writelines(str(attributeName[0]) + ' ')
                    
                    # Insert a column in the Table
                    self.__insertColumn()
                    
                    # Set the item name as the name of the attribute
                    self.__setHorizontalItemAt(headerCount, attributeName[0])
                    
                    # Load The data into the Table
                    self.__loadGetData(tableName, attributeName, headerCount, isFirst)
    
                    isFirst = False;
                    headerCount += 1;
    
                attListFile.writelines("\n")
                
            # Add relevant attributes to the right side for adding values
            self.addAttributeForm(count);
            
            count += 1

    
    def addAttributeForm(self, tableIndex):
        # Open the Attribute List Fiel
        attListFile = open("Data/database/attributeList.dat", 'r')

        # Create A Widget for the form
        formLayout = QWidget()
        
        # Make the widget layout as form
        formLayout.setLayout(QFormLayout())
        
        # Add the created widget to the stack and set the current to it
        self.stackWidget.addWidget(formLayout)
        self.stackWidget.setCurrentWidget(formLayout)
        
        # Create a temporary List
        listAttList = []
        
        # Get each attribute
        for i, attrValue in enumerate(attListFile):
            if i == tableIndex:
                attrValue = attrValue.split(' ')
                listAttList = attrValue
                break;
        
        # Put each attribute to the form (add a QLabel with its name and QLineEdit)
        for i in listAttList:
            if(i == '\n'):
                continue;
            self.stackWidget.currentWidget().layout().addRow(QLabel(i), QLineEdit())
        attListFile.close()
        
        # Add a button at the end of all the form for making chanages
        tempButton = QPushButton("Add Values")
        self.stackWidget.currentWidget().layout().addRow(tempButton)
        
        # Connect it to the addButtonPush
        tempButton.clicked.connect(self.addButtonPush)

    def addButtonPush(self):
        
        
        # Initial Variables
        listStr = ""
        headerCount = self.tabWidget.currentWidget().columnCount()
        currentRow = self.__insertRow()
        
        for i in range(0,self.stackWidget.currentWidget().layout().rowCount()-1):
            # Get the itemAt(i,1)
            tempWidget =  self.stackWidget.currentWidget().layout().itemAt(i,1);
            # Get the text value of that item
            textWidgetValue = tempWidget.widget().text()
            
            # If it's an int, then make it string without quotation
            if isinstance(textWidgetValue, int):
                listStr += str(textWidgetValue);
            # If it's none, then make it NULL
            elif textWidgetValue.lower() == "none":
                listStr += "NULL";
            # If it's a string, then add ' to it
            else:
                listStr += " ' " + textWidgetValue + " ' ";
            self.__setItemAt(currentRow, i, textWidgetValue)
            listStr += ','
            
        # Insert the Value in the Database
        try:
            self.API.insertValue(self.tabWidget.tabText(self.tabWidget.currentIndex()), listStr.rstrip(','))
        except:
            pop_message("ERROR: Input Error");
            self.tabWidget.currentWidget().removeRow(currentRow)
        
        # Old Code
        #startingStr =  f"INSERT INTO {self.tabWidget.tabText(self.tabWidget.currentIndex())} VALUES({listStr.rstrip(',')})"
        #self.API.executeCommand(startingStr)
        
        # Change this to only update the new value not all
        #self.loadData();
                
    def tabChanged(self, item):
        self.stackWidget.setCurrentIndex(item);    
        pass
    
    def saveChanged(self, item):
        
        with open("Data/database/selectCommand.dat", 'a') as f:
            try:
                f.write(
                f"""
UPDATE {self.tabWidget.tabText(self.tabWidget.currentIndex())} SET {self.tabWidget.currentWidget().horizontalHeaderItem(item.column()).text()} = "{item.text()}" WHERE {self.tabWidget.currentWidget().horizontalHeaderItem(0).text()} = "{(self.tabWidget.currentWidget().item(item.row(), 0).text())}";
                """)
            except:
                print("Some thing Happen in SaveChanged)")
    
    def AddAttribute(self):
        pass

    def GroupAttribute(self): #Grouping table is the class of group ui
        Widget.widget(4).loadData(self.tabWidget.tabText(self.tabWidget.currentIndex()))
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

    # Private
    def __loadGetData(self,  tableName, attributeName, headerPosition, isFirst):
        rowPosition = -1;
        for data in self.API.getDataFrom(tableName, attributeName[0]):
            if isFirst:
                rowPosition = self.__insertRow();
            else:
                rowPosition += 1;
            try:
                self.__setItemAt(rowPosition, headerPosition, str(data))
            except:
                dateTime = data.strftime("%Y-%m-%d")
                self.__setItemAt(rowPosition, headerPosition, dateTime)
    
    # Returns the position if needed
    def __insertRow(self):
        rowCount = self.tabWidget.currentWidget().rowCount();
        self.tabWidget.currentWidget().insertRow(rowCount);
        return rowCount
    
    # Returns the position if needed
    def __insertColumn(self):
        colCount = self.tabWidget.currentWidget().columnCount()
        self.tabWidget.currentWidget().insertColumn(colCount);
        return colCount

    def __setItemAt(self, rowPosition, headerPosition, data):
        try:
            self.tabWidget.currentWidget().setItem(rowPosition,headerPosition,QTableWidgetItem(str(data)))
        except:
            dateTime = data.strftime("%Y-%m-%d")
            self.tabWidget.currentWidget().setItem(rowPosition,headerPosition,QTableWidgetItem(dateTime))
    
    def __setHorizontalItemAt(self, headerPosition, data):
        self.tabWidget.currentWidget().setHorizontalHeaderItem(headerPosition,QTableWidgetItem(data))
        
        