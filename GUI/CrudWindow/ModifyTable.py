import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *

class ModifyTable(QDialog):
    def __init__(self, apiCrud):
        super(ModifyTable, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\ModifyTable.ui" 
        self.ui = loadUi(UIPATH,self)
        self.MOKbutton.clicked.connect(self.gotoaddCRUD)
        self.MExitbutton.clicked.connect(self.gotocancelCRUD)
        self.API = apiCrud;


    def loadData(self, tableName, tabIndex):
        attrFile = open("Data/database/attributeList.dat", 'r')
        for i, attrValue in enumerate(attrFile):
            if i == tabIndex:
                attrValue = attrValue.split(' ')
                typeList = self.API.getAttributeTypes(tableName);
                for i in range(0,len(attrValue) - 1):
                    rowPosition = self.tableWidget.rowCount();
                    self.tableWidget.insertRow(rowPosition);
                    self.tableWidget.setItem(rowPosition,0,QTableWidgetItem(str(attrValue[i])))
                    self.tableWidget.setItem(rowPosition,1,QTableWidgetItem(str(typeList[i])))
                break;
    
    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    # Functions of the Buttons // Both will Go Back to the Main Crud Window 

    def gotoaddCRUD(self):
        Widget.setCurrentIndex(3)

    
    def gotocancelCRUD(self):
        self.tableWidget.setRowCount(0)
        Widget.setCurrentIndex(3)
