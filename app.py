import sys
import os

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QRegExpValidator, QTextCursor


main_ui           = uic.loadUiType(os.path.join("ui", "main.ui"))[0] 

class MyApp(QMainWindow, main_ui):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    


if __name__ == "__main__" :

    
    
    app = QApplication(sys.argv)
    
    myApp = MyApp()
    
    myApp.show()
    
    app.exec_()