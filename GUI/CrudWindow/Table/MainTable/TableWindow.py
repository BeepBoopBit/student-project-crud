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
        self.TOK.clicked.connect(self.TableMenuFunction)        # Table Menu Button ->  #8
        self.TCancel.clicked.connect(self.tableCancel)          # Cancel Button     ->  #3
        self.API = apiCrud;

    # Setup table
    def TableMenuFunction(self):
        pop_message(text="Table Succesfully Created!") 
        with open("Data/createTable/tableName.dat", "w") as f:
            f.write(self.Table_Input.toPlainText());
        Widget.widget(7).readTable();
        Widget.setCurrentIndex(7)

    def tableCancel(self):
        Widget.setCurrentIndex(3)

# Table Menu Window

class TableMenu(QtWidgets.QDialog):
    def __init__(self, apiCrud):
        super().__init__()
        UI_PATH = "GUI\\CrudWindow\\\\Table\\MainTable\\CreateTableMenu.ui"
        uic.loadUi(UI_PATH, self)
        self.AddColumn.clicked.connect(self.tableColumnFunction)        # Setup Column  ->  #9
        self.Exit.clicked.connect(self.tableExit)                       # Exit          ->  #3 | Close
        self.Submit.clicked.connect(self.submitTable)                   # Submit        ->  #3 | Truncate
        self.Delete.clicked.connect(self.deleteAttribute);              # Delete Column ->  pass
        stuff = self.tableWidget.horizontalHeader();
        stuff.setStretchLastSection(True);
        
        self.API = apiCrud;
        self.show()

    # Delete Attribute

    def deleteAttribute(self):
        r = self.tableWidget.currentRow()
        self.tableWidget.removeRow(r)
        pass

    # Read table

    def readTable(self):
        with open("Data/createTable/tableName.dat", "r") as f:
            self.table_name.setText(f.readline())

    # Read attribute data

    def readAttributeData(self):
        colPos = 0
        with open("Data/createTable/columnName.dat", "r") as f:
            columnName = f.readline();
            rowPosition = self.tableWidget.rowCount();
            self.tableWidget.insertRow(rowPosition);
            self.tableWidget.setItem(rowPosition,colPos,QTableWidgetItem(columnName))
            colPos += 1

        with open("Data/createTable/type.dat","r") as f:
            typeName = f.readline();
            self.tableWidget.setItem(rowPosition,colPos,QTableWidgetItem(typeName))
            colPos += 1
            
        constraintFile = open("Data/createTable/constraints.dat","r+"); 
        fkFile = open("Data/createTable/fk.dat","r+")
        typeFile = open("Data/createTable/type.dat","r");
        colFile = open("Data/createTable/columnName.dat", "r");
        
        str = ' ' + constraintFile.readline() + ',' + fkFile.readline() + ' '
        self.tableWidget.setItem(rowPosition,colPos,QTableWidgetItem(str))
        with open("Data/createTable/command.dat", 'a') as f:
            f.writelines( ' ' + colFile.readline() + ' ' + typeFile.readline() + str + '\n')
        constraintFile.truncate(0);
        fkFile.truncate(0);
        constraintFile.close();
        fkFile.close();

    # Switch Table Column
            
    def tableColumnFunction(self):
        Widget.setCurrentIndex(8)

    # Return Exit   ->  #3

    def tableExit(self):
        colName = open("Data/createTable/columnName.dat", "w")
        command = open("Data/createTable/command.dat", "w")
        constraints = open("Data/createTable/constraints.dat", "w")
        fk = open("Data/createTable/fk.dat", "w")
        tableName = open("Data/createTable/tableName.dat", "w")
        typeName = open("Data/createTable/type.dat", "w")
        commandFile = open("Data/createTable/command.dat", "w")
        self.tableWidget.setRowCount(0);
        colName.truncate()
        command.truncate()
        constraints.truncate()
        fk.truncate()
        tableName.truncate()
        typeName.truncate()
        commandFile.truncate()
        
        
        colName.close()
        command.close()
        constraints.close()
        fk.close()
        tableName.close()
        typeName.close()
        commandFile.close()
        
        Widget.setCurrentIndex(3)

    # Add table to CRUD   ->  #3

    def submitTable(self):
        colName = open("Data/createTable/columnName.dat", "w")
        constraints = open("Data/createTable/constraints.dat", "w")
        fk = open("Data/createTable/fk.dat", "w")
        tableName = open("Data/createTable/tableName.dat", "r+")
        typeName = open("Data/createTable/type.dat", "w")
        commandFile = open("Data/createTable/command.dat", "r+")
        value = commandFile.read().removesuffix('\n').removesuffix(' ').removesuffix(',')
        self.API.createTable(tableName.read(),value);
        self.tableWidget.setRowCount(0);
        colName.truncate()
        commandFile.truncate()
        constraints.truncate()
        fk.truncate()
        tableName.truncate()
        typeName.truncate()
        commandFile.truncate()
        Widget.widget(3).loadData()
        Widget.setCurrentIndex(3)

# Table Column Window

class TableColumn(QtWidgets.QDialog):

    def __init__(self , apiCrud):
        super().__init__()
        UI_PATH = "GUI\\CrudWindow\\\\Table\\MainTable\\CreateTable_ColProperties.ui"
        uic.loadUi(UI_PATH, self)
        self.COK.clicked.connect(self.okButton)                 # OK Button         ->  #8 / #10
        self.CCancel.clicked.connect(self.cancelFunction)       # Cancel Button     ->  #8
        self.API = apiCrud;

    # OK Button / Condition 

    def okButton(self):
        consFile = open("Data/createTable/constraints.dat", 'a')
        if self.primary_key.isChecked():
            consFile.write(" PRIMARY KEY ");
        if self.not_null.isChecked():
            consFile.write(" NOT NULL ");
        if self.unique.isChecked():
            consFile.write(" UNIQUE ");
        consFile.close()
        if self.foreign_key.isChecked():
            self.foreignKeyFunction();
        else:
            Widget.setCurrentIndex(7)
        self.saveData();
        Widget.widget(7).readAttributeData();

        pass

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
        self.FKOK.clicked.connect(self.OKFunction)                  # OK Button         ->  #8        
        self.FKCancel.clicked.connect(self.CancelFunction)          # Cancel Button     ->  #8
        self.API = apiCrud;

    # OK Button

    def OKFunction(self):
        with open("Data/createTable/fk.dat", "w") as f:
            f.write( ' FOREIGN KEY(' + self.from_input.toPlainText() + ') ')
            # Lack of Information
            f.write( ' REFERENCES ' + self.referenes_input.toPlainText() +  '(' + self.attributename_input.toPlainText() +') ')
        Widget.widget(7).readAttributeData();
        Widget.setCurrentIndex(7)
            
    # Cancel Button 
    
    def CancelFunction(self):
        Widget.setCurrentIndex(7)

