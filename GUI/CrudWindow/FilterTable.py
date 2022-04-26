import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from GUI.globalVariable import *

# Filter Window Class

class FilterTable(QDialog): 
    def __init__(self, apiCrud):
        super(FilterTable, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\FilterTable.ui" 
        self.ui = loadUi(UIPATH,self)
        self.FOKbutton.clicked.connect(self.gotoaddCRUD)  
        self.FExitbutton.clicked.connect(self.gotocancelCRUD)
        self.API = apiCrud;
        
    # PopUp Message Setup

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

## Functions of the Buttons // Both will Go Back to the Main Crud Window 

    def gotoaddCRUD(self):
        self.pop_message("Process Success!") # Di ko na-try kasi di pa merge sa gawa ni JC
        Widget.setCurrentIndex(3)

    
    def gotocancelCRUD(self):
        self.pop_message("Process Failure!") # Di ko na-try kasi di pa merge sa gawa ni JC
        Widget.setCurrentIndex(3)

