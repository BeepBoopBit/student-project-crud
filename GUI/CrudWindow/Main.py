from email import header
import os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *
from CRUD_API import *
from datetime import datetime
class MainCrudWindow(QDialog):

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def __init__(self, apiCrud):
        super(MainCrudWindow, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\Main.ui"
        self.ui = loadUi(UIPATH, self)
        self.API = apiCrud;

        self.MAddButton.clicked.connect(self.AddAttribute)
        self.MGroupButton.clicked.connect(self.GroupAttribute)
        self.MFitlerButton.clicked.connect(self.FilterAttribute)
        self.MSearchButton.clicked.connect(self.SearchAttribute)
        self.MModifyButton.clicked.connect(self.ModifyAttribute)
        self.MCreateButton.clicked.connect(self.CreateAttribute)
        self.MDeleteButton.clicked.connect(self.DeleteAttribute)
        self.MChangeButton.clicked.connect(self.ChangeAttribute)
        self.MSignOutButton.clicked.connect(self.SignOutAttribute)

        self.loadData();
        # Load the data

    def loadData(self):
        
        while self.tabWidget.count():
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
            
        tableList = self.API.getTableList();
        if len(tableList) <= 0:
            pass
        else:
            count = 0
            for i in tableList:
                with open("Data/database/tableList.dat", 'a') as f:
                    f.writelines(i + '\n');
                self.tabWidget.addTab(QTableWidget(), i)
                self.tabWidget.setCurrentIndex(count)
                headerCount = 0;
                tempAttributeList =self.API.getAttributeList(i) 
                stuff = self.tabWidget.currentWidget().horizontalHeader();
                stuff.setStretchLastSection(True);
                isFirst = True;

                attListFile = open("Data/database/attributeList.dat", 'a')
                for j in tempAttributeList:
                    attListFile.writelines(str(j[0]) + ' ')
                    colCount = self.tabWidget.currentWidget().columnCount()
                    self.tabWidget.currentWidget().insertColumn(colCount);
                    self.tabWidget.currentWidget().setHorizontalHeaderItem(headerCount,QTableWidgetItem(j[0]))
                    rowPosition = -1;
                    for data in self.API.getDataFrom(i, j[0]):
                        if isFirst:
                            rowPosition = self.tabWidget.currentWidget().rowCount();
                            self.tabWidget.currentWidget().insertRow(rowPosition);
                        else:
                            rowPosition += 1;
                        try:
                            self.tabWidget.currentWidget().setItem(rowPosition,headerCount,QTableWidgetItem(str(data)))
                        except:
                            dateTime = data.strftime("%Y-%m-%d")
                            self.tabWidget.currentWidget().setItem(rowPosition,headerCount,QTableWidgetItem(dateTime))
                    isFirst = False;
                    headerCount += 1;
                attListFile.writelines("\n")
                count += 1
    
    def AddAttribute(self):
        pass

    def GroupAttribute(self): #Grouping table is the class of group ui
        Widget.setCurrentIndex(5)

    def FilterAttribute(self): #Filter table is the class of filter ui
        Widget.setCurrentIndex(4)
        
    def SearchAttribute(self):
        pass

    def ModifyAttribute(self): #Modify Table is the class of modify ui
        Widget.widget(6).loadData(self.tabWidget.tabText(self.tabWidget.currentIndex()),self.tabWidget.currentIndex())
        Widget.setCurrentIndex(6)
        

    def CreateAttribute(self): #Create Table is the class of create ui
        Widget.setCurrentIndex(7);
        

    def DeleteAttribute(self):
        pass

    def ChangeAttribute(self):
        Widget.setCurrentIndex(1)


    def SignOutAttribute(self): #Sign out is the class of sign out ui
        Widget.setCurrentIndex(0)



    

