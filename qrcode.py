try:
    from pyzbar.pyzbar import decode
except Exception as e:
    print(e)
    print("請輸入 sudo apt-get install libzbar0")
    print("以及 pip install pyzbar")

def decodePic(img):
    return decode(img)