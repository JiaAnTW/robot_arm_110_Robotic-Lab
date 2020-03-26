# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, Form):
        Form.setObjectName("物件資訊")
        Form.resize(450, 534)

        self.objInfoWidget = QtWidgets.QWidget(Form)
        self.objInfoWidget.setGeometry(QtCore.QRect(0, 10, 421, 221))
        self.objInfoWidget.setObjectName("objInfoWidget")
        self.objLayout= QtWidgets.QGridLayout(self.objInfoWidget)
        self.objLayout.setContentsMargins(0, 0, 0, 0)
        self.objLayout.setObjectName("objLayout")

        self.obj_topic = QtWidgets.QLabel(self.objInfoWidget)
        self.obj_topic.setObjectName("obj_topic")
        self.objLayout.addWidget(self.obj_topic, 0, 0, 1, 1)
        self.obj_status = QtWidgets.QLabel(self.objInfoWidget)
        self.obj_status.setObjectName("obj_status")
        self.objLayout.addWidget(self.obj_status, 0, 1, 1, 1)

        self.obj_label = QtWidgets.QLabel(self.objInfoWidget)
        self.obj_label.setObjectName("obj_label")
        self.objLayout.addWidget(self.obj_label, 1, 0, 1, 1)
        self.objPos_label = QtWidgets.QLabel(self.objInfoWidget)
        self.objPos_label.setObjectName("objPos_label")
        self.objLayout.addWidget(self.objPos_label, 1, 1, 1, 1)

        self.objBtnLabel = QtWidgets.QLabel(self.objInfoWidget)
        self.objBtnLabel.setObjectName("objBtnLabel")
        self.objLayout.addWidget(self.objBtnLabel, 1, 2, 1, 1)

        self.objArr=[]

        self.objLayout.setColumnStretch(0, 1)
        self.objLayout.setColumnStretch(1, 2)
        self.objLayout.setColumnStretch(2, 1)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 460, 441, 91))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_correct = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_correct.setObjectName("btn_correct")
        self.horizontalLayout_4.addWidget(self.btn_correct)
        self.btn_detect = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_detect.setObjectName("btn_detect")
        self.horizontalLayout_4.addWidget(self.btn_detect)
        self.btn_always_detect = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_always_detect.setObjectName("btn_always_detect")
        self.horizontalLayout_4.addWidget(self.btn_always_detect)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.objPos_label.setText(_translate("Form", "所在座標"))
        self.obj_label.setText(_translate("Form", "物體列表"))
        self.obj_topic.setText(_translate("Form", "偵測狀態："))
        self.obj_status.setText(_translate("Form", "[ 未偵測 ]"))
        self.btn_correct.setText(_translate("Form", "校正"))
        self.btn_detect.setText(_translate("Form", "單次偵測物體"))
        self.btn_always_detect.setText(_translate("Form", "開啟即時偵測"))