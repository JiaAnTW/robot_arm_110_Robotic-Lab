from socket import *
import threading
import time
##-----------------------定義結束，以下為主程式-----------------------
isFinish=False
msg="no"

def socketCli():
    HOSTc = '127.0.0.1'
    PORTc = 8001
    BUFSIZEc = 1024
    ADDRc = (HOSTc,PORTc)

    try:
        tcpCliSock2 = socket(AF_INET, SOCK_STREAM) 
        tcpCliSock2.connect(ADDRc)
        data='socket connected successfully!'
        tcpCliSock2.send(str("OK").encode())
        data = tcpCliSock2.recv(BUFSIZEc)
        print(data)
        msg=data
        isFinish=True
        tcpCliSock2.close()
        
    except Exception as e:
        print(e)

socketCli()
