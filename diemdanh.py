import cv2
import numpy as np
import os 
import RPi.GPIO as GPIO
import time
from time import sleep
from openpyxl import Workbook

RELAY = 5
P = 6
MODE = 13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)
GPIO.output(RELAY,GPIO.LOW)

GPIO.setup(P, GPIO.OUT)
GPIO.output(P,GPIO.LOW)

GPIO.setup(MODE, GPIO.OUT)
GPIO.output(MODE,GPIO.LOW)

wb = Workbook()
sheet = wb.active
temp =''
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX
dem = 0
#khoi tao bo dem id:
id = 0

# nhap ten id:
names = ['ID0: ',
         'ID1: Mr Thanh',
         'ID2: ',
         'ID3: ',
         'ID4: ']

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

    faces = faceCascade.detectMultiScale( 
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
            dem += 1
            id = names[id]
            tenid = str(id)
            confidence = "  {0}%".format(round(100 - confidence))
            if tenid != temp:
                now = time.strftime("%x")  
                sheet['A{}'.format(dem)] = now  
                sheet['B{}'.format(dem)] = tenid
            temp = tenid
        else:
            id = "Khong xac dinh"
            confidence = "  {0}%".format(round(100 - confidence))
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('KHOA CUA THONG MINH',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Xoa cache:
print("\n [INFO] Thoat chuong trinh")
d4 = time.strftime("%b-%d-%Y")
wb.save('{}-du-lieu.xlsx'.format(d4)) 
cam.release()
cv2.destroyAllWindows()
