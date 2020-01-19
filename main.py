#sudo chmod 666 /dev/ttyUSB0
from ui import *
from dialog import *
import sys
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') #解決安裝ROS 造成import opencv 出現error的問題

import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage 
from PyQt5.QtCore import  QObject, QThread, pyqtSignal, Qt

try:
    from pydobot import Dobot
except Exception as e:
    print(e)
import cv2
import pyrealsense2 as rs
import numpy as np

class MySignal(QObject):  # global signal 
    sig = QtCore.pyqtSignal()


signal = MySignal()
class correct_Thread(QThread):
    def run(self):
        
        self.correct()

    def set_device(self,device):
        self.device = device
    def save_img(self):
        global signal
        signal.sig.emit()    
    def correct(self):
        (x, y, z, r, j1, j2, j3, j4) = (260,0,60,0,0,45,45,0)
        pos=[]
        def print_data():
            time.sleep(2)
            (x1, y1, z1, r1, j11, j21, j31, j41) = self.device.pose()
            self.save_img()
            pos.append((x1, y1, z1, r1, j11, j21, j31, j41))
            print("("+str(x1)+"  ,  "+str(y1)+"  ,  "+str(z1)+"  ,  "+str(j11)+"  ,  "+str(j21)+"  ,  "+str(j31)+"  ,  "+str(j41)+")\n")
            time.sleep(1)

        indexArr=[]
        i=1.2
        for k in range(2) :
            indexArr.append((x+15*i,y,z,r))
            indexArr.append((x-10*i,y,z,r))
            indexArr.append((x+10*i,y-15*i,z+15*i,r))
            indexArr.append((x,y+20*i,z,r))
            indexArr.append((x,y-20*i,z,r))
            indexArr.append((x+10*i,y+15*i,z+15*i,r))
            indexArr.append((x-15*i,y+20*i,z+15*i,r))
            indexArr.append((x-15*i,y-10*i,z+15*i,r))
            i+=1

        for index in indexArr:
            self.device.move_to(index[0], index[1], index[2], index[3], wait=True)
            print_data()

        self.device.move_to(x, y,z, r, wait=True)
        print_data()
        
        with open('pos.txt', 'w') as f:
            for item in pos:
                f.write(str(item))
                f.write("\n")

        self.device.move_to(x, y, z, r, wait=True)
        time.sleep(1)    
        


class Thread(QThread):
    changePixmap = pyqtSignal(QtGui.QImage)
    

    def run(self):
        global signal
        self.i = 0
        signal.sig.connect(self.save_img)

        self.pipeline = rs.pipeline()
        self.config = rs.config()
        #config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)

        self.pipeline.start(self.config)
        
        while True:
            frames = self.pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if  not color_frame:
                continue

            self.color_image = np.asanyarray(color_frame.get_data())
            self.img = self.color_image
            h, w, ch = self.color_image.shape
            bytesPerLine = ch * w
           
            
            cv2.cvtColor(self.color_image, cv2.COLOR_RGB2BGR, self.color_image)
            
            #cv2.COLOR_RGB2BGR
                
            convertToQtFormat = QtGui.QImage(self.color_image.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            p = convertToQtFormat.scaled(1280, 720, Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
        
    def save_img(self):
        cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR, self.img)
        cv2.imwrite(str(self.i)+'.jpg', self.img)
        self.i +=1
        print("save: "+str(self.i)+"\n")

    def stop(self):
        self.pipeline.stop()
        self.quit()

class MyPopup(QDialog, Ui_dialog):

    def __init__(self, parent=None):
        super(MyPopup, self).__init__(parent)
        self.setupUi(self)
        self.label.resize(1280,720)
        self.label.move(0,0)

        self.btn_save.clicked.connect(self.save_img)
        self.show()
        
    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        if x <= 1280 and y <= 720:
            #print (x,y)
            self.label_X.setText(str(x))
            self.label_Y.setText(str(y))
            self.update()


    def save_img(self):
        global signal
        signal.sig.emit()
        
        
    @QtCore.pyqtSlot(QtGui.QImage) 
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
        self.update()


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

        self.btn_stop.clicked.connect(self.run_thread)

        self.streampopup = MyPopup()
        self.streampopup.show()
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint)

        self.th = Thread(self)
        self.th.changePixmap.connect(self.streampopup.setImage)
        self.th.start()

        
        for x in range(3):
            self.gridLayout_2.setColumnStretch(x, x+1)
    def closeEvent(self, event):
        self.th.stop()

    def save_img(self):
        global signal
        signal.sig.emit()
        
    def run_thread(self):
        t = correct_Thread(self)
        t.set_device(self.device)
        t.start()
    
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
            print(tmp)
            (x, y, z, r) =tmp
            print(content)
            self.user_set_pos[self.comboBox.count()-1]=(float(content),y,z,r)
        except Exception as e:
            print("輸入格式錯誤")
            print(e)
    
    def set_y(self,content):
        try:
            tmp=self.user_set_pos[self.comboBox.count()-1]
            (x, y, z, r) =tmp
            self.user_set_pos[self.comboBox.count()-1]=(x,float(content),z,r)
        except Exception as e:
            print("輸入格式錯誤")
            print(e)

    def set_z(self,content):
        try:
            tmp=self.user_set_pos[self.comboBox.count()-1]
            (x, y, z, r) =tmp
            self.user_set_pos[self.comboBox.count()-1]=(x,y,float(content),r)
        except Exception as e:
            print("輸入格式錯誤")
            print(e)

    def set_r(self,content):
        try:
            tmp=self.user_set_pos[self.comboBox.count()-1]
            (x, y, z, r) =tmp
            self.user_set_pos[self.comboBox.count()-1]=(x,y,z,float(content))
        except Exception as e:
            print("輸入格式錯誤")
            print(e)

    def get_pos(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            (x,y,z,r,j1,j2,j3,j4)=self.device.pose()
            self.user_set_pos[0]=(x,y,z,r)
        except Exception as e:
            self.user_set_pos[0]=(0,0,0,0)

        pos=self.user_set_pos[0]
        self.label_1.setText(_translate("Form", str(round(pos[0],5))))
        self.lineEdit_1.setText(_translate("Form", str(round(pos[0],5))))

        self.label_5.setText(_translate("Form", str(round(pos[1],5))))
        self.lineEdit_2.setText(_translate("Form", str(round(pos[1],5))))

        self.label_6.setText(_translate("Form", str(round(pos[2],5))))
        self.lineEdit_3.setText(_translate("Form", str(round(pos[2],5))))

        self.label_7.setText(_translate("Form", str(round(pos[3],5))))
        self.lineEdit_4.setText(_translate("Form", str(round(pos[3],5))))

    def action(self):
        test=[]
        for i in range(self.comboBox.count()):
            print(str(self.user_set_pos[i]))
            (x, y, z, r) =self.user_set_pos[i]
            
            try: #call  pydobot
                self.device.move_to(x, y, z, r, wait=True)
                time.sleep(self.waitTime)
                self.get_pos()
                test.append(self.device.pose())
                

            except Exception as e:
                print("輸入格式錯誤")
                print("錯誤訊息： "+str(e))
        with open('pos.txt', 'w') as f:
            for item in test:
                f.write(str(item))
                f.write("\n")
    
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
    #w = MyPopup()
    w.show()
    sys.exit(app.exec_())
