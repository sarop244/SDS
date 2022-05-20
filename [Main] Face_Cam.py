import Face_Calculation

import Face_Function

import Firebase_Main

import cv2

import dlib

import pyrebase

import numpy as np

import os

from math import hypot


def midpoint(p1, p2):
    
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

def get_blinking(eye_points, facial_landmarks):
    
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)

    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)

    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))

    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))
 
    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_lenght / ver_line_lenght

    return ratio


#def filedown(cnt):
    
     #all_files = storage.child().list_files()
     
     #for file in all_files:
      #print(file)
      #file.download_to_filename("facefolder/{}.jpg".format(cnt))
      #cnt+=1

#config = {  "apiKey": "AIzaSyBTGrklWDyt2cWXL3XVgV7AvJLeQXX60iQ",
    #"authDomain": "smart-doorlock-c9e00.firebaseapp.com",
    #"databaseURL": "https://smart-doorlock-c9e00-default-rtdb.firebaseio.com",
    #"projectId": "smart-doorlock-c9e00",
    #"storageBucket": "smart-doorlock-c9e00.appspot.com",
    #"messagingSenderId": "404335392148",
    #"appId": "1:404335392148:web:75c6d6f8572fea4dbf4b81",
    #"measurementId": "G-7TB1L2YDF4",
    #"serviceAccount": "smart-doorlock-c9e00-firebase-adminsdk-qge67-165a3f65b6.json"}
            
# firebase 사진 불러오기
#Firebase_Token= Firebase_Token.Token()
#Firebase_Token=Firebase_FaceImage.Token()
firebase = Firebase_Main.Token.firebase

auth = Firebase_Main.Token.auth

storage = Firebase_Main.Token.storage

#all_files = storage.child().list_files()

cap = cv2.VideoCapture(0)

#predictor_path = 'shape_predictor_68_face_landmarks.dat'
#face_recog = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")


#detector = dlib.get_frontal_face_detector()
#predictor = dlib.shape_predictor(predictor_path)


predictor_path=Face_Function.Face_Function.predictor_path

face_recog= Face_Function.Face_Function.face_recog

detector= Face_Function.Face_Function.detector

predictor = Face_Function.Face_Function.predictor

r_eye_points = [42, 43, 44, 45, 46, 47]

l_eye_points = [36, 37, 38, 39, 40, 41]

blinking_count=0

count=0

noface=0

while(cap.isOpened()):
    
    ret, frame = cap.read()
    #frame = cv2.imread("facefolder/2.jpg")
    frame = cv2.resize(frame,dsize=(640,480))
    
    frame = cv2.flip(frame,1)
    #frame = cv2.resize(frame,dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #frame =  all_files.download_to_filename("facefolder/1.jpg")#sangha
    dets = detector(frame, 0)
    
    #img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    count%=21  # 10번중에 한번 좌표따기
    
    count+=1
    
    noface%=50
    
    noface+=1
    #landmark
    
    if dets:
        
        for k, d in enumerate(dets):
            
            shape = predictor(frame, d)
            
            right_eye = get_blinking(r_eye_points, shape)
        
            left_eye = get_blinking(l_eye_points, shape)
            
            blinking = (left_eye + right_eye) / 2
            
            if(blinking>=5.0):
                
                blinking_count+=1
                
            print(blinking_count)
            
            #print(dets)
            #landmarks = np.matrix([[p.x, p.y] for p in shape.parts()])
            
                    # make prediction and transform to numpy array

            #land = predictor(img_rgb, d)
                    
            
            
            #create list to contain landmarks
            for num in range(shape.num_parts):
                
                cv2.circle(frame, (shape.parts()[num].x, shape.parts()[num].y), 3, (0,255,0), -1)
                
                
            if count==20 and blinking_count>=1 :
                #face_descriptors = []
                face_descriptor = face_recog.compute_face_descriptor(frame,shape)
                #print(frame)
                
                face_descriptors= np.array(face_descriptor)
                #face_desriptor= np.array(face_descriptor)
                #print(face_descriptors)
                
                img_count = os.listdir('facefolder/')
                #print(img_count)
                Face_Calculation.MyFace(face_descriptors,img_count)
                
                
        
    else:
        
        if(noface==1):
            
          cnt=0
          
          blinking_count=0
          
#           all_files = storage.child().list_files()
#           print('s')
#           for file in all_files:
#              print(file)
#              file.download_to_filename("facefolder/{}.jpg".format(cnt))
#              cnt+=1
          Firebase_Main.Filedown(cnt)
            
    cv2.imshow('frame', frame)
    #cv2.imshow('frame2', frame2)
        #out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        print("q pressed")
        
        break
    
cap.release()
#out.release()

#cv2.destroyAllWindows()



