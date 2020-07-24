import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("groupRadioButton.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #GroupBox안에 있는 RadioButton들을 연결합니다.
        self.groupBox_rad1.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad2.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad3.clicked.connect(self.groupboxRadFunction)

    def groupboxRadFunction(self) :
        if self.groupBox_rad1.isChecked() : print("GroupBox_rad1 Chekced")
        elif self.groupBox_rad2.isChecked() : print("GroupBox_rad2 Checked")
        elif self.groupBox_rad3.isChecked() : print("GroupBox_rad3 Checked")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()