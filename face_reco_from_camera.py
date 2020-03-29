import dlib          
import numpy as np   
import cv2          
import pandas as pd  
import pyrealsense2 as rs
 
 
 # face recognition model, the object maps human faces into 128D vectors
 # Refer this tutorial: http://dlib.net/python/index.html#dlib.face_recognition_model_v1
facerec = dlib.face_recognition_model_v1("data/data_dlib/dlib_face_recognition_resnet_model_v1.dat")
 
 

 # compute the e-distance between two 128D features
def return_euclidean_distance(feature_1, feature_2):
    feature_1 = np.array(feature_1)
    feature_2 = np.array(feature_2)
    dist = np.sqrt(np.sum(np.square(feature_1 - feature_2)))
    return dist
 

def face_reco_from_camera():
 # process csv feature data
    facerec = dlib.face_recognition_model_v1("data/data_dlib/dlib_face_recognition_resnet_model_v1.dat")
    path_features_known_csv = "data/features_all.csv"
    csv_rd = pd.read_csv(path_features_known_csv, header=None)
 

 # the array to save the features of faces in the database
    features_known_arr = []


 # print known faces
    for i in range(csv_rd.shape[0]):
        features_someone_arr = []
        for j in range(0, len(csv_rd.ix[i, :])):
            features_someone_arr.append(csv_rd.ix[i, :][j])
        features_known_arr.append(features_someone_arr)
    print("Faces in Database：", len(features_known_arr))
#input the path of image
    img_rd = cv2.imread('emma_test.jpg')

 # The detector and predictor will be used
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('data/data_dlib/shape_predictor_68_face_landmarks.dat')
 
#img_rd = np.asanyarray(img.get_data())
    img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)
    faces = detector(img_gray, 0)
#font to write
    font = cv2.FONT_HERSHEY_COMPLEX

#dets = detector(rgb_image)
#cv2.imshow("camera", img_rd)
    kk = cv2.waitKey(0)
    pos_namelist = []
    name_namelist = []
  
 # press 'q' to exit
    if kk == ord('q'):
        cv2.destroyAllWindows()
    else:
# when face detected
        if len(faces) != 0:
            print('detect face!')      
    # get the features captured and save into features_cap_arr
            features_cap_arr = []
            for i in range(len(faces)):
                shape = predictor(img_rd, faces[i])
                features_cap_arr.append(facerec.compute_face_descriptor(img_rd, shape))

            # traversal all the faces in the database
                for k in range(len(faces)):
                    print("##### camera person", k+1, "#####")
                 # 让人名跟随在矩形框的下方
                 # 确定人名的位置坐标
                 # 先默认所有人不认识，是 unknown
                 # set the default names of faces with "unknown"
                    name_namelist.append("unknown")
 
                 #  the positions of faces captured
                    pos_namelist.append(tuple([faces[k].left(), int(faces[k].bottom() + (faces[k].bottom() - faces[k].top())/4)]))
 
                 
                 # for every faces detected, compare the faces in the database
                    e_distance_list = []
                    for i in range(len(features_known_arr)):
                        # if person_X is not empty
                        if str(features_known_arr[i][0]) != '0.0':
                            print("with person", str(i + 1), "the e distance: ", end='')
                            e_distance_tmp = return_euclidean_distance(features_cap_arr[k], features_known_arr[i])
                            print(e_distance_tmp)
                            e_distance_list.append(e_distance_tmp)
                        else:
                        # empty person_X
                            e_distance_list.append(999999999)
                        # Find the one with minimum e distance
                            similar_person_num = e_distance_list.index(min(e_distance_list))
                        # print(e_distance_list)
                        # print(similar_person_num)
                            print("Minimum e distance with person", int(similar_person_num)+1)
                        #if min(e_distance_list) < 0.4:
                        # Here you can modify the names shown on the camera
                            name_namelist[k] = "Person "+str(int(similar_person_num)+1)
                            print("May be person "+str(int(similar_person_num)+1))
                        #else:
                           # print("Unknown person")

                         # draw rectangle
                            for kk, d in enumerate(faces):
                                cv2.rectangle(img_rd, tuple([d.left(), d.top()]), tuple([d.right(), d.bottom()]), (0, 255, 255), 2)
                            print('\n')
 
                      # write names under rectangle
                        for i in range(len(faces)):
                            cv2.putText(img_rd, name_namelist[i], pos_namelist[i], font, 0.8, (0, 255, 255), 1, cv2.LINE_AA)
 
    print("Faces in camera now:", name_namelist, "\n")

    cv2.putText(img_rd, "Press 'q': Quit", (20, 450), font, 0.8, (84, 255, 159), 1, cv2.LINE_AA)
    cv2.putText(img_rd, "Face Recognition", (20, 40), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img_rd, "Faces: " + str(len(faces)), (20, 100), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
 
     # show with opencv
    cv2.imshow("camera", img_rd)
    cv2.waitKey(0)
if __name__ == "__main__":
    face_reco_from_camera()