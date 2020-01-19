# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1422, 819)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 60, 16))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 750, 1121, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_x = QtWidgets.QLabel(self.frame)
        self.label_x.setGeometry(QtCore.QRect(10, 10, 71, 41))
        self.label_x.setObjectName("label_x")
        self.label_y = QtWidgets.QLabel(self.frame)
        self.label_y.setGeometry(QtCore.QRect(180, 10, 71, 41))
        self.label_y.setObjectName("label_y")
        self.label_X = QtWidgets.QLabel(self.frame)
        self.label_X.setGeometry(QtCore.QRect(80, 10, 91, 41))
        self.label_X.setObjectName("label_X")
        self.label_Y = QtWidgets.QLabel(self.frame)
        self.label_Y.setGeometry(QtCore.QRect(270, 10, 101, 41))
        self.label_Y.setObjectName("label_Y")
        self.btn_send = QtWidgets.QPushButton(self.frame)
        self.btn_send.setGeometry(QtCore.QRect(700, 0, 181, 61))
        self.btn_send.setObjectName("btn_send")
        self.label_D = QtWidgets.QLabel(self.frame)
        self.label_D.setGeometry(QtCore.QRect(410, 10, 101, 41))
        self.label_D.setObjectName("label_D")
        self.label_d = QtWidgets.QLabel(self.frame)
        self.label_d.setGeometry(QtCore.QRect(520, 10, 121, 41))
        self.label_d.setObjectName("label_d")
        self.btn_save = QtWidgets.QPushButton(self.frame)
        self.btn_save.setGeometry(QtCore.QRect(920, 0, 171, 61))
        self.btn_save.setObjectName("btn_save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_x.setText(_translate("Form", "X"))
        self.label_y.setText(_translate("Form", "Y"))
        self.label_X.setText(_translate("Form", "TextLabel"))
        self.label_Y.setText(_translate("Form", "TextLabel"))
        self.btn_send.setText(_translate("Form", "send"))
        self.label_D.setText(_translate("Form", "D"))
        self.label_d.setText(_translate("Form", "TextLabel"))
        self.btn_save.setText(_translate("Form", "Save Img"))
