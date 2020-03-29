# Dlib 人臉識別
dlib 使用的是ResNet(深度殘差網路)
模型檔下載：https://drive.google.com/drive/folders/1cfzZ9bjWHDXK_-O_BgpF0_YDd-7e_SZF?usp=sharing
>Dlib 人臉偵測演算法使用方向梯度直方圖(HOG)的特徵, 加上線性分類器(linear classifier)、影像金字塔(image pyramid)與滑動窗格(sliding window)計算出來. 演算的結果會有一個分數, 此分數愈大, 表示愈接近人臉. 分數愈低表示愈接近誤判. 調用detector.run()即可取得分數

why dlib HoG? 
* pros:在CPU上運行速度快,與opencv模型相比較小
* cons:
       1.不能檢測小臉，因為它訓練資料的最小人臉尺寸為80×80，但是使用者可以用較小尺寸的人臉資料自己訓練檢測器
       2.只能辨別正臉,除非再自己做face_alignment
## face_detect.py 
* 需要事先安裝dlib套件
登入人臉和身份以作為之後人臉辨識的資料庫,當辨識到人臉時可以選擇按'n'或's',或是直接把照片放入資料夾內
* 待解決的問題：需要大臉偵測（自拍照類型） out of range 的問題？？
## facedata_to_csv.py
* 需要下載shape_predictor_68_face_landmarks.dat檔案(人臉特徵點標示模型已經訓練好了)
計算資料庫內人像特徵值,並除存為csv檔,方便之後程式提取資料
## face_reco_from_camera.py
* 需要下載dlib_face_recognition_resnet_model_v1.dat檔案（藉由csv檔辨識人臉）
讀取csv檔案的特徵值再比對待辨識的人臉,誤差值最小者變判定其為資料庫的哪一個人

