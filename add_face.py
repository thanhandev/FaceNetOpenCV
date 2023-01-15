import cv2
import os

cam = cv2.VideoCapture(0)#cấu hình địa chỉ camera
cam.set(3, 640) # cài chiều rộng video
cam.set(4, 480) # cài chiều cao video

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
#sử dụng haarcascade_frontalface_default tách khuôn mặt

# Nhập ID:
face_id = input('\n Nhap ID roi bam Enter <return> ==>  ')

print("\n [INFO] Vui long nhin vao camera ...")
# Khởi tạo biến đếm số khuôn mặt đã chụp:
count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Lưu ảnh:
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Nhấn ESC để thoát
    if k == 27:
        break
    elif count >= 80: # Chụp 80 ảnh rồi dừng
         break

# Xoá cache
print("\n [INFO] Thoat chuong trinh")
cam.release()
cv2.destroyAllWindows()


