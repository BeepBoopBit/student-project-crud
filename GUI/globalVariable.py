import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

# Setting-up the Window
app = QApplication(sys.argv)
Widget = QtWidgets.QStackedWidget();

# PopUp message set-up
def pop_message(text=""): 
    msg = QtWidgets.QMessageBox()
    msg.setText("{}".format(text))
    msg.exec_()