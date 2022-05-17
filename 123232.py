import dlib
import cv2
import pyrebase
import numpy as np
import os
def MyFace(face_d):
    
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
  all_files = storage.child().list_files()



  #upload
  #storage.child(my_image).put(my_image)
  #download
  #storage.child(my_image).download(filename="facefolder/1.jpg", path=os.path.basename(my_image))

  for file in all_files:      # 사진 하나씩 firebase 에서 다운로드
    try:
      file.download_to_filename("facefolder/1.jpg")
      
      img = cv2.imread("facefolder/1.jpg")   # 이미지 출력
      #img = cv2.resize(image, dsize=(640, 480), interpolation=cv2.INTER_AREA)   #이미지크기 조절 함수
      #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #색

      predictor_path = 'shape_predictor_68_face_landmarks.dat'
      face_recog = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
      print('emfd')

      detector = dlib.get_frontal_face_detector()
      predictor = dlib.shape_predictor(predictor_path)
      
      print('emfdjdha?')
      dets=detector(img,1)
      for face in dets :
          
        shape = predictor(img, face)
        landmarks = np.matrix([[p.x, p.y] for p in shape.parts()])
        
        for num in range(shape.num_parts):
            cv2.circle(img, (shape.parts()[num].x, shape.parts()[num].y), 3, (0,255,0), -1)
            
      
      face_descriptor = face_recog.compute_face_descriptor(img,shape)
      print(face_descriptor)

     
    except:
      print("Download Failed")



MyFace(1)

