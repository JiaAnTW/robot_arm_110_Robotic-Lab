# Robot_arm_110_Robotic-Lab
## Developer documents
*   pydobot api:https://hackmd.io/wKYzzFSsQGO85s0LELkB6w
*   tesseract(ocr): https://hackmd.io/4rLx8xwwQqu9ICGh61GGFA?both

# 注意事項
# 載模型
請先到[https://drive.google.com/file/d/1O7gbsR4eAk4lptmVe1Ce9QKZIvf1U2vH/view?usp=sharing](https://drive.google.com/file/d/1O7gbsR4eAk4lptmVe1Ce9QKZIvf1U2vH/view?usp=sharing)

把模型下載下來,放在robot_arm...資料夾底下


去改/複製yolov3.py的內容就好.

## 如果你要取得偵測到的物體資料
請看yolov3.py中的
```
detections = darknet.detect_image(netMain, metaMain, darknet_image, thresh=0.25)
```
這一行會回傳偵測到的內容, 資料格式為
```
[
    (種類名稱, 預測可能性,(長度為4的座標資訊)),
    ('cube', 0.9999891519546509, (2851.58935546875, 1735.2767333984375, 876.068115234375, 816.390380859375))
    （以此類推）......
]
```
只要對資料做以下動作
```
# 取得第i個物體的資料
obj = data[i] 

bounds = obj[2]
yExtent = int(bounds[3])
xEntent = int(bounds[2])
xCoord = int(bounds[0] - bounds[2]/2)
yCoord = int(bounds[1] - bounds[3]/2)
boundingBox = [
    [xCoord, yCoord],
    [xCoord, yCoord + yExtent],
    [xCoord + xEntent, yCoord + yExtent],
    [xCoord + xEntent, yCoord]
]
```
boundingBox就會是圍出該物體所在的方框4點座標
