from socket import *
import yolov3
import cv2
##-----------------------定義結束，以下為主程式-----------------------

HOST = '127.0.0.1'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM) 
tcpCliSock.connect(ADDR)
data='socket connected successfully!'
tcpCliSock.send(data.encode())
# 初始化Yolo
yolov3.YOLO()


while True:
    data = tcpCliSock.recv(BUFSIZE)
    print( data)
    if data=='exit':
        break
    if data=="":
        continue
    img=cv2.imread("0.jpg")
    data=yolov3.detect_box(cv2.imread("./target.jpg"))
    tcpCliSock.send(str(data).encode())
tcpCliSock.close()