import pytesseract
from PIL import Image

import pyocr
import pyocr.builders

import numpy as np 
import cv2 
import numpy as np 
import matplotlib.pyplot as plt

def ocr():
    img = cv2.imread('./ocr_data/167.jpg')
    print(img.shape)
    #img=img[600:1477,0:1100]
    img1 = np.float32(img)

    # k-means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness,labels,centers = cv2.kmeans(img1,2,None,criteria,10,flags)
    img1= center = np.uint8(centers)
    res = center[labels.flatten()]
    res2 = res.reshape((img.shape))
    cv2.imshow('Corner',res2)

    def contrast_brightness_image(src1, a, g):
        h, w, ch = src1.shape
        src2 = np.zeros([h, w, ch], src1.dtype)
        dst = cv2.addWeighted(src1, a, src2, 1-a, g)
        return dst

    """(h, w) = img.shape[:2] #10
    center = (w // 2, h // 2) #11
 
    M = cv2.getRotationMatrix2D(center, -60, 1.0) #12
    rotated = cv2.warpAffine(img, M, (w, h)) #13
    img = rotated"""
 
    gray = cv2.cvtColor(res2,cv2.COLOR_BGR2GRAY) 
    ret,thresh1=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    gray2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    ret,thresh2=cv2.threshold(gray2,127,255,cv2.THRESH_BINARY)
    gray = np.float32(thresh1) 
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) 
    corners = np.int0(corners)


    # corner
    editBoxX=[]
    editBoxY=[]
    for corner in corners:
        x,y = corner.ravel()
        editBoxX.append(x)
        editBoxY.append(y) 
        print("dot "+str(x)+" "+str(y)) 
        #cv2.circle(img,(x,y),3,255,-1)
        cv2.circle(res2,(x,y),3,255,-1)
    cv2.imshow('Corner',res2)
    targetBox=[]

    for i in range(len(editBoxX)):
        for j in range(i+1,len(editBoxX)):
            addBox={}
            for k in range(j+1,len(editBoxX)):
                directA={"x":editBoxX[i]-editBoxX[j],"y":editBoxY[i]-editBoxY[j]}
                directB={"x":editBoxX[i]-editBoxX[k],"y":editBoxY[i]-editBoxY[k]}
                innerProduct=directA["x"]*directB["x"]+directA["y"]*directB["y"]
                lengthA=pow(directA["x"],2)+pow(directA["y"],2)
                lengthB=pow(directB["x"],2)+pow(directB["y"],2)
                if (innerProduct<lengthA*lengthB*0.034 and innerProduct>lengthA*lengthB*0.034*-1) and (lengthA/lengthB<1.3 and lengthA/lengthB>0.97):
                    addBox={
                        "x_max": max([editBoxX[i],editBoxX[j],editBoxX[k]]),
                        "x_min": min([editBoxX[i],editBoxX[j],editBoxX[k]]),
                        "y_max": max([editBoxY[i],editBoxY[j],editBoxY[k]]),
                        "y_min": min([editBoxY[i],editBoxY[j],editBoxY[k]]),
                    }
                    try:
                        targetBox.index(addBox)
                        break
                    except:
                        targetBox.append(addBox)
                        break
            if addBox!={}:
                break

    print(targetBox)

    #cv2.imshow('Corner',res2)
    result=[]
    for target in targetBox:
        adjSizeX=int((target["x_max"]-target["x_min"])*0.025)
        adjSizeY=int((target["x_max"]-target["x_min"])*0.025)
        image=thresh2[target["y_min"]+adjSizeY:target["y_max"]-adjSizeY,target["x_min"]+adjSizeX:target["x_max"]-adjSizeX]
        image = Image.fromarray(image)
        content = pytesseract.image_to_string(image,lang='eng',config='--psm 13')
        if content!="":
            result.append({"num":content,"pos":[(target["x_max"]+target["x_min"])/2,(target["y_max"]+target["y_min"])/2]})
            print(content)
            #image.show()
    return result
    """adjSize=int((max(editBoxY)-min(editBoxY))*0.05)

    image1=thresh2[min(editBoxY)+adjSize:max(editBoxY)-adjSize,editBoxX[7]+adjSize:editBoxX[6]-adjSize]
    image1 = Image.fromarray(image1)
    image1.show() 

    image2=thresh2[min(editBoxY)+adjSize:max(editBoxY)-adjSize,editBoxX[5]+adjSize:editBoxX[4]-adjSize]
    image2 = Image.fromarray(image2)
    image2.show() 

    content = pytesseract.image_to_string(image1,lang='eng',config='--psm 13')
    print(content)

    content = pytesseract.image_to_string(image2,lang='eng',config='--psm 13')
    print(content)"""

    print("done")

print(ocr())
cv2.waitKey(0)