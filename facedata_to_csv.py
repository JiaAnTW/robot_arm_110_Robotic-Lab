import cv2
import os
import dlib
from skimage import io
import csv
import numpy as np


# the path to read images
path_images_from_camera = "data/data_faces_from_camera/"
 
# Dlib front_face detector
detector = dlib.get_frontal_face_detector()
 
# Dlib face_predictor
predictor = dlib.shape_predictor("data/data_dlib/shape_predictor_68_face_landmarks.dat")
 
 # Face recognition model, the object maps human faces into 128D vectors
face_rec = dlib.face_recognition_model_v1("data/data_dlib/dlib_face_recognition_resnet_model_v1.dat")
 
 
 # return the single image  128D features
def return_128d_features(path_img):
    img_rd = io.imread(path_img)
    img_gray = cv2.cvtColor(img_rd, cv2.COLOR_BGR2RGB)
    faces = detector(img_gray, 1)
 
    print("%-40s %-20s" % ("image with faces detected:", path_img), '\n')
 
     # make sure that the image is really a human face
    if len(faces) != 0:
        shape = predictor(img_gray, faces[0])
        face_descriptor = face_rec.compute_face_descriptor(img_gray, shape)
    else:
        face_descriptor = 0
        print("no face")
 
    return face_descriptor
 
 
 # write features into csv file
def return_features_mean_personX(path_faces_personX):
    features_list_personX = []
    photos_list = os.listdir(path_faces_personX)
    if photos_list:
        for i in range(len(photos_list)):
             # use return_128d_features() to get 128D feature
            print("%-40s %-20s" % (" image to read:", path_faces_personX + "/" + photos_list[i]))
            features_128d = return_128d_features(path_faces_personX + "/" + photos_list[i])
             # print(features_128d)
             # skip the image that didnt detect human face
            if features_128d == 0:
                i += 1
            else:
                features_list_personX.append(features_128d)
    else:
        print(" Warning: No images in " + path_faces_personX + '/', '\n')
 
     # compute 128D features
     # N x 128D -> 1 x 128D
    if features_list_personX:
        features_mean_personX = np.array(features_list_personX).mean(axis=0)
    else:
        features_mean_personX = '0'
  
    return features_mean_personX
 
 
 # read the whole images of a person
def write_to_csv():
    people = os.listdir(path_images_from_camera)
    people.sort()
 
    with open("data/features_all.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for person in people:
            print("##### " + person + " #####")
         # Get the mean/average features of face/personX, it will be a list with a length of 128D
            features_mean_personX = return_features_mean_personX(path_images_from_camera + person)
            writer.writerow(features_mean_personX)
            print(" The mean of features:", list(features_mean_personX))
            print('\n')
            print(" Save all the features of faces registered into: data/features_all.csv")

if __name__ == "__main__":
    write_to_csv()