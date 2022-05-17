import dlib
import numpy as np
import cv2
import ex2
import pyrebase
import os

def filedown(cnt):
    
     all_files = storage.child().list_files()
     
     for file in all_files:
      print(file)
      file.download_to_filename("facefolder/{}.jpg".format(cnt))
      cnt+=1

config = {  "apiKey": "AIzaSyBTGrklWDyt2cWXL3XVgV7AvJLeQXX60iQ",
    "authDomain": "smart-doorlock-c9e00.firebaseapp.com",
    "databaseURL": "https://smart-doorlock-c9e00-default-rtdb.firebaseio.com",
    "projectId": "smart-doorlock-c9e00",
    "storageBucket": "smart-doorlock-c9e00.appspot.com",
    "messagingSenderId": "404335392148",
    "appId": "1:404335392148:web:75c6d6f8572fea4dbf4b81",
    "measurementId": "G-7TB1L2YDF4",
    "serviceAccount": "smart-doorlock-c9e00-firebase-adminsdk-qge67-165a3f65b6.json"}
# firebase 사진 불러오기
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()

#all_files = storage.child().list_files()

cap = cv2.VideoCapture(0)

predictor_path = 'shape_predictor_68_face_landmarks.dat'
face_recog = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)


count=0
noface=0
while(cap.isOpened()):
    ret, frame = cap.read()
        
    #frame = cv2.flip(frame, 1)  #sangha
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
            print(dets)
            #landmarks = np.matrix([[p.x, p.y] for p in shape.parts()])
            
                    # make prediction and transform to numpy array

            #land = predictor(img_rgb, d)
                    
            
            
            #create list to contain landmarks
            for num in range(shape.num_parts):
                cv2.circle(frame, (shape.parts()[num].x, shape.parts()[num].y), 3, (0,255,0), -1)
                
                
            if count==20 :
                #face_descriptors = []
                face_descriptor = face_recog.compute_face_descriptor(frame,shape)
                #print(frame)
                
                face_descriptors= np.array(face_descriptor)
                #face_desriptor= np.array(face_descriptor)
                #print(face_descriptors)
                
                img_count = os.listdir('facefolder/')
                print(img_count)
                ex2.MyFace(face_descriptors,img_count)
                
                
        
    else:
        #print(noface)
        if(noface==1):
          cnt=0
          
          filedown(cnt)
            
    cv2.imshow('frame', frame)
        #out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q pressed")
        break
    
cap.release()
#out.release()

#cv2.destroyAllWindows()



