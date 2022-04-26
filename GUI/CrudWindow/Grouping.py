import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from GUI.globalVariable import *

# Load GroupingTable Window

class GroupingTable(QDialog):
    def __init__(self, apiCrud):
        super(GroupingTable, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\Grouping.ui" 
        self.ui = loadUi(UIPATH,self)
        self.GBOkButton.clicked.connect(self.GBOkButton)
        self.GBExitButton.clicked.connect(self.GBExitButton)
        self.GBAddAttribute.clicked.connect(self.SelectAddAttribute)
        self.API = apiCrud;

        # PopUp Message Setup

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()        
        
    def GBOkButton(self):
        pass


    def GBExitButton(self):
        pass

# Load SelectAttribute.ui

class SelectAddAttribute(QDialog):
    def __init__(self):
        super(SelectAddAttribute, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\SelectAttribute.ui"
        self.ui = loadUi(UIPATH, self)
        self.GBOkButton.clicked.connect(self.GBOkButton)
        self.GBExitButton.clicked.connect(self.GBExitButton)

    def GBOkButton(self):
        pass


    def GBExitButton(self):
        pass
