import cv2
import numpy as np
import os 
import time
from time import sleep
#phat hien khuon mat su dung OpenCV:
recognizer = cv2.face.LBPHFaceRecognizer_create()
#lay co so du lieu da dao tao:
recognizer.read('trainer/trainer.yml')
#trinh nhan dien khuon mat
FaceNet = "facenet_opencv.xml"
FacerRecognition = cv2.CascadeClassifier(FaceNet);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['ID0: ',
         'ID1: Ten nguoi 1',
         'ID2: Ten nguoi 2',
         'ID3: Ten nguoi 3',
         'ID4: Ten nguoi 4']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = FacerRecognition.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 45):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "Khong xac dinh"
            confidence = "  {0}%".format(round(100 - confidence))
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('KHOA CUA THONG MINH',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Thoat chuong trinh")
cam.release()
cv2.destroyAllWindows()
