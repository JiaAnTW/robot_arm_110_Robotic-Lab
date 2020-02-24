try:
    from pyzbar.pyzbar import decode
except Exception as e:
    print(e)
    print("請輸入 sudo apt-get install libzbar0")
    print("以及 pip install pyzbar")

def decodePic(img):
    try:
        if type(img)!= str:
            return decode(img)
    except:
        return []

if __name__ == "__main__":
    import cv2
    print(decodePic(cv2.imread("./test.png"))[0].data)