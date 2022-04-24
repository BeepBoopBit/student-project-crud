from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from tkinter import Widget
import sys
import os

class NameTable(QtWidgets.QDialog): # Create Table Window
    def __init__(self):
        super().__init__()
        uic.loadUi('index\CreateTable.ui', self)
        Widget.setFixedHeight(154)
        Widget.setFixedWidth(319)
        
        self.TOK.clicked.connect(self.TableMenuFunction)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()        
        
    def TableMenuFunction(self):
        TablemenuF = TableMenu()
        Widget.addWidget(TablemenuF)
        Widget.setFixedHeight(550)
        Widget.setFixedWidth(955)
        Widget.setCurrentIndex(Widget.currentIndex()+1)
        self.pop_message(text="Table Succesfully Created!")
      
class TableMenu(QtWidgets.QDialog): # Table Menu Window
    def __init__(self):
        super().__init__()
        uic.loadUi('index\CreateTableMenu.ui', self)
        self.AddColumn.clicked.connect(self.tableColumnFunction)
        self.show()

    def tableColumnFunction(self):
        self.w = TableColumn()
        self.w.show()

class TableColumn(QtWidgets.QDialog): # Add Column Window
    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()  

    def __init__(self):
        super().__init__()
        uic.loadUi('index\CreateTable_ColProperties.ui', self)
        self.COK.clicked.connect(self.foreignKeyFunction)
        self.CCancel.clicked.connect(self.cancelFunction)

    def foreignKeyFunction(self):
        self.hide()
        self.pop_message(text="Column Succesfully Created!")
        self.w = ForeignKey()
        self.w.show()
        
    def cancelFunction(self):
        self.hide()
        self.pop_message(text="Process Failure!")

class ForeignKey(QtWidgets.QDialog): # Add Foreign Key Window // IF NAKA TICK YUNG FOREIGN KEY
    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_() 
    
    def __init__(self):
        super().__init__()
        uic.loadUi('index\CreateTable_FK.ui', self)
        self.FKOK.clicked.connect(self.OKFunction)
        self.FKCancel.clicked.connect(self.CancelFunction)

    def OKFunction(self):
        self.hide()
        self.pop_message(text="Column Succesfully Created!")

    def CancelFunction(self):
        self.hide()
        self.pop_message(text="Process Failure!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QStackedWidget()
    window = NameTable()
    Widget.addWidget(window)
    Widget.show()
    sys.exit(app.exec_())