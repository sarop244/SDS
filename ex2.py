import dlib
import cv2
import numpy as np
import os
def MyFace(face_d,img_count):
    
  print(img_count)
  
  predictor_path = 'shape_predictor_68_face_landmarks.dat'
  face_recog = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
  print('lag')

  detector = dlib.get_frontal_face_detector()
  predictor = dlib.shape_predictor(predictor_path)
  



  #upload
  #storage.child(my_image).put(my_image)
  #download
  #storage.child(my_image).download(filename="facefolder/1.jpg", path=os.path.basename(my_image))
  count=0
  
  #for x in range(len(img_count)):      # 사진 하나씩 firebase 에서 다운로드
    #try:
      #print(all_files)
      #while count<=len(all_files):
          #file.download_to_filename("facefolder/{}.jpg".format(count))
          #print(file)
          #img = cv2.imread("facefolder/{}.jpg".format(count))   # 이미지 출력
      #img = cv2.resize(image, dsize=(640, 480), interpolation=cv2.INTER_AREA)   #이미지크기 조절 함수
      #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #색
  for a in range(len(img_count)):
      
      img = cv2.imread("facefolder/{}.jpg".format(a))
      img = cv2.resize(img,dsize=(640,480))
      #img = cv2.resize(img,dsize=(0,0), fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
      #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      #print('emfdjdha?')
      dets=detector(img,0)
      for face in dets :
        shape = predictor(img, face)
        #landmarks = np.matrix([[p.x, p.y] for p in shape.parts()])
        
        #for num in range(shape.num_parts):
            #cv2.circle(img, (shape.parts()[num].x, shape.parts()[num].y), 3, (0,255,0), -1)
            
      #face_descriptors = []
      print(a)
      face_descriptor = face_recog.compute_face_descriptor(img,shape)
                
      
      
      face_descriptors = np.array(face_descriptor)
      #print('jebal')
      #print(face_d - face_descriptors)
      #y = face_d - face_descriptors
      #print(np.linalg.norm(face_descriptors))
      #print('jebalrrrrrrrrrrrrrrr')
      #dist = np.linalg.norm(y)#유클리디안 거리계산
      #print(dist)
      
      #print(np.array(face_descriptors))
      #print(face_descriptor)
      
      #np.save('faceDescs/' +'1'+'.npy',face_descriptors)
      #print('asdf')
      
      #for i in range(len(img_count)):
      #print('asdfdfasdfs')
        #descs = np.load('facefolder/' + img_count[i], allow_pickle=True)[()]
        
        #for name, saved_desc in descs.items():

      a=np.array([face_d])
      b=np.array([face_descriptors])
      #print(a)
      #print(b)
      dist = np.linalg.norm(a-b, axis=1)#유클리디안 거리계산
      print(dist)  
      if dist <= 0.4:
            #last_found = {'name': name, 'dist': dist, 'color': (255,255,255)}
        print('sameeeeeeeeee')
      if dist > 0.4:
        print('Wrong')
                    #if(count_blinking >= 1):
                        #print("등록된 사용자입니다.")
                        #face_doorlock_test.main()
                        #last_found = {'name': name, 'dist': dist, 'color': (255,255,255)}
                        #cv2.rectangle(img_bgr, pt1=(d.left(), d.top()), pt2=(d.right(), d.bottom()), color=last_found['color'], thickness=2)
                        #cv2.putText(img_bgr, last_found['name'], org=(d.left(), d.top()), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=last_found['color'], thickness=2)
                        #detect_value = False
          #dist = np.linalg.norm([face_d] - face_descriptor, axis=1)#유클리디안 거리계산
            

          #print(dist)

     
    #except:
      #print("Download Failed")


#MyFace(1,[1,2,3])

