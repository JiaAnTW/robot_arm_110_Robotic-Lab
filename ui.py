from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1905, 910)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(1310, 20, 591, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Y_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Y_label.setObjectName("Y_label")
        self.gridLayout_2.addWidget(self.Y_label, 1, 1, 1, 1)
        self.Z_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Z_label.setObjectName("Z_label")
        self.gridLayout_2.addWidget(self.Z_label, 2, 1, 1, 1)
        self.X_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.X_edit.setObjectName("X_edit")
        self.gridLayout_2.addWidget(self.X_edit, 0, 3, 1, 1)
        self.Y_output = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Y_output.setObjectName("Y_output")
        self.gridLayout_2.addWidget(self.Y_output, 1, 2, 1, 1)
        self.Z_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Z_edit.setObjectName("Z_edit")
        self.gridLayout_2.addWidget(self.Z_edit, 2, 3, 1, 1)
        self.Y_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Y_edit.setObjectName("Y_edit")
        self.gridLayout_2.addWidget(self.Y_edit, 1, 3, 1, 1)
        self.Z_output = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Z_output.setObjectName("Z_output")
        self.gridLayout_2.addWidget(self.Z_output, 2, 2, 1, 1)
        self.X_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.X_label.setObjectName("X_label")
        self.gridLayout_2.addWidget(self.X_label, 0, 1, 1, 1)
        self.R_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.R_edit.setObjectName("R_edit")
        self.gridLayout_2.addWidget(self.R_edit, 3, 3, 1, 1)
        self.R_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.R_label.setObjectName("R_label")
        self.gridLayout_2.addWidget(self.R_label, 3, 1, 1, 1)
        self.R_output = QtWidgets.QLabel(self.gridLayoutWidget)
        self.R_output.setObjectName("R_output")
        self.gridLayout_2.addWidget(self.R_output, 3, 2, 1, 1)
        self.X_output = QtWidgets.QLabel(self.gridLayoutWidget)
        self.X_output.setObjectName("X_output")
        self.gridLayout_2.addWidget(self.X_output, 0, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1440, 550, 461, 321))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_new = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_new.setObjectName("btn_new")
        self.horizontalLayout_2.addWidget(self.btn_new)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setMinimumSize(QtCore.QSize(144, 22))
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_suck = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_suck.setObjectName("btn_suck")
        self.horizontalLayout_4.addWidget(self.btn_suck)
        self.btn_free = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_free.setObjectName("btn_free")
        self.horizontalLayout_4.addWidget(self.btn_free)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(1580, 270, 321, 251))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_z_reduce = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btn_z_reduce.setObjectName("btn_z_reduce")
        self.gridLayout_3.addWidget(self.btn_z_reduce, 3, 1, 1, 1)
        self.btn_z_increase = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btn_z_increase.setObjectName("btn_z_increase")
        self.gridLayout_3.addWidget(self.btn_z_increase, 3, 0, 1, 1)
        self.btn_x_reduce = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btn_x_reduce.setObjectName("btn_x_reduce")
        self.gridLayout_3.addWidget(self.btn_x_reduce, 1, 1, 1, 1)
        self.btn_y_reduce = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btn_y_reduce.setObjectName("btn_y_reduce")
        self.gridLayout_3.addWidget(self.btn_y_reduce, 2, 1, 1, 1)
        self.btn_y_increase = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btn_y_increase.setObjectName("btn_y_increase")
        self.gridLayout_3.addWidget(self.btn_y_increase, 2, 0, 1, 1)
        self.btn_x_increase = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btn_x_increase.setObjectName("btn_x_increase")
        self.gridLayout_3.addWidget(self.btn_x_increase, 1, 0, 1, 1)
        self.input_interval = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.input_interval.setObjectName("input_interval")
        self.gridLayout_3.addWidget(self.input_interval, 0, 0, 1, 1)
        self.btn_set = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btn_set.setObjectName("btn_set")
        self.gridLayout_3.addWidget(self.btn_set, 0, 1, 1, 1)
        self.stream_label = QtWidgets.QLabel(Form)
        self.stream_label.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.stream_label.setObjectName("stream_label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 810, 1101, 61))
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
        self.label_X.setText("")
        self.label_X.setObjectName("label_X")
        self.label_Y = QtWidgets.QLabel(self.frame)
        self.label_Y.setGeometry(QtCore.QRect(270, 10, 101, 41))
        self.label_Y.setText("")
        self.label_Y.setObjectName("label_Y")
        self.label_D = QtWidgets.QLabel(self.frame)
        self.label_D.setGeometry(QtCore.QRect(410, 10, 101, 41))
        self.label_D.setObjectName("label_D")
        self.label_d = QtWidgets.QLabel(self.frame)
        self.label_d.setGeometry(QtCore.QRect(520, 10, 121, 41))
        self.label_d.setText("")
        self.label_d.setObjectName("label_d")
        self.btn_save = QtWidgets.QPushButton(self.frame)
        self.btn_save.setGeometry(QtCore.QRect(610, 0, 171, 61))
        self.btn_save.setObjectName("btn_save")
        self.btn_go = QtWidgets.QPushButton(self.frame)
        self.btn_go.setGeometry(QtCore.QRect(870, 0, 171, 61))
        self.btn_go.setObjectName("btn_go")
        self.btn_move = QtWidgets.QPushButton(Form)
        self.btn_move.setGeometry(QtCore.QRect(1330, 310, 145, 42))
        self.btn_move.setObjectName("btn_move")
        self.btn_return = QtWidgets.QPushButton(Form)
        self.btn_return.setGeometry(QtCore.QRect(1160, 810, 211, 61))
        self.btn_return.setObjectName("btn_return")
        self.btn_update_loc = QtWidgets.QPushButton(Form)
        self.btn_update_loc.setGeometry(QtCore.QRect(1330, 390, 174, 42))
        self.btn_update_loc.setObjectName("btn_update_loc")
        self.btn_rotate_j1_90 = QtWidgets.QPushButton(Form)
        self.btn_rotate_j1_90.setGeometry(QtCore.QRect(1330, 460, 174, 42))
        self.btn_rotate_j1_90.setObjectName("btn_rotate_j1_90")
        self.btn_reverse = QtWidgets.QPushButton(Form)
        self.btn_reverse.setGeometry(QtCore.QRect(1330, 530, 174, 42))
        self.btn_reverse.setObjectName("btn_reverse")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Y_label.setText(_translate("Form", "Y"))
        self.Z_label.setText(_translate("Form", "Z"))
        self.Y_output.setText(_translate("Form", "0"))
        self.Z_output.setText(_translate("Form", "0"))
        self.X_label.setText(_translate("Form", "X      "))
        self.R_label.setText(_translate("Form", "R"))
        self.R_output.setText(_translate("Form", "0"))
        self.X_output.setText(_translate("Form", "0                                   "))
        self.btn_new.setText(_translate("Form", "new"))
        self.checkBox.setText(_translate("Form", "校正"))
        self.label_9.setText(_translate("Form", "time/point"))
        self.btn_suck.setText(_translate("Form", "suck"))
        self.btn_free.setText(_translate("Form", "free"))
        self.btn_z_reduce.setText(_translate("Form", "Z-"))
        self.btn_z_increase.setText(_translate("Form", "Z+"))
        self.btn_x_reduce.setText(_translate("Form", "X-"))
        self.btn_y_reduce.setText(_translate("Form", "Y-"))
        self.btn_y_increase.setText(_translate("Form", "Y+"))
        self.btn_x_increase.setText(_translate("Form", "X+"))
        self.btn_set.setText(_translate("Form", "        Set      "))
        self.stream_label.setText(_translate("Form", "TextLabel"))
        self.label_x.setText(_translate("Form", "X"))
        self.label_y.setText(_translate("Form", "Y"))
        self.label_D.setText(_translate("Form", "D"))
        self.btn_save.setText(_translate("Form", "Save Img"))
        self.btn_go.setText(_translate("Form", "GO"))
        self.btn_move.setText(_translate("Form", "Move"))
        self.btn_return.setText(_translate("Form", "return"))
        self.btn_update_loc.setText(_translate("Form", "update"))
        self.btn_rotate_j1_90.setText(_translate("Form", "rotate_j1"))
        self.btn_reverse.setText(_translate("Form", "reverse"))