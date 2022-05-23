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

def DelImage():
    
    if os.path.exists('facefolder/'):
        
        for file in os.scandir('facefolder'):
            
            print('Remoce file: ',file)
            
            os.remove(file)

firebase = Firebase_Main.Token.firebase

auth = Firebase_Main.Token.auth

storage = Firebase_Main.Token.storage

cap = cv2.VideoCapture(0)

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
   
    frame = cv2.resize(frame,dsize=(640,480))
    
    frame = cv2.flip(frame,1)
    
    dets = detector(frame, 0)
    
    count%=16  
    
    count+=1
    
    noface%=100
    
    noface+=1
    
    if dets:
        
        for k, d in enumerate(dets):
            
            shape = predictor(frame, d)
            
            right_eye = get_blinking(r_eye_points, shape)
        
            left_eye = get_blinking(l_eye_points, shape)
            
            blinking = (left_eye + right_eye) / 2
            
            if(blinking>=5.0):
                
                blinking_count+=1
                
            print(blinking_count)

            for num in range(shape.num_parts):
                
                cv2.circle(frame, (shape.parts()[num].x, shape.parts()[num].y), 3, (0,255,0), -1)
                
            if count==15 and blinking_count>=1 :

                face_descriptor = face_recog.compute_face_descriptor(frame,shape)
                
                face_descriptors= np.array(face_descriptor)

                img_count = os.listdir('facefolder/')
                
                Face_Calculation.MyFace(face_descriptors,img_count)
        
    else:
        
        if(noface==1):
            
          cnt=0
          
          blinking_count=0
          
          DelImage()
          
          Firebase_Main.Filedown(cnt)
            
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        print("q pressed")
        
        break
    
cap.release()



