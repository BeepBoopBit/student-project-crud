import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from GUI.globalVariable import *


class MainCrudWindow(QDialog):

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def __init__(self):
        super(MainCrudWindow, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\Main.ui"
        self.ui = loadUi(UIPATH, self)

        self.MAddButton.clicked.connect(self.AddAttribute)
        self.MGroupButton.clicked.connect(self.GroupAttribute)
        self.MFitlerButton.clicked.connect(self.FilterAttribute)
        self.MSearchButton.clicked.connect(self.SearchAttribute)
        self.MModifyButton.clicked.connect(self.ModifyAttribute)
        self.MCreateButton.clicked.connect(self.CreateAttribute)
        self.MDeleteButton.clicked.connect(self.DeleteAttribute)
        self.MChangeButton.clicked.connect(self.ChangeAttribute)
        self.MSignOutButton.clicked.connect(self.SignOutAttribute)

    
    def AddAttribute(self):
        pass

    def GroupAttribute(self): #Grouping table is the class of group ui
        Widget.setCurrentIndex(5)

    def FilterAttribute(self): #Filter table is the class of filter ui
        Widget.setCurrentIndex(4)
        
    def SearchAttribute(self):
        pass

    def ModifyAttribute(self): #Modify Table is the class of modify ui
        Widget.setCurrentIndex(6)
        

    def CreateAttribute(self): #Create Table is the class of create ui
        Widget.setCurrentIndex(7)
        

    def DeleteAttribute(self):
        pass

    def ChangeAttribute(self):
        Widget.setCurrentIndex(1)


    def SignOutAttribute(self): #Sign out is the class of sign out ui
        Widget.setCurrentIndex(0)



    

