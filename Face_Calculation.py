import Face_Function

import Doorlock_Move

import Firebase_Main

import cv2

import dlib

import numpy as np

import os

from datetime import datetime



def MyFace(face_d,img_count):
    
  now = datetime.now()

  predictor_path=Face_Function.Face_Function.predictor_path
  
  face_recog= Face_Function.Face_Function.face_recog

  detector= Face_Function.Face_Function.detector
  
  predictor = Face_Function.Face_Function.predictor
    
  count=0
  
  for a in range(len(img_count)):
      
      img = cv2.imread("facefolder/{}".format(img_count[a]))
      
      img = cv2.resize(img,dsize=(640,480))

      dets=detector(img,0)
      
      for face in dets :
          
        shape = predictor(img, face)
        
        print(a)
        
        face_descriptor = face_recog.compute_face_descriptor(img,shape)
                      
        face_descriptors = np.array(face_descriptor)

        x=np.array([face_d])
        
        y=np.array([face_descriptors])

        dist = np.linalg.norm(x-y, axis=1)
        
        print(dist)
        
        if dist <= 0.4:

          print('sameeeeeeeeee')

          data={"name":"{}_{}".format(now.strftime('%Y-%m-%d %H:%M:%S'),img_count[a])}
          
          db=Firebase_Main.Token.db
          
          db.child("OpenDoor_Log").push(data)

          Doorlock_Move.Doorlock()
          
        if dist > 0.4:
            
          print('Wrong')
          
