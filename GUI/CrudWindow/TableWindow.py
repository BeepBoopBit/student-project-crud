import os
from PyQt5 import QtWidgets, uic
from tkinter import Widget
from GUI.globalVariable import *


class NameTable(QtWidgets.QDialog): # Create Table Window
    def __init__(self):
        super().__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateTable.ui"
        uic.loadUi(UIPATH, self)
        self.TOK.clicked.connect(self.TableMenuFunction)
        self.TCancel.clicked.connect(self.tableCancel)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()        
        
    def TableMenuFunction(self):
        self.pop_message(text="Table Succesfully Created!") 
        Widget.setCurrentIndex(8)

    def tableCancel(self):
        Widget.setCurrentIndex(3)

##################################################################

class TableMenu(QtWidgets.QDialog): # Table Menu Window
    def __init__(self):
        super().__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateTableMenu.ui"
        uic.loadUi(UIPATH, self)
        self.AddColumn.clicked.connect(self.tableColumnFunction)
        self.Exit.clicked.connect(self.tableExit)
        self.Submit.clicked.connect(self.submitTable)
        self.show()

    def tableColumnFunction(self):
        Widget.setCurrentIndex(9)

    def tableExit(self):
        Widget.setCurrentIndex(3)

    def submitTable():
        Widget.setCurrentIndex(3)

##################################################################

class TableColumn(QtWidgets.QDialog): # Add Column Window
    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()  

    def __init__(self):
        super().__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateTable_ColProperties.ui"
        uic.loadUi(UIPATH, self)
        self.COK.clicked.connect(self.foreignKeyFunction)
        self.CCancel.clicked.connect(self.cancelFunction)

    def foreignKeyFunction(self):
        Widget.setCurrentIndex(10)
        
    def cancelFunction(self):
        Widget.setCurrentIndex(8)
        

##################################################################

class ForeignKey(QtWidgets.QDialog): # Add Foreign Key Window // IF NAKA TICK YUNG FOREIGN KEY
    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_() 
    
    def __init__(self):
        super().__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\CreateTable_FK.ui"
        uic.loadUi(UIPATH, self)
        self.FKOK.clicked.connect(self.OKFunction)
        self.FKCancel.clicked.connect(self.CancelFunction)

    def OKFunction(self):
        Widget.setCurrentIndex(8)

    def CancelFunction(self):
        Widget.setCurrentIndex(8)

##################################################################
