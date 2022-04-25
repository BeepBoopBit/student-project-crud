import os
from PyQt5 import QtWidgets, uic
from tkinter import Widget
from GUI.globalVariable import *
from PyQt5.QtWidgets import QTableWidgetItem


class NameTable(QtWidgets.QDialog): # Create Table Window
    def __init__(self, apiCrud):
        super().__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateTable.ui"
        uic.loadUi(UIPATH, self)
        self.TOK.clicked.connect(self.TableMenuFunction)
        self.TCancel.clicked.connect(self.tableCancel)
        self.API = apiCrud;

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()        
        
    def TableMenuFunction(self):
        self.pop_message(text="Table Succesfully Created!") 
        with open("Data/createTable/tableName.dat", "w") as f:
            f.write(self.Table_Input.toPlainText());
        Widget.widget(8).readTable();
        Widget.setCurrentIndex(8)

    def tableCancel(self):
        Widget.setCurrentIndex(3)

##################################################################

class TableMenu(QtWidgets.QDialog): # Table Menu Window
    def __init__(self, apiCrud):
        super().__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateTableMenu.ui"
        uic.loadUi(UIPATH, self)
        self.AddColumn.clicked.connect(self.tableColumnFunction)
        self.Exit.clicked.connect(self.tableExit)
        self.Submit.clicked.connect(self.submitTable)
        
        stuff = self.tableWidget.horizontalHeader();
        stuff.setStretchLastSection(True);
        
        
        self.API = apiCrud;
        self.show()

    def readTable(self):
        with open("Data/createTable/tableName.dat", "r") as f:
            self.table_name.setText(f.readline())

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
        str = ' ' + constraintFile.readline() + ' ' + fkFile.readline() + ' '
        self.tableWidget.setItem(rowPosition,colPos,QTableWidgetItem(str))
        constraintFile.truncate(0);
        fkFile.truncate(0);
        constraintFile.close();
        fkFile.close();
            
            
            
    def tableColumnFunction(self):
        Widget.setCurrentIndex(9)

    def tableExit(self):
        Widget.setCurrentIndex(3)

    def submitTable(self):
        # IMPLEMENT THE API
        Widget.setCurrentIndex(3)

##################################################################

class TableColumn(QtWidgets.QDialog): # Add Column Window
    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()  

    def __init__(self , apiCrud):
        super().__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateTable_ColProperties.ui"
        uic.loadUi(UIPATH, self)
        self.COK.clicked.connect(self.okButton)
        self.CCancel.clicked.connect(self.cancelFunction)
        self.API = apiCrud;

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
            self.saveData();
            Widget.widget(8).readAttributeData();
            Widget.setCurrentIndex(8)
        pass

    def foreignKeyFunction(self):
        Widget.setCurrentIndex(10)
        
    def cancelFunction(self):
        Widget.setCurrentIndex(8)
        
    def saveData(self):
        with open("Data/createTable/columnName.dat", "w") as f:
            f.write(self.column_input.toPlainText())
        with open("Data/createTable/type.dat","w") as f:
            f.write(self.type_input.toPlainText())
            
##################################################################

class ForeignKey(QtWidgets.QDialog): # Add Foreign Key Window // IF NAKA TICK YUNG FOREIGN KEY
    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_() 
    
    def __init__(self, apiCrud):
        super().__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateTable_FK.ui"
        uic.loadUi(UIPATH, self)
        self.FKOK.clicked.connect(self.OKFunction)
        self.FKCancel.clicked.connect(self.CancelFunction)
        self.API = apiCrud;

    def OKFunction(self):
        with open("Data/createTable/fk.dat", "w") as f:
            f.write( ' ' + self.from_input.toPlainText() + ' ')
            f.write( ' ' + self.referenes_input.toPlainText() +  ' ')
        Widget.widget(8).readAttributeData();
        Widget.setCurrentIndex(8)
            

    def CancelFunction(self):
        Widget.setCurrentIndex(8)

##################################################################
