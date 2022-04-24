from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from tkinter import Widget
import sys
import os

#Filter Window Class

class FilterTable(QDialog): 
    def __init__(self):
        super(FilterTable, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\FilterTable.ui" 
        self.ui = loadUi(UIPATH,self)
        self.FOKbutton.clicked.connect(self.gotoaddCRUD)  
        self.FExitbutton.clicked.connect(self.gotocancelCRUD)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

## Functions of the Buttons // Both will Go Back to the Main Crud Window 

    def gotoaddCRUD(self):
        AddCRUD = MainCrudWindow()  # MainCrudWindow is the class of MAIN // Depends kay JC
        Widget.addWidget(AddCRUD)
        Widget.setCurrentIndex(Widget.currentIndex()+1)
        self.pop_message("Table is Succesfully Filtered!") #Di ko na-try kasi di pa merge sa gawa ni JC

    
    def gotocancelCRUD(self):
        CancelCRUD = MainCrudWindow() # MainCrudWindow is the class of MAIN // Depends kay JC
        Widget.addWidget(CancelCRUD)
        Widget.setCurrentIndex(Widget.currentIndex()+1)
        self.pop_message("Process Failure!") #Di ko na-try kasi di pa merge sa gawa ni JC


app=QApplication(sys.argv)
mainwindow=FilterTable()
Widget=QtWidgets.QStackedWidget()
Widget.addWidget(mainwindow)
Widget.setFixedWidth(600)
Widget.setFixedHeight(350)
Widget.show()
app.exec()
