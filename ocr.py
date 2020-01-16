import pytesseract
from PIL import Image

import pyocr
import pyocr.builders

import numpy as np 
import cv2 
import numpy as np 
import matplotlib.pyplot as plt
img = cv2.imread('./ocr_data/152.jpg')
print(img.shape)
img=img[600:1477,0:1100]
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

thresh2=thresh2[min(editBoxY):max(editBoxY),min(editBoxX):max(editBoxX)]
image = Image.fromarray(thresh2)
image.show() 

content = pytesseract.image_to_string(image,lang='eng',config='--psm 13')
print(content)

print("done")
cv2.waitKey(0)