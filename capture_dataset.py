import numpy as np
import cv2
import os
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# Haarcascade for face detection
face_cascade = cv2.CascadeClassifier('face.xml')

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
# eye_cascade = cv2.CascadeClassifier('eye.xml')

#Start webcam
cap = cv2.VideoCapture(0)

#enter username for which u want to train
path = input("enter new user:")
# if not os.path.exists(path):
# 	os.mkdir(path)

c=1

while 1:

    #capture video frame
    ret, img = cap.read()

    #convert to greyscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detect faces in image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #store user in dataset folder
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        cv2.imwrite("dataset/"+path+"."+str(c)+".jpg",roi_gray)
        # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # roi_color = img[y:y+h, x:x+w]
        c+=1
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
        #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    #display image
    cv2.imshow('img',img)
    
    #exit loop condition
    k = cv2.waitKey(300) & 0xff
    if k == 27:
        break

#close webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
