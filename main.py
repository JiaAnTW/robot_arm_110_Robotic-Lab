#sudo chmod 666 /dev/ttyUSB0
from ui import *
from dialog import *
import sys
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') #解決安裝ROS 造成import opencv 出現error的問題
from socket import *
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout,QButtonGroup
from PyQt5.QtGui import QPixmap, QImage 
from PyQt5.QtCore import  QObject, QThread, pyqtSignal, Qt, QMutex
import darknet
import qrcode
import yolov3

try:
    from pydobot import Dobot
except Exception as e:
    print(e)
import cv2
import pyrealsense2 as rs
import numpy as np

#img_mutex,det_mutex,detection_result,detection_img,is_detect,is_Finish
is_Finish=True
is_detect=False
detection_img=None 
img_mutex=QMutex()
det_mutex=QMutex() 
detection_result=None 


class MySignal(QObject):  # global signal 
    sig = QtCore.pyqtSignal()


signal = MySignal()




class yolo_Thread(QThread):
    addNewObj= pyqtSignal(list)
    def run(self):
        self.is_Finish=True
        self.i=0
        self.is_img=False
        self.is_detect=False
        self.is_always_detect=False
        self.detection_img=None 
        self.fin_mutex=QMutex()
        self.img_mutex=QMutex()
        self.det_mutex=QMutex() 
        self.detection_result=None
        yolov3.YOLO()
        threading.Thread(target = self.initSocket())
        while True:
            try:
                if self.is_img==True :
                    #print("let's detect!")
                    #detections=yolov3.detect_box(self.detection_img)
                    if self.is_always_detect==True:
                        try:
                            cv2.imwrite("target.jpg", self.detection_img)
                            self.i=1
                            detections=self.sendData()
                        except Exception as e:
                            print("沒有連接到socket,將無法開啟即時偵測功能")
                            self.is_always_detect=False
                            print(e)
                    elif self.is_detect==True:
                        detections=yolov3.detect_box(self.detection_img)
                    self.img_mutex.lock()
                    self.is_Finish=True
                    self.is_img=False
                    self.addNewObj.emit([detections,self.detection_img])
                    self.img_mutex.unlock()
                    self.detection_img=None
                    self.detection_result=detections
                    #print("done")
                    
            except Exception as e:
                print("stop during thread pool")
                print(e)
    
    def initSocket(self):
        HOST=''
        PORT = 8888
        ADDR = (HOST,PORT)
        self.tcpSerSock = socket(AF_INET, SOCK_STREAM)  
        self.tcpSerSock.bind(ADDR)
        self.tcpSerSock.listen()
        print('wating for connection...')
        self.tcpCliSock,self.addr = self.tcpSerSock.accept()

        print( '...connected from:',self.addr)
        BUFSIZE = 1024
        data = self.tcpCliSock.recv(BUFSIZE)
        #print (data)
        #self.tcpSerSock.setblocking(False)
        #self.tcpCliSock.setblocking(False)
        
    
    def sendData(self):
        try:
            if (self.is_Finish==False):
                import os
                os.system("cp target.jpg /media/sf_winLinux/project")
                data="test"
                BUFSIZE = 1024
                self.tcpCliSock.send(data.encode())
                #print("here")
                #time.sleep(1.5)
                data = self.tcpCliSock.recv(BUFSIZE)
                data=str(data)
                #print ("123") 
                return self.handleString(data)
        except Exception as e:
            print("error during send and recv socket")
            print(e)
            return []

    def handleString(self,obj):
        try:
            strArr=obj.split("'")
            #print(obj)
            name=strArr[1]
            strArr[2]=strArr[2].replace("(", "")
            strArr[2]=strArr[2].replace(")", "")
            strArr[2]=strArr[2].replace("]", "")
            strArr[2]=strArr[2].replace("\"", "")
            strArr[2]=strArr[2].split(",")
            strArr[2].pop(0)
            for items in strArr[2]:
                items=float(items)
            data=[(name,float(strArr[2][0]),
            (float(strArr[2][1]),float(strArr[2][2]),float(strArr[2][3]),float(strArr[2][4])))]
            return data
        except Exception as e:
            print("error handle string from socket")
            print("data is "+obj)
            print(e)
            return []            

    def _del_(self):      
        self.tcpCliSock.close() 


class Thread(QThread):
    changePixmap = pyqtSignal(QtGui.QImage)
    addNewObj= pyqtSignal(list,list)

    def run(self):
        global signal
        self.i = 0
        signal.sig.connect(self.save_img)
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.beforeResult=[]
        #config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
        self.pipeline.start(self.config)
        detection_result=None
        is_Finish=True
        self.yolo_t=yolo_Thread()
        self.yolo_t.start()
        self.yolo_t.addNewObj.connect(self.obj_thread)

        while True:
            frames = self.pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if  not color_frame:
                continue
            #print("1")
            self.color_image = np.asanyarray(color_frame.get_data())
            self.img = self.color_image
            h, w, ch = self.color_image.shape
            bytesPerLine = ch * w
           
            #print("2")
            cv2.cvtColor(self.color_image, cv2.COLOR_RGB2BGR, self.color_image)
            #cv2.COLOR_RGB2BGR
            #print("is detect is "+str(self.yolo_t.is_detect)+", img is "+str(self.yolo_t.is_Finish))
            if (self.yolo_t.is_detect==True or self.yolo_t.is_always_detect==True) and self.yolo_t.is_Finish==True:
                self.yolo_t.img_mutex.lock()
                #print("koko")
                self.yolo_t.is_img=True
                self.yolo_t.is_detect=False
                self.yolo_t.detection_img=self.color_image
                self.yolo_t.img_mutex.unlock()
                self.yolo_t.fin_mutex.lock()
                self.yolo_t.is_Finish=False
                self.yolo_t.fin_mutex.unlock()
            #print("3")
            if self.yolo_t.detection_result!=None:
                try:
                    #print("123456")
                    self.yolo_t.det_mutex.lock()
                    #print(str(self.yolo_t.detection_result))
                    self.color_image = yolov3.cvDrawBoxes(self.yolo_t.detection_result, self.color_image)
                    #print("yyoyoyo!")
                    self.yolo_t.is_detect=False
                    self.yolo_t.det_mutex.unlock()
                    #self.color_image = cv2.cvtColor(self.color_image, cv2.COLOR_BGR2RGB)
                    #print("Finish all")
                except Exception as e:
                    print("eee")
                    print(e)
            #print("4")
            try:    
                convertToQtFormat = QtGui.QImage(self.color_image.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                p = convertToQtFormat.scaled(1280, 720, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
            except Exception as e:
                print("stop after detect")
                print(e)


        
    def save_img(self):
        cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR, self.img)
        cv2.imwrite(str(self.i)+'.jpg', self.img)
        self.i +=1
        print("save: "+str(self.i)+"\n")

    def stop(self):
        self.pipeline.stop()
        self.quit()

    def setFinish(self):
        self.yolo_t.is_detect=True
    
    def setAlwaysDetect(self):
        if self.yolo_t.is_always_detect==True:
            self.yolo_t.is_always_detect=False
        else:
            self.yolo_t.is_always_detect=True

    def obj_thread(self, data):
        th=threading.Thread(target = self.updateObj, args = (data[0], data[1]))
        th.start()

    def updateObj(self,detection,img):
        name=[]
        pos=[]
        if detection ==[]:
            time.sleep(2)
            self.beforeResult=detection
            self.addNewObj.emit(name,pos)
            return
        if detection!=None and self.beforeResult!=detection:
            for item in detection:
                try:
                    x, y, w, h = item[2][0],\
                    item[2][1],\
                    item[2][2],\
                    item[2][3]
                    xmin, ymin, xmax, ymax = yolov3.convertBack(
                    float(x), float(y), float(w), float(h),img.shape[1]/darknet.network_width(yolov3.netMain),img.shape[0]/darknet.network_height(yolov3.netMain))
                    image=img[ymin:ymax,xmin:xmax]
                    pos.append([int((xmin+xmax)/2),int((ymin+ymax)/2)])
                    name.append(qrcode.decodePic(image)[0].data.decode())
                    #print("item is "+str(name[len(name)-1]))
                except Exception as e:
                    name.append("不明物")
            self.beforeResult=detection
            self.addNewObj.emit(name,pos)
            
                
class MyPopup(QDialog, Ui_dialog):

    def __init__(self, parent=None,dobot=None):
        super(MyPopup, self).__init__(parent)
        self.setupUi(self)
        self.btn_grp = QButtonGroup(self)
        self.btn_grp.setExclusive(True)
        
        self.btn_detect.clicked.connect(dobot.single_detect)
        self.btn_always_detect.clicked.connect(dobot.always_detect)

        self.btn_grp.buttonClicked[int].connect(dobot.get_items)
        self.objArr=[]
        self.show()
    
    def add_obj(self,name,objList):
        _translate = QtCore.QCoreApplication.translate
        for obj in self.objArr:
            for items in obj:
                del items
        self.objArr=[]
        j=0
        for obj in objList:
            self.objArr.append([
                    QtWidgets.QLabel(self.objInfoWidget),
                    QtWidgets.QLabel(self.objInfoWidget),
                    QtWidgets.QPushButton(self.objInfoWidget),
                ])
            for i in range(3):
                self.objLayout.addWidget(self.objArr[j][i], 2+j, i, 1, 1)
            self.objArr[j][0].setText(_translate("Form", str(name[j])))
            self.objArr[j][1].setText(_translate("Form", str(obj[2])))
            self.objArr[j][2].setText(_translate("Form", "抓取"))
            j+=1
        


class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.x = 640.0
        self.y = 360.0
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


    def always_detect(self):
        self.th.setAlwaysDetect()

    #compute (u,v) to real world corrdinate space
    def trans(self):
        #u = 797
        #v = 419.0

        (x,y,z) = self.get_pos()
        print(x)
        print(y)
        print(z)
        
        u = self.x 
        v = self.y 

        X = np.array([[u, v, 1.0]]).reshape(1,3)

        M = np.array([[ 3.07210472e-03,-3.68102103e-01, 0.00000000e+00],
                    [-3.74686041e-01, -6.87139754e-03, -2.16840434e-18],
                    [ 4.06011267e+02,  2.64299383e+02,  1.00000000e+00] ])
        
        result = X.dot(M)
        #print(result)
        #we use fixed depth for now
        self.device.move_to(result[0][0],result[0][1],-100.0, 0.0 , wait = True) 


    def _init_ui_connect(self):
        _translate = QtCore.QCoreApplication.translate
        self.btn_new.clicked.connect(self._set_user_set_pos)   #get data

        self.btn_move.clicked.connect(self.action)
        self.btn_go.clicked.connect(self.trans)


        self.comboBox.insertItem(0,"點1")
        self.lineEdit.textEdited.connect(self.set_time)
        self.X_edit.textEdited.connect(self.set_x)
        self.Y_edit.textEdited.connect(self.set_y)
        self.Z_edit.textEdited.connect(self.set_z)
        self.R_edit.textEdited.connect(self.set_r)
        self.comboBox.currentIndexChanged.connect(self.switch_point)
        
        self.lineEdit.setText(_translate("Form", str(2)))


        self.streampopup = MyPopup(dobot=self)
        self.streampopup.show()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        

        
        #self.btn_detect.clicked.connect(self.single_detect)

        #button.clicked.connect(lambda: calluser(name))
        self.interval = 1
        self.input_interval.textEdited.connect(self.set_inputinterval)
        self.btn_x_increase.clicked.connect(lambda: self.move_xyz(self.interval, 0, 0))
        self.btn_x_reduce.clicked.connect(lambda: self.move_xyz(-self.interval, 0, 0))
        self.btn_y_increase.clicked.connect(lambda: self.move_xyz(0, self.interval, 0))
        self.btn_y_reduce.clicked.connect(lambda: self.move_xyz(0, -self.interval, 0))
        self.btn_z_increase.clicked.connect(lambda: self.move_xyz(0, 0, self.interval))
        self.btn_z_reduce.clicked.connect(lambda: self.move_xyz(0, 0, -self.interval))

        self.btn_return.clicked.connect(self.return_ori)



        self.th = Thread(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.addNewObj.connect(self.add_obj)
        self.th.start()
        
        
        self.stream_label.resize(1280,720)
        self.stream_label.move(0,0)

        self.btn_save.clicked.connect(self.save_img)


        
        self.btn_suck.clicked.connect(self.run_suck)
        self.btn_free.clicked.connect(self.free)

    def add_obj(self,name,objList):
        self.streampopup.add_obj(name,objList)

    def get_items(self,idi):
        
        btn_id=idi
        print("id is "+str(btn_id))
        print("click "+str(btn_id))
        x=self.nowItem[btn_id]["pos"][0]
        y=self.nowItem[btn_id]["pos"][1]
        print("go to "+str(x)+" "+str(y))

        ##在這裡做座標轉換
        y1=float(-55*x/228+204.1228)
        x1=float(-5*y/19+414.4737)
        ##在上面做座標轉換

        self.device.move_to(x1, y1, -20, 0, wait=True)
        self.run_suck()
        time.sleep(1)
        self.device.move_to(260, 0, 100, 0, wait=True)
        self.free


    def run_suck(self):
        self.device.grip(True)
        
    def free(self):
        #self.device.grip(False)
        self.device.suck(False) 
        


    # go to initinal position
    def return_ori(self):
        (x, y, z) = self.get_pos()   
        self.device.move_to(211.9, y, z, 0.0) 

        self.device.move_to(211.9, 1.1, z, 0.0) 

        self.device.move_to(211.9, 1.1, 172.64, 0.0) 
        self.get_pos()
        #211.9810 1.1234 172.8245 0.3037


        
    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        # get depth 
        self.th.get_depth(self.x, self.y)

        if self.x <= 1280 and self.y <= 720:
            #print (x,y)
            self.label_X.setText(str(self.x))
            self.label_Y.setText(str(self.y))
            self.update()


    def save_img(self):
        global signal
        signal.sig.emit()
        
        
    @QtCore.pyqtSlot(QtGui.QImage) 
    def setImage(self, image):
        self.stream_label.setPixmap(QPixmap.fromImage(image))
        self.update()

    def set_inputinterval(self, content):
        
        self.interval = float(content)
      
    def closeEvent(self, event):
        self.th.stop()
        self.streampopup.quit()


    def single_detect(self):
        self.th.setFinish()

    def save_img(self):
        global signal
        signal.sig.emit()
        
    
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
            self.user_set_pos[self.comboBox.count()-1]=(float(content),y,z,r)
            print(content)
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
            (x, y, z, r, j1, j2, j3, j4)=self.device.pose()
            self.user_set_pos[0]=(x,y,z,r)
        except Exception as e:
            (x,y,z)=(0,0,0)
            self.user_set_pos[0]=(0,0,0,0)

        pos=self.user_set_pos[0]
        self.X_output.setText(_translate("Form", str(round(pos[0],5))))
        self.X_edit.setText(_translate("Form", str(round(pos[0],5))))

        self.Y_output.setText(_translate("Form", str(round(pos[1],5))))
        self.Y_edit.setText(_translate("Form", str(round(pos[1],5))))

        self.Z_output.setText(_translate("Form", str(round(pos[2],5))))
        self.Z_edit.setText(_translate("Form", str(round(pos[2],5))))

        self.R_output.setText(_translate("Form", str(round(pos[3],5))))
        self.R_edit.setText(_translate("Form", str(round(pos[3],5))))
        return (x,y,z)

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

    def move_xyz(self, x_, y_, z_):
        (x,y,z) = self.get_pos()   
        self.device.move_to(x+ x_, y +y_, z+z_, 0.0 , wait= True) 

    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
