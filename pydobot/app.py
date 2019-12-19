from pydobot.message import Message
from serial.tools import list_ports
import time
from pydobot import Dobot

port = '/dev/ttyS3'
device = Dobot(port=port, verbose=True)
dist=device.pose()
print("dobot is at "+str(dist))
#dist.x=dist.x+10
#device.move_to(dist[0])
#time.sleep(2)
#dist.x=dist.x-10
#device.move_to(dist)
(x, y, z, r, j1, j2, j3, j4) = device.pose()
#print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
device.move_to(x, y+10, z, r, wait=False)
time.sleep(2)
device.move_to(x, y, z, r, wait=True) 

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
