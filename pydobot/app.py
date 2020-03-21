from pydobot.message import Message
from serial.tools import list_ports
import time
from pydobot import Dobot

port = '/dev/ttyS3'
device = Dobot(port=port, verbose=False)
dist=device.pose()
print("dobot is at "+str(dist))
#dist.x=dist.x+10
#device.move_to(dist[0])
#time.sleep(2)
#dist.x=dist.x-10
#device.move_to(dist)
#print(device.pose())
def print_data():
    time.sleep(2)
    (x1, y1, z1, r1, j11, j21, j31, j41) = device.pose()
    print("("+str(x1)+"  ,  "+str(y1)+"  ,  "+str(z1)+"  ,  "+str(j11)+"  ,  "+str(j21)+"  ,  "+str(j31)+"  ,  "+str(j41)+")\n")
    time.sleep(1)


(x, y, z, r, j1, j2, j3, j4) = (260,0,-8,0,0,45,45,0)
#print("("+str(x)+"  ,  "+str(y)+"  ,  "+str(z)+"  ,  "+str(j1)+"  ,  "+str(j2)+"  ,  "+str(j3)+"  ,  "+str(j4)+")\n")

indexArr=[]
i=1
for k in range(3) :
    indexArr.append((x+20*i,y,z,r))
    indexArr.append((x-20*i,y,z,r)) 
    indexArr.append((x,y+20*i,z,r)) 
    indexArr.append((x,y-20*i,z,r)) 
    indexArr.append((x+10*i,y+10*i,z,r)) 
    indexArr.append((x-10*i,y+10*i,z,r)) 
    indexArr.append((x-10*i,y-10*i,z,r))
    i+=0.5



#device.move_to(x, y+40, z, r, wait=True)
#time.sleep(2)
#(x1, y1, z1, r1, j11, j21, j31, j41) = device.pose()
#print("("+str(x1)+"  ,  "+str(y1)+"  ,  "+str(z1)+"  ,  "+str(j11)+"  ,  "+str(j21)+"  ,  "+str(j31)+"  ,  "+str(j41)+")\n")
#time.sleep(6)

#device.move_to(x+40, y+40, z, r, wait=True)
#print_data()     

for index in indexArr:
  device.move_to(index[0], index[1], index[2], index[3], wait=True)
  print_data()

#device.move_to(x+40, y, z+40, r, wait=True)
#print_data()


#device.move_to(x, y, z+40, r, wait=True)
#time.sleep(2)
#(x1, y1, z1, r1, j11, j21, j31, j41) = device.pose()
#print_data()
#print("("+str(x1)+"  ,  "+str(y1)+"  ,  "+str(z1)+"  ,  "+str(j11)+"  ,  "+str(j21)+"  ,  "+str(j31)+"  ,  "+str(j41)+")\n")

#device.move_to(x, y+40, z+40, r, wait=True)
#print_data()
#ime.sleep(2)
#(x1, y1, z1, r1, j11, j21, j31, j41) = device.pose()
#print("("+str(x1)+"  ,  "+str(y1)+"  ,  "+str(z1)+"  ,  "+str(j11)+"  ,  "+str(j21)+"  ,  "+str(j31)+"  ,  "+str(j41)+")\n")

#device.move_to(x+40, y+40, z+40, r, wait=True)
#print_data()
#time.sleep(2)
#(x1, y1, z1, r1, j11, j21, j31, j41) = device.pose()
#print("("+str(x)+"  ,  "+str(y)+"  ,  "+str(z)+"  ,  "+str(j1)+"  ,  "+str(j2)+"  ,  "+str(j3)+"  ,  "+str(j4)+")\n")

device.move_to(x, y, z, r, wait=True) 
print_data()
#time.sleep(2)
#(x1, y1, z1, r1, j11, j21, j31, j41) = device.pose()
#print("("+str(x1)+"  ,  "+str(y1)+"  ,  "+str(z1)+"  ,  "+str(j11)+"  ,  "+str(j21)+"  ,  "+str(j31)+"  ,  "+str(j41)+")\n")

def empty():
        msg = Message()
        msg.id = 62
        msg.ctrl = 0x03
	#dist=msg.pose()
	
        msg.params = bytearray([])
        msg.params.extend(bytearray([0x00]))
        msg.params.extend(bytearray([0x00]))
        return device._send_command(msg)

#empty()
device.close()
