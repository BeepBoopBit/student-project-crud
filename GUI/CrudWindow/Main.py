from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from tkinter import Widget
import sys
import os


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
        self.MFilterButton.clicked.connect(self.FilterAttribute)
        self.MSearchButton.clicked.connect(self.SearchAttribute)
        self.MModifyButton.clicked.connect(self.ModifyAttribute)
        self.MCreateButton.clicked.connect(self.CreateAttribute)
        self.MDeleteButton.clicked.connect(self.DeleteAttribute)
        self.MDeleteButton.clicked.connect(self.ChangeAttribute)
        self.MDeleteButton.clicked.connect(self.SignOutAttribute)

    
    #def AddAttribute(self):
    #    addAttribute = MainCrudWindow() 
    #    Widget.addWidget(AddCRUD)
    #    Widget.setCurrentIndex(Widget.currentIndex()+1)
    #    self.pop_message("Successfully Added!")

    def GroupAttribute(self): #Grouping table is the class of group ui
        groupAttribute = GroupingTable() 
        Widget.addWidget(groupAttribute)
        Widget.setCurrentIndex(Widget.currentIndex()+1)
        

    def FilterAttribute(self): #Filter table is the class of filter ui
        filterAttribute = FilterTable() 
        Widget.addWidget(filterAttribute)
        Widget.setCurrentIndex(Widget.currentIndex()+1)
        

    #def SearchAttribute(self):
    #    searchAttribute = MainCrudWindow() 
    #    Widget.addWidget(AddCRUD)
    #    Widget.setCurrentIndex(Widget.currentIndex()+1)
    #    self.pop_message("Table is Succesfully Filtered!")

    def ModifyAttribute(self): #Modify Table is the class of modify ui
        modifyAttribute = ModifyTable() 
        Widget.addWidget(modifyAttribute)
        Widget.setCurrentIndex(Widget.currentIndex()+1)
        

    def CreateAttribute(self): #Create Table is the class of create ui
        createAttribute = NameTable() 
        Widget.addWidget(createAttribute)
        Widget.setCurrentIndex(Widget.currentIndex()+1)
        

    #def DeleteAttribute(self):
    #    deleteAttribute = MainCrudWindow() 
    #    Widget.addWidget(AddCRUD)
    #    Widget.setCurrentIndex(Widget.currentIndex()+1)
    #    self.pop_message("Table is Succesfully Filtered!")

    #def ChangeAttribute(self):
    #    changeAttribute = MainCrudWindow() 
    #    Widget.addWidget(AddCRUD)
    #    Widget.setCurrentIndex(Widget.currentIndex()+1)
    #    self.pop_message("Table is Succesfully Filtered!")

    def SignOutAttribute(self): #Sign out is the class of sign out ui
        signoutAttribute = SignIn() 
        Widget.addWidget(signoutAttribute)
        Widget.setCurrentIndex(Widget.currentIndex()+1)
        self.pop_message("Logout")



    

