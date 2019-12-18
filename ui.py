# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
try:
    from pyDobot import Dobot
    except Exception as e:
            print(e)

class Ui_Form(object):
    def __init__(self):
        self.user_set_pos=(0,0,0,0,0,0,0,0)
        self._connect_dobot(0)

    def _connect_dobot(self,i):
        try:
            portArray=["ttyUSB0","ttyUSB01","ttyUSB2","ttyUSB3","ttyUSB4","ttyUSB5","ttyS0","ttyS1","ttyS2","ttyS3","ttyS4","ttyS5"]
            self.device=Dobot(post=portArray[i],verbose=False)
        except Exception as e:
            print(e)
            if(i<len(portArray)):
                self._connect_dobot(i+1)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1884, 1218)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 751, 1191))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 751, 1161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_rgb = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_rgb.setObjectName("label_rgb")
        self.verticalLayout.addWidget(self.label_rgb)
        self.label_d = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_d.setObjectName("label_d")
        self.verticalLayout.addWidget(self.label_d)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(790, 20, 551, 1171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(-10, 30, 531, 771))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.btn_go = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_go.setGeometry(QtCore.QRect(50, 660, 191, 91))
        self.btn_go.setObjectName("btn_go")

        self.btn_go.clicked.connect(self.action)   #get data

        self.btn_reset = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_reset.setGeometry(QtCore.QRect(280, 660, 201, 91))
        self.btn_reset.setObjectName("btn_reset")

        self.btn_reset.clicked.connect(self.reset) #reset

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 30, 251, 601))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_x = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_x.setObjectName("input_x")
        self.verticalLayout_2.addWidget(self.input_x)
        self.input_y = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_y.setObjectName("input_y")
        self.verticalLayout_2.addWidget(self.input_y)
        self.input_z = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_z.setObjectName("input_z")
        self.verticalLayout_2.addWidget(self.input_z)
        self.input_r = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_r.setObjectName("input_r")
        self.verticalLayout_2.addWidget(self.input_r)
        self.input_j1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_j1.setObjectName("input_j1")
        self.verticalLayout_2.addWidget(self.input_j1)
        self.input_j2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_j2.setObjectName("input_j2")
        self.verticalLayout_2.addWidget(self.input_j2)
        self.input_j3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_j3.setObjectName("input_j3")
        self.verticalLayout_2.addWidget(self.input_j3)
        self.input_j4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.input_j4.setObjectName("input_j4")
        self.verticalLayout_2.addWidget(self.input_j4)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(120, 50, 129, 32))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 129, 32))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(120, 200, 129, 32))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(120, 270, 129, 32))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(120, 340, 129, 32))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(120, 410, 129, 32))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(120, 490, 129, 32))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(120, 570, 129, 32))
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(30, 870, 201, 71))
        self.label_11.setObjectName("label_11")
        self.btn_stop = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_stop.setGeometry(QtCore.QRect(20, 1000, 151, 91))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_open = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_open.setGeometry(QtCore.QRect(200, 1000, 151, 91))
        self.btn_open.setObjectName("btn_open")
        self.btn_close = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_close.setGeometry(QtCore.QRect(380, 1000, 151, 91))
        self.btn_close.setObjectName("btn_close")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(1350, 20, 531, 1181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.text_output = QtWidgets.QTextBrowser(self.groupBox_2)
        self.text_output.setGeometry(QtCore.QRect(20, 190, 511, 971))
        self.text_output.setObjectName("text_output")
        self.btn_update = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_update.setGeometry(QtCore.QRect(20, 70, 191, 101))
        self.btn_update.setObjectName("btn_update")
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.text_output.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.reset() #讓所有input歸0

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "RGB D "))
        self.label_rgb.setText(_translate("Form", "TextLabel"))
        self.label_d.setText(_translate("Form", "TextLabel"))
        self.groupBox_3.setTitle(_translate("Form", "Control"))
        self.btn_go.setText(_translate("Form", "Go"))
        self.btn_reset.setText(_translate("Form", "ReSet"))
        self.label.setText(_translate("Form", "X"))
        self.label_2.setText(_translate("Form", "Y"))
        self.label_3.setText(_translate("Form", "Z"))
        self.label_4.setText(_translate("Form", "R"))
        self.label_5.setText(_translate("Form", "Joint 1"))
        self.label_6.setText(_translate("Form", "Joint 2"))
        self.label_7.setText(_translate("Form", "Joint 3"))
        self.label_8.setText(_translate("Form", "Joint 4"))
        self.label_11.setText(_translate("Form", "Grip Control"))
        self.btn_stop.setText(_translate("Form", "STOP"))
        self.btn_open.setText(_translate("Form", "OPEN"))
        self.btn_close.setText(_translate("Form", "CLOSE"))
        self.groupBox_2.setTitle(_translate("Form", "TextBrowser"))
        self.btn_update.setText(_translate("Form", "Update"))

    def action(self): #get arm location
        self._set_user_set_pos()
        (x, y, z, r, j1, j2, j3, j4) =self.user_set_pos
        try: #call  pydobot
            self.device.move_to(x, y, z, r, j1, j2, j3, j4 wait=True)
        except Exception as e:
            print("輸入格式錯誤")
            print("錯誤訊息： "+str(e))

    def reset(self):
        self.input_x.setText("0")
        self.input_y.setText("0")
        self.input_z.setText("0")
        self.input_r.setText("0")
        self.input_j1.setText("0")
        self.input_j2.setText("0")
        self.input_j3.setText("0")
        self.input_j4.setText("0")

        self._set_user_set_pos()

    def _set_user_set_pos(self): 
        try:
            self.user_set_pos=(float(self.input_x.text()),
                                float(self.input_y.text()),
                                float(self.input_z.text()),
                                float(self.input_r.text()),
                                float(self.input_j1.text()),
                                float(self.input_j2.text()),
                                float(self.input_j3.text()),
                                float(self.input_j4.text()))
        except Exception as e:
            print("輸入格式錯誤")
            print("錯誤訊息： "+str(e))  

 

        

