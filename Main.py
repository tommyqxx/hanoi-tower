# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from hello_world import *
from ex_Hanoi_Tower_prob import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 320)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 41, 28))
        self.pushButton.setObjectName("pushButton")
        self.lbl_1 = QtWidgets.QLabel(Form)
        self.lbl_1.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.lbl_1.setObjectName("lbl_1")
        self.txb_input = QtWidgets.QLineEdit(Form)
        self.txb_input.setGeometry(QtCore.QRect(10, 30, 113, 22))
        self.txb_input.setObjectName("txb_input")
        self.lbl_2 = QtWidgets.QLabel(Form)
        self.lbl_2.setGeometry(QtCore.QRect(10, 100, 55, 16))
        self.lbl_2.setObjectName("lbl_2")
        self.txbr_output = QtWidgets.QTextBrowser(Form)
        self.txbr_output.setGeometry(QtCore.QRect(10, 120, 221, 181))
        self.txbr_output.setObjectName("txbr_output")
        self.pushButton.clicked.connect(self.on_click)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.lbl_1.setText(_translate("Form", "Give a number of tower:"))
        self.lbl_2.setText(_translate("Form", "Result:"))

    #@pyqtSlot()
    def on_click(self):
        self.txbr_output.setText("")
        #self.txb_input.setText(input())
        a=self.txb_input.text()
       # b = hello_world(a)
        #print(a)
        #print(b)
        #self.txbr_output(b)
        #self.txbr_output.setText(a)
       # self.txbr_output.setText(hello_world(a))
        print('button clicked')

        #hanoi_tower(n, a, b, c, arr):
        output=[]
       # print(hanoi_tower(int(a),'A','B','C',output))
       # print(b)
        self.txbr_output.setText(str(hanoi_tower(int(a),'A','B','C',output)))




        #clear txbr_1
        #get input from txb_1
        #call function


if __name__=="__main__":
    import sys
    from PyQt5.QtGui import QIcon
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())


