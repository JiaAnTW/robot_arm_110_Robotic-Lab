from PIL import Image,ImageEnhance
import pytesseract
import numpy as np
import cv2
import pyocr
import pyocr.builders
filepath= "./test_png.png"
img =  cv2.imread('test_png.png', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('My Image', img)

# 按下任意鍵則關閉所有視窗
#cv2.waitKey(0)
#cv2.destroyAllWindows()
builder = pyocr.builders.DigitBuilder()

# Set Page Segmentation mode to Single Char :
builder.tesseract_layout = 10 # If tool = tesseract
image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) #cv2 to Image
image = image.convert('L')# 對比度增強
content = pytesseract.image_to_string(image,lang='eng',config='-psm 7 digits')
print(content)
#image.show()  
 

 