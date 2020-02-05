# 注意事項
# 載模型
請先到[https://drive.google.com/open?id=1O7gbsR4eAk4lptmVe1Ce9QKZIvf1U2vH](https://drive.google.com/open?id=1O7gbsR4eAk4lptmVe1Ce9QKZIvf1U2vH)

把模型下載下來,放在yolov3資料夾底下


去改/複製darknet_video.py的內容就好.

## 如果你要改成在外面那層資料夾的code寫darknet_video.py的內容

要把
```
import darknet
```
改成
```
import yolov3.darknet
```

## 如果你要取得偵測到的物體資料
請看darknet_video.py中的
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
