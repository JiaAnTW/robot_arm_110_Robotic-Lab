from ctypes import *
import math
import random
import os
import cv2
import numpy as np
import time
import darknet
#import pyrealsense2 as rs

def convertBack(x, y, w, h,resizeX=1,resizeY=1):
    xmin = int(round(x - (w / 2))*resizeX)
    xmax = int(round(x + (w / 2))*resizeX)
    ymin = int(round(y - (h / 2))*resizeY)
    ymax = int(round(y + (h / 2))*resizeY)
    return xmin, ymin, xmax, ymax


def cvDrawBoxes(detections, img):
    i=0
    for detection in detections:
        x, y, w, h = detection[2][0],\
            detection[2][1],\
            detection[2][2],\
            detection[2][3]
        xmin, ymin, xmax, ymax = convertBack(
            float(x), float(y), float(w), float(h),img.shape[1]/darknet.network_width(netMain),img.shape[0]/darknet.network_height(netMain))
        pt1 = (xmin, ymin)
        pt2 = (xmax, ymax)
        try:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            #cv2.imshow('obj'+str(i), image)
            cv2.rectangle(img, pt1, pt2, (0, 255, 0), 1)
            cv2.putText(img,
                        detection[0].decode() +
                        " [" + str(round(detection[1] * 100, 2)) + "]",
                        (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        [0, 255, 0], 2)
        except Exception as e:
            print(e)
        i+=1
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


netMain = None
metaMain = None
altNames = None


def YOLO():
    #global pipeline, config
    #pipeline = rs.pipeline()
    #config = rs.config()
    #config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
    #pipeline.start(config)

    global metaMain, netMain, altNames
    configPath = "./cfg/yolov3-obj.cfg"
    weightPath = "yolo-obj_last.weights"
    metaPath = "./data/obj.data"
    if not os.path.exists(configPath):
        raise ValueError("Invalid config path `" +
                         os.path.abspath(configPath)+"`")
    if not os.path.exists(weightPath):
        raise ValueError("Invalid weight path `" +
                         os.path.abspath(weightPath)+"`")
    if not os.path.exists(metaPath):
        raise ValueError("Invalid data file path `" +
                         os.path.abspath(metaPath)+"`")
    if netMain is None:
        netMain = darknet.load_net_custom(configPath.encode(
            "ascii"), weightPath.encode("ascii"), 0, 1)  # batch size = 1
    if metaMain is None:
        metaMain = darknet.load_meta(metaPath.encode("ascii"))
    if altNames is None:
        try:
            with open(metaPath) as metaFH:
                metaContents = metaFH.read()
                import re
                match = re.search("names *= *(.*)$", metaContents,
                                  re.IGNORECASE | re.MULTILINE)
                if match:
                    result = match.group(1)
                else:
                    result = None
                try:
                    if os.path.exists(result):
                        with open(result) as namesFH:
                            namesList = namesFH.read().strip().split("\n")
                            altNames = [x.strip() for x in namesList]
                except TypeError:
                    pass
        except Exception:
            pass

    global darknet_image
    darknet_image = darknet.make_image(darknet.network_width(netMain),
                                    darknet.network_height(netMain),3)

def detect_box(color_image):
    prev_time = time.time()
    #color_image=cv2.imread("./yolo.jpg")
    #ret, frame_read = cap.read()
    """frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    #if  not color_frame:
        #continue

    color_image = np.asanyarray(color_frame.get_data())
    img = color_image
    h, w, ch = color_image.shape
    bytesPerLine = ch * w 
    cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR, color_image)"""



    frame_rgb = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb,
                                   (darknet.network_width(netMain),
                                    darknet.network_height(netMain)),
                                   interpolation=cv2.INTER_LINEAR)

    darknet.copy_image_from_bytes(darknet_image,frame_resized.tobytes())
    print("start detect")
    #這一行會回傳偵測到的內容, 資料格式請看readme
    detections = darknet.detect_image(netMain, metaMain, darknet_image, thresh=0.25)
    print("finsh detect")
    print(detections)
    return detections

    for detection in detections:
        x, y, w, h = detection[2][0],\
            detection[2][1],\
            detection[2][2],\
            detection[2][3]
        xmin, ymin, xmax, ymax = convertBack(
            float(x), float(y), float(w), float(h))
        
        resizeImg=[
            color_image.shape[0]/darknet.network_width(netMain),
            color_image.shape[1]/darknet.network_height(netMain)
            ]
        print("["+str(color_image.shape[0])+", "+str(color_image.shape[1])+"]")
        print("["+str(darknet.network_width(netMain))+", "+str(darknet.network_height(netMain))+"]")
        print(str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax))
        print("-----------------------------------------")
        print(str(xmin*resizeImg[0])+","+str(ymin*resizeImg[1])+","+str(xmax*resizeImg[0])+","+str(ymax*resizeImg[1]))


    image = cvDrawBoxes(detections, color_image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(time.time()-prev_time)
    while(True):
        cv2.imshow('Demo', image)
        cv2.waitKey(3)
    #pipeline.stop()

if __name__ == "__main__":
    YOLO()
    
    """frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    color_image = np.asanyarray(color_frame.get_data())
    img = color_image
    h, w, ch = color_image.shape
    bytesPerLine = ch * w 
    cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR, color_image)"""
    color_image=cv2.imread("./0.jpg")
    detect_box(color_image)
