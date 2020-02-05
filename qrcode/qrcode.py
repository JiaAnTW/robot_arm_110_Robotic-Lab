import sys
import qrtools

qr = qrtools.QR()
qr.decode("small.jpg")
print(qr.data)