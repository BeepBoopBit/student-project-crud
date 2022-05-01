from email import header
import os
from tokenize import Double
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QPushButton,  QStackedLayout, QFormLayout, QWidget, QScrollArea
from PyQt5.uic import loadUi
from GUI.globalVariable import *
from CRUD_API import *

# TODO: Implement Search Functionality
# TODO: Create Row

class MainCrudWindow(QDialog):

    def __init__(self, apiCrud):
        super(MainCrudWindow, self).__init__()
        UI_PATH = "GUI\\CrudWindow\\Main.ui"
        self.ui = loadUi(UI_PATH, self)
        
        self.API = apiCrud;
        self.dbName = ""
        # Initializing Signals
        self.MGroupButton.clicked.connect(self.GroupAttribute)
        self.MSortButton.clicked.connect(self.SortAttribute)
        self.MModifyButton.clicked.connect(self.ModifyAttribute)
        self.MCreateButton.clicked.connect(self.CreateAttribute)
        self.MDeleteButton.clicked.connect(self.DeleteAttribute)
        self.MChangeButton.clicked.connect(self.ChangeAttribute)
        self.MSignOutButton.clicked.connect(self.SignOutAttribute)
        self.tabWidget.currentChanged.connect(self.tabChanged);
        self.MSearchButton.clicked.connect(self.searchFunction);
        self.MDeleteRow.clicked.connect(self.deleteRowFunction);
        
        # Some Variables
        self.tb_name = ["" , 0]
        
    def changeDatabaseLabel(self, databaseName):
        self.dbName = databaseName
        self.database.setText(self.dbName)
        
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
                
            # Add a Table to the current Tab
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
                    self.__loadAttributeData(tableName, attributeName, headerCount, isFirst)
    
                    isFirst = False;
                    headerCount += 1;
    
                attListFile.writelines("\n")
                
            # Add relevant attributes to the right side for adding values
            self.addAttributeForm(count);
            
            count += 1

    def loadNewTable(self, tableName):
        # Add a Table Table to the current Tab
        tempWidget = QTableWidget();
        self.tabWidget.addTab(tempWidget, tableName)
        
        # Set the current tab to the last Tab
        self.tabWidget.setCurrentWidget(tempWidget)
        
        # Connect the New Table in the Tab to the function SaveChange when a certain item is Changed
        self.tabWidget.currentWidget().itemChanged.connect(self.saveChanged);
        
        
        attList = self.API.getAttributeList(tableName);
        headerPosition = 0
        
        attListFile = open("Data/database/attributeList.dat", 'a')
        for i in attList:
            # Insert a column in the Table
            self.__insertColumn()
            self.__setHorizontalItemAt(headerPosition, i[0]);
            
            attListFile.write(i[0] + ' ')
            headerPosition += 1;
        attListFile.close();
        
        tabCount = self.tabWidget.count()
        self.addAttributeForm(tabCount-1)
    
    def deleteRowFunction(self):
        rowCount = self.tabWidget.currentWidget().currentRow()
        tempWidgetText = self.tabWidget.currentWidget().item(rowCount,0).text();
        if isinstance(tempWidgetText, int):
            pass;
        else:
            tempWidgetText = "'" + tempWidgetText + "'"
        self.API.deleteItem(self.tb_name[0], self.tabWidget.currentWidget().horizontalHeaderItem(0).text(), tempWidgetText);
        self.tabWidget.currentWidget().removeRow(rowCount);
        pass
    
    def searchFunction(self):
        Widget.setFixedWidth(740)
        Widget.setFixedHeight(450)
        Widget.widget(13).loadData(self.tabWidget.tabText(self.tabWidget.currentIndex()));
        Widget.setCurrentIndex(13);
        pass
    
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
            elif(i == ''):
                continue
            self.stackWidget.currentWidget().layout().addRow(QLabel(i), QLineEdit())
        attListFile.close()
        
        # Add a button at the end of all the form for making chanages
        tempButton = QPushButton("Add Values")
        self.stackWidget.currentWidget().layout().addRow(tempButton)
        
        # Connect it to the addButtonPush
        tempButton.clicked.connect(self.addButtonPush)

    def addButtonPush(self):
        
        
        tableName = self.tabWidget.tabText(self.tabWidget.currentIndex());
        tabIndex = self.tabWidget.currentIndex()
        
        typeListVarb =  []
        attrFile = open("Data/database/attributeList.dat", 'r')
        for i, attrValue in enumerate(attrFile):
            if i == tabIndex:
                attrValue = attrValue.split(' ')
                typeList = self.API.getAttributeTypes(tableName);
                for i in range(0,len(attrValue) - 1):
                    typeListVarb.append(str(typeList[i]))
                break;
        attrFile.close();
        
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
            tolowerVarb = (typeListVarb[i]).lower();
            if tolowerVarb == 'int' or tolowerVarb == 'float' or tolowerVarb == 'double':
                listStr += str(textWidgetValue);
            # If it's none, then make it NULL
            elif tolowerVarb == "none":
                listStr += "NULL";
            # If it's a string, then add ' to it
            else:
                listStr += " ' " + textWidgetValue + " ' ";
            
            # Set the item at the specific row and column
            self.__setItemAt(currentRow, i, textWidgetValue)
            listStr += ','
            
        # Insert the Value in the Database
        try:
            self.API.insertValue(self.tabWidget.tabText(self.tabWidget.currentIndex()), listStr.rstrip(','))
        except:
            pop_message("ERROR: Input Error");
            self.tabWidget.currentWidget().removeRow(currentRow)
                
    def tabChanged(self, item):
        self.stackWidget.setCurrentIndex(item);    
        self.tb_name = [self.tabWidget.tabText(self.tabWidget.currentIndex()), item];
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

    def GroupAttribute(self):
        Widget.setFixedWidth(770)
        Widget.setFixedHeight(485)
        Widget.widget(4).loadData(self.tabWidget.tabText(self.tabWidget.currentIndex()))
        Widget.setCurrentIndex(4)

    def SortAttribute(self):
        Widget.setFixedWidth(770)
        Widget.setFixedHeight(485)
        Widget.widget(11).loadData(self.tabWidget.tabText(self.tabWidget.currentIndex()))
        Widget.setCurrentIndex(11);
        pass

    def ModifyAttribute(self):
        Widget.setFixedWidth(660)
        Widget.setFixedHeight(390)
        Widget.widget(5).loadData(self.tabWidget.tabText(self.tabWidget.currentIndex()),self.tabWidget.currentIndex())
        Widget.setCurrentIndex(5)
        

    def CreateAttribute(self): 
        Widget.setFixedWidth(320)
        Widget.setFixedHeight(160)
        Widget.setCurrentIndex(6);
        

    def DeleteAttribute(self):
        try:
            self.API.dropTable(self.tb_name[0])
            self.tabWidget.removeTab(self.tb_name[1]);
        except:
            pop_message("Cannot Drop, Sometable depends on it")            
                
        

    def ChangeAttribute(self):
        with open("Data/database/selectCommand.dat") as f:
            for line in f:
                line = line.rstrip()
                if line == '':
                    continue
                else:
                    self.API.changeData(line);
        self.loadData();

    def SignOutAttribute(self):
        # Set the Dimensions
        Widget.setFixedWidth(550)
        Widget.setFixedHeight(330)
        Widget.setCurrentIndex(0)

    # Private
    def __loadAttributeData(self,  tableName, attributeName, headerPosition, isFirst):
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
        
        