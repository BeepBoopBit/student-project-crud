import os
from PyQt5 import QtWidgets, uic
from tkinter import Widget
from GUI.globalVariable import *
from PyQt5.QtWidgets import QTableWidgetItem

# Naming a new table Window

class NameTable(QtWidgets.QDialog): 
    def __init__(self, apiCrud):
        super().__init__()
        UI_PATH = "GUI\\CrudWindow\\Table\\MainTable\\CreateTable.ui"
        uic.loadUi(UI_PATH, self)

        # Initialize Signals
        self.TOK.clicked.connect(self.TableMenuFunction)        # Table Menu Button ->  #8
        self.TCancel.clicked.connect(self.tableCancel)          # Cancel Button     ->  #3
        
        # Initialize API
        self.API = apiCrud;

    # Setup table
    def TableMenuFunction(self):
        # Write the name of the table to a file        
        str = "";
        with open("Data/createTable/tableName.dat", "w") as f:
            str = self.Table_Input.toPlainText();
            f.write(str);

        if len(str) < 1:
            pop_message(text="No Input data") 
        else:
            pop_message(text="Table Successfully Created!") 
            Widget.setFixedWidth(955)
            Widget.setFixedHeight(550)
            Widget.widget(7).readTable();
            Widget.setCurrentIndex(7)

    def tableCancel(self):
        Widget.setFixedWidth(1100)
        Widget.setFixedHeight(650)
        Widget.setCurrentIndex(3)

# Table Menu Window

class TableMenu(QtWidgets.QDialog):
    def __init__(self, apiCrud):
        super().__init__()
        UI_PATH = "GUI\\CrudWindow\\\\Table\\MainTable\\CreateTableMenu.ui"
        uic.loadUi(UI_PATH, self)
        
        # Initialize Signals
        self.AddColumn.clicked.connect(self.tableColumnFunction)        
        self.Exit.clicked.connect(self.tableExit)                        
        self.Submit.clicked.connect(self.submitTable)                    
        self.Delete.clicked.connect(self.deleteAttribute);              
        stuff = self.tableWidget.horizontalHeader();
        stuff.setStretchLastSection(True);
        
        # Initialize API
        self.API = apiCrud;
        self.show()

    def deleteAttribute(self):
        r = self.tableWidget.currentRow()
        self.tableWidget.removeRow(r)
        pass

    def readTable(self):
        # Show the table name into the label
        with open("Data/createTable/tableName.dat", "r") as f:
            self.table_name.setText(f.readline())

    def readAttributeData(self):
        colPos = 0
        # Read the column
        with open("Data/createTable/columnName.dat", "r") as f:
            columnName = f.readline();
            rowPosition = self.tableWidget.rowCount();

            # Insert each data in the table
            self.tableWidget.insertRow(rowPosition);
            self.tableWidget.setItem(rowPosition,colPos,QTableWidgetItem(columnName))
            colPos += 1

        with open("Data/createTable/type.dat","r") as f:
            typeName = f.readline();
            # Insert each data in the table
            self.tableWidget.setItem(rowPosition,colPos,QTableWidgetItem(typeName))
            colPos += 1
            
        constraintFile = open("Data/createTable/constraints.dat","r+"); 
        fkFile = open("Data/createTable/fk.dat","r+")
        typeFile = open("Data/createTable/type.dat","r");
        colFile = open("Data/createTable/columnName.dat", "r");
        
        str = ' ' + constraintFile.readline() + ',' + fkFile.readline() + ' '
        # Insert an item in the table
        self.tableWidget.setItem(rowPosition,colPos,QTableWidgetItem(str))
        
        # Write out the command for later use when commiting in SQL
        with open("Data/createTable/command.dat", 'a') as f:
            f.writelines( ' ' + colFile.readline() + ' ' + typeFile.readline() + str + '\n')
        constraintFile.truncate();
        fkFile.truncate();
        constraintFile.close();
        fkFile.close();

    # Switch Table Column
            
    def tableColumnFunction(self):
        Widget.setFixedWidth(610)
        Widget.setFixedHeight(360)
        Widget.setCurrentIndex(8)

    # Return Exit   ->  #3
    def tableExit(self):
        Widget.setFixedWidth(1100)
        Widget.setFixedHeight(650)
        
        # Open all files and delete the contents of it
        colName = open("Data/createTable/columnName.dat", "w")
        colName.truncate()
        colName.close()
        
        constraints = open("Data/createTable/constraints.dat", "w")
        constraints.truncate()
        constraints.close()
        
        fk = open("Data/createTable/fk.dat", "w")
        fk.truncate()
        fk.close()
        
        tableName = open("Data/createTable/tableName.dat", "w")
        tableName.truncate()
        tableName.close()
        
        typeName = open("Data/createTable/type.dat", "w")
        typeName.truncate()
        typeName.close()
        
        commandFile = open("Data/createTable/command.dat", "w")
        commandFile.truncate()
        commandFile.close()
        
        self.tableWidget.setRowCount(0);
        
        Widget.setCurrentIndex(3)

    # Add table to CRUD   ->  #3
    def submitTable(self):
        
        # Remove all the contents of the file
        colName = open("Data/createTable/columnName.dat", "w")
        colName.truncate()
        colName.close()
        
        # Remove all the contents of the file
        constraints = open("Data/createTable/constraints.dat", "w")
        constraints.truncate()
        constraints.close()
        
        # Remove all the contents of the file
        fk = open("Data/createTable/fk.dat", "w")
        fk.truncate()
        fk.close()
        
        # Remove all the contents of the file
        typeName = open("Data/createTable/type.dat", "w")
        typeName.truncate()
        typeName.close()
        
        # Get the command 
        commandFile = open("Data/createTable/command.dat", "r+")
        value = commandFile.read().removesuffix('\n').removesuffix(' ').removesuffix(',')
        commandFile.truncate()
        commandFile.close()
        
        # Call the API for creating a table
        try:
            tableName = open("Data/createTable/tableName.dat", "r+")
            self.API.createTable(tableName.read(),value);
            tableName.truncate()
            tableName.close()
            
            Widget.setFixedWidth(1100)
            Widget.setFixedHeight(650)
            Widget.widget(3).loadNewTable(self.table_name.text())
            Widget.setCurrentIndex(3)
        except:
            if len(value) < 1:
                pop_message("No Data Submitted")
            else:
                pop_message("UNKNOWN ERROR: Please Try again and report this problem")            
                self.tableWidget.setRowCount(0);
                

        
       

# Table Column Window

class TableColumn(QtWidgets.QDialog):

    def __init__(self , apiCrud):
        super().__init__()
        UI_PATH = "GUI\\CrudWindow\\\\Table\\MainTable\\CreateTable_ColProperties.ui"
        uic.loadUi(UI_PATH, self)
        
        # Initialize Signals
        self.COK.clicked.connect(self.okButton)                 
        self.CCancel.clicked.connect(self.cancelFunction)     
        
        # initialize API  
        self.API = apiCrud;

    # OK Button / Condition 

    def okButton(self):
        consFile = open("Data/createTable/constraints.dat", 'r+')
        consFile.truncate();
        
        # Write the appropriate value to what is check in the window
        if self.primary_key.isChecked():
            consFile.write(" PRIMARY KEY ");
        if self.not_null.isChecked():
            consFile.write(" NOT NULL ");
        if self.unique.isChecked():
            consFile.write(" UNIQUE ");
        consFile.close()
        
        # If the foreign key is check, go to the forign key window
        if self.foreign_key.isChecked():
            self.foreignKeyFunction();
        else:
            Widget.setCurrentIndex(7)
            
        self.primary_key.setCheckState(False);
        self.not_null.setCheckState(False);
        self.unique.setCheckState(False);
        self.foreign_key.setCheckState(False);
        
        # Save the data
        self.saveData();
        Widget.setFixedWidth(955)
        Widget.setFixedHeight(550)
        Widget.widget(7).readAttributeData();

    # Foreign Key Window

    def foreignKeyFunction(self):
        Widget.setCurrentIndex(9)
        
    def cancelFunction(self):
        Widget.setCurrentIndex(7)
        
    # Save data

    def saveData(self):
        with open("Data/createTable/columnName.dat", "w") as f:
            f.write(self.column_input.toPlainText())
        with open("Data/createTable/type.dat","w") as f:
            f.write(self.type_input.toPlainText())
            
# Add Foreign Key Window

class ForeignKey(QtWidgets.QDialog): 

    def __init__(self, apiCrud):
        super().__init__()
        UI_PATH = "GUI\\CrudWindow\\\\Table\\MainTable\\CreateTable_FK.ui"
        uic.loadUi(UI_PATH, self)
        
        # Initialize Signals
        self.FKOK.clicked.connect(self.OKFunction)                      
        self.FKCancel.clicked.connect(self.CancelFunction)         
        
        # Initialize API
        self.API = apiCrud;

    def OKFunction(self):
        # Write the appropriate command for the foreign key
        with open("Data/createTable/fk.dat", "w") as f:
            f.write( ' FOREIGN KEY(' + self.from_input.toPlainText() + ') ')
            # Lack of Information
            f.write( ' REFERENCES ' + self.referenes_input.toPlainText() +  '(' + self.attributename_input.toPlainText() +') ')
        Widget.setFixedWidth(955)
        Widget.setFixedHeight(550)
        Widget.widget(7).readAttributeData();
        Widget.setCurrentIndex(7)
            
    # Cancel Button 
    
    def CancelFunction(self):
        Widget.setCurrentIndex(7)

