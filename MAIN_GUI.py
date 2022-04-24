from GUI.SignInWindow.SignIn import *
from GUI.globalVariable import *


SignInWindow=SignIn()
Widget.addWidget(SignInWindow)
Widget.setFixedWidth(600)
Widget.setFixedHeight(350)
Widget.show()

app.exec()
