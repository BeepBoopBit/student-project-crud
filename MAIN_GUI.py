from GUI.SignInWindow.SignIn import *
from GUI.globalVariable import *
from GUI.DatabaseWindow.Database import *

SignInWindow=SignIn()
Widget.addWidget(SignInWindow)
Widget.setFixedWidth(1100)
Widget.setFixedHeight(650)
Widget.show()

app.exec()