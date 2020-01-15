import sys
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') #解決安裝ROS 造成import opencv 出現error的問題

import pyrealsense2 as rs
import numpy as np
import cv2
 
pipeline = rs.pipeline()
config = rs.config()
#config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
 
pipeline.start(config)
i = 1
try:
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if  not color_frame:
            continue
        color_image = np.asanyarray(color_frame.get_data())
 
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', color_image)
        
        key = cv2.waitKey(1)
        
        if key & 0xFF == ord('s') :
            cv2.imwrite(str(i)+'.jpg', color_image)
            i = i + 1
            
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
finally:
    pipeline.stop()