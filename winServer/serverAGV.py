from socket import *
import threading
import time
##-----------------------定義結束，以下為主程式-----------------------
isFinish=False
msg="no"
tcpCliSock=None
HOST = '127.0.0.1'
#HOST = '192.168.31.183'
PORT = 8001
BUFSIZE = 1024
ADDR = (HOST,PORT)

def socketCli():
    HOSTc = '127.0.0.1'
    PORTc = 8000
    BUFSIZEc = 1024
    ADDRc = (HOSTc,PORTc)

    try:
        tcpCliSock2 = socket(AF_INET, SOCK_STREAM) 
        tcpCliSock2.connect(ADDRc)
        data='socket connected successfully!'
        tcpCliSock2.send(str("OK").encode())
        data = tcpCliSock2.recv(BUFSIZEc)
        print("get "+str(data))
        tcpCliSock2.close()
        msg=data
        time.sleep(3)
        tcpCliSock.send(msg)
        print("send "+str(msg))
        isFinish=False
        tcpCliSock.close()
        isFinish=True
        
        
    except Exception as e:
        print(e)



try:
    tcpSerSock = socket(AF_INET, SOCK_STREAM)  
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen()
    print('wating for AGV connection...')
    while(True):
        tcpCliSock,addr = tcpSerSock.accept()
        print( '...connected from:',addr)
        data = tcpCliSock.recv(BUFSIZE)
        time.sleep(3)
        socketCli()
        tcpCliSock.close()
except Exception as e:
    tcpSerSock.close()
    print(e)


