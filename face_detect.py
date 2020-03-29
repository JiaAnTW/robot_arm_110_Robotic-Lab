import dlib
import cv2
import pyrealsense2 as rs
import numpy as np
import shutil 
import sys,os,glob


path_photos_from_camera = "data/data_faces_from_camera/"
path_csv_from_photos = "data/data_csvs_from_camera/"
def pre_work_del_old_face_folders():
      # delete the previous data & folder both images and csv file
    folders_rd = os.listdir(path_photos_from_camera)
    for i in range(len(folders_rd)):
        shutil.rmtree(path_photos_from_camera+folders_rd[i])
 
    csv_rd = os.listdir(path_csv_from_photos)
    for i in range(len(csv_rd)):
        os.remove(path_csv_from_photos+csv_rd[i])
  
def pre_work_mkdir():
  
    # make folders to save faces images and csv
    if os.path.isdir(path_photos_from_camera):
        pass
    else:
        os.mkdir(path_photos_from_camera)
    if os.path.isdir(path_csv_from_photos):
        pass
    else:
        os.mkdir(path_csv_from_photos)




def face_detect():
    
    path_photos_from_camera = "data/data_faces_from_camera/"
    path_csv_from_photos = "data/data_csvs_from_camera/"
    #pre_work_del_old_face_folders() delete the previous data folder
    #open folder
    pre_work_mkdir()
   
    # counter of screen shot
    cnt_ss = 0 
    #the path to store photo
    current_face_dir = ""
    # if old face exists, start from person_x+1
    if os.listdir("data/data_faces_from_camera/"):
    # get the number of data
        person_list = os.listdir("data/data_faces_from_camera/")
        person_list.sort()
        person_num_latest = int(str(person_list[-1]).split("_")[-1])
        person_cnt = person_num_latest
  
    # if the file is empty then start from person_1
    # start from person_1
    else:
        person_cnt = 0
    # the flag to control if save
    save_flag = 1
    # the flag to check if press 'n' before 's'
    press_n_flag = 0
    
    
    # Configure depth and color streams
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    # Start streaming
    pipeline.start(config)

    detector = dlib.get_frontal_face_detector()
    color_green = (0, 255, 0)
    line_width = 3
    try:
        while True:
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()
            if not depth_frame or not color_frame:
                continue
       
            rgb_image = np.asanyarray(color_frame.get_data())
            img_gray = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
            faces = detector(img_gray, 0)
            #font to write
            font = cv2.FONT_HERSHEY_COMPLEX
           
            key = cv2.waitKey(1)


            if key == ord('n'):
                person_cnt += 1
                current_face_dir = path_photos_from_camera + "person_" + str(person_cnt)
                os.makedirs(current_face_dir)
                print('\n')
                print(" Create folders: ", current_face_dir)
 
                cnt_ss = 0              #  clear the cnt of facesq
                press_n_flag = 1        # have pressed 'n'
                print("press n !")
            
            if len(faces) != 0:
            # show the rectangle box
                for k, d in enumerate(faces):
                    # we need to compute the width and height of the box
                    # (x,y), (width, height)
                    pos_start = tuple([d.left(), d.top()])
                    pos_end = tuple([d.right(), d.bottom()])
    
                    # compute the size of rectangle box
                    height = (d.bottom() - d.top())
                    width = (d.right() - d.left())
 
                    hh = int(height/2)
                    ww = int(width/2)
                    #  the color of rectangle of faces detected
                    color_rectangle = (255, 255, 255)
                    if (d.right()+ww) > 640 or (d.bottom()+hh > 480) or (d.left()-ww < 0) or (d.top()-hh < 0):
                        print('save flag is 0!')
                        cv2.putText(rgb_image, "OUT OF RANGE", (20, 300), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                        color_rectangle = (0, 0, 255)
                        save_flag = 0
                    else:
                        print('save flag is 1!')
                        color_rectangle = (255, 255, 255)
                        save_flag = 1
 
                    cv2.rectangle(rgb_image,
                              tuple([d.left() - ww, d.top() - hh]),
                              tuple([d.right() + ww, d.bottom() + hh]),
                              color_rectangle, 2)
 
                    #  create blank image according to the size of face detected
                    im_blank = np.zeros((int(height*2), width*2, 3), np.uint8)
                   
                    if save_flag:
                        #  press 's' to save faces into local images
                        if key == ord('s'):
                            # check if you have pressed 'n'
                            if press_n_flag:
                                cnt_ss += 1
                                for ii in range(height*2):
                                    for jj in range(width*2):
                                        im_blank[ii][jj] = rgb_image[d.top()-hh + ii][d.left()-ww + jj]
                                cv2.imwrite(current_face_dir + "/img_face_" + str(cnt_ss) + ".jpg", im_blank)
                            print(" Save into：", str(current_face_dir) + "/img_face_" + str(cnt_ss) + ".jpg")
                        else:
                            print(" Please press 'N' before 'S'")
 
                #  show the numbers of faces detected
            cv2.putText(rgb_image, "Faces: " + str(len(faces)), (20, 100), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
 
                #  add some statements
            cv2.putText(rgb_image, "Face Register", (20, 40), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(rgb_image, "N: New face folder", (20, 350), font, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(rgb_image, "S: Save current face", (20, 400), font, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(rgb_image, "Q: Quit", (20, 450), font, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.imshow("camera", rgb_image)
                # Press esc or 'q' to close the image window
            if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
    finally:
        # Stop streaming
        pipeline.stop()
if __name__ == "__main__":
    face_detect()        