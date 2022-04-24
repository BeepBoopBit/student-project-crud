from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from tkinter import Widget
import sys
import os

class ModifyTable(QDialog):
    def __init__(self):
        super(ModifyTable, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\ModifyTable.ui" 
        self.ui = loadUi(UIPATH,self)
        self.MOKbutton.clicked.connect(self.gotoaddCRUD)
        self.MExitbutton.clicked.connect(self.gotocancelCRUD)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    # Functions of the Buttons // Both will Go Back to the Main Crud Window 

    def gotoaddCRUD(self):
        AddCRUD = MainCrudWindow() 
        Widget.addWidget(AddCRUD)
        Widget.setCurrentIndex(Widget.currentIndex()+1)
        self.pop_message("Table is Succesfully Filtered!")

    
    def gotocancelCRUD(self):
        CancelCRUD = MainCrudWindow()
        Widget.addWidget(CancelCRUD)
        Widget.setCurrentIndex(Widget.currentIndex()+1)
        self.pop_message("Process Failure!")

app=QApplication(sys.argv)
mainwindow=ModifyTable()
Widget=QtWidgets.QStackedWidget()
Widget.addWidget(mainwindow)
Widget.setFixedWidth(600)
Widget.setFixedHeight(350)
Widget.show()
app.exec()