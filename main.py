from ui import *
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
try:
    from pydobot import Dobot
except Exception as e:
    print(e)


class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.onBindingUi()
        self.user_set_pos=[(0,0,0,0)]
        print("開始自動尋找dobot所在的port\n")
        self._connect_dobot(0)
        self._init_ui_connect()
        self.get_pos()
        self.waitTime=2
    
    def _connect_dobot(self,i):
        try:
            portArray=["/dev/ttyUSB0","/dev/ttyUSB01","/dev/ttyUSB2","/dev/ttyUSB3","/dev/ttyUSB4","/dev/ttyUSB5","/dev/ttyS0","/dev/ttyS1","/dev/ttyS2","/dev/ttyS3","/dev/ttyS4","/dev/ttyS5"]
            self.device=Dobot(port=portArray[i],verbose=False)
            print("連接成功")
        except Exception as e:
            print("無法在"+portArray[i]+"連接Dobot\n原因:"+str(e))
	
            if(i<len(portArray)-1):
                print("沒關係的別驚慌,我會嘗試連接下一個port\n")
                self._connect_dobot(i+1)
            else:
                print("連接失敗，請檢查是否有將dobot接上USB")

    def _init_ui_connect(self):
        _translate = QtCore.QCoreApplication.translate
        self.btn_go.clicked.connect(self._set_user_set_pos)   #get data
        self.btn_reset.clicked.connect(self.action)
        self.comboBox.insertItem(0,"點1")
        self.lineEdit.textEdited.connect(self.set_time)
        self.lineEdit_1.textEdited.connect(self.set_x)
        self.lineEdit_2.textEdited.connect(self.set_y)
        self.lineEdit_3.textEdited.connect(self.set_z)
        self.lineEdit_4.textEdited.connect(self.set_r)
        self.comboBox.currentIndexChanged.connect(self.switch_point)
        self.lineEdit.setText(_translate("Form", str(2)))
    
    def switch_point(self,index):
        try:
            _translate = QtCore.QCoreApplication.translate
            self.lineEdit_1.setText(_translate("Form", str(self.user_set_pos[index][0])))
            self.lineEdit_2.setText(_translate("Form", str(self.user_set_pos[index][1])))
            self.lineEdit_3.setText(_translate("Form", str(self.user_set_pos[index][2])))
            self.lineEdit_4.setText(_translate("Form", str(self.user_set_pos[index][3])))
        except Exception as e:
            print(e)

    def set_time(self,content):
        try:
            self.waitTime=float(content)
        except Exception as e:
            print("輸入格式錯誤")
            print(e)



    def set_x(self,content):
        try:
            tmp=self.user_set_pos[self.comboBox.count()-1]
            self.user_set_pos[self.comboBox.count()-1]=(float(content),tmp[1],tmp[2],tmp[3])
        except Exception as e:
            print("輸入格式錯誤")
            print(e)
    
    def set_y(self,content):
        try:
            self.user_set_pos[self.comboBox.count()]=(tmp[0],float(content),tmp[2],tmp[3])
        except Exception as e:
            print("輸入格式錯誤")

    def set_z(self,content):
        try:
            self.user_set_pos[self.comboBox.count()]=(tmp[0],tmp[1],float(content),tmp[3])
        except Exception as e:
            print("輸入格式錯誤")

    def set_r(self,content):
        try:
            self.user_set_pos[self.comboBox.count()]=(tmp[0],tmp[1],tmp[2],float(content))
        except Exception as e:
            print("輸入格式錯誤")

    def get_pos(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            pos=self.device.pose()
            self.user_set_pos[0]=pos
            print(pos)
        except Exception as e:
            pos=(0,0,0,0)

        self.label_1.setText(_translate("Form", str(round(pos[0],5))))
        self.lineEdit_1.setText(_translate("Form", str(round(pos[0],5))))

        self.label_5.setText(_translate("Form", str(round(pos[1],5))))
        self.lineEdit_2.setText(_translate("Form", str(round(pos[1],5))))

        self.label_6.setText(_translate("Form", str(round(pos[2],5))))
        self.lineEdit_3.setText(_translate("Form", str(round(pos[2],5))))

        self.label_7.setText(_translate("Form", str(round(pos[3],5))))
        self.lineEdit_4.setText(_translate("Form", str(round(pos[3],5))))

    def action(self):
        for i in range(self.comboBox.count()):
            (x, y, z, r) =self.user_set_pos[i]
            print(str(x))
            try: #call  pydobot
                self.device.move_to(x, y, z, r, wait=True)
                time.sleep(self.waitTime)
                self.get_pos()

            except Exception as e:
                print("輸入格式錯誤")
                print("錯誤訊息： "+str(e))
    
    def _set_user_set_pos(self): 
        try:
            self.comboBox.addItem("點"+str(self.comboBox.count()+1))
            self.user_set_pos.append((0,0,0,0))
            print(str(self.user_set_pos))
        except Exception as e:
            print("輸入格式錯誤")
            print("錯誤訊息： "+str(e))  
    
    def onBindingUi(self):
        pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
